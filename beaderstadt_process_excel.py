"""
Process an Excel file to determine what fast food company has the highest total calorie count on the menu.
"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import pandas as pd

# Import from external packages
import openpyxl

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name: str = "beaderstadt_data"
processed_folder_name: str = "data_processed"

#####################################
# Define Functions
#####################################

def find_company_with_highest_calories(file_path: pathlib.Path) -> tuple:
    """Determine which company has the highest total calorie count from an Excel file."""
    try:
        df = pd.read_excel(file_path)

        if 'Company' not in df.columns or 'Calories' not in df.columns:
            raise ValueError("The columns 'Company' and 'Calories' must exist in the Excel sheet.")
        
         # Convert 'Calories' to numeric, forcing errors to NaN 
        df['Calories'] = pd.to_numeric(df['Calories'], errors='coerce')

        # Remove rows where 'Calories' is NaN
        df = df.dropna(subset=['Calories'])
        
        # Group by company and sum calories for each company
        company_calories = df.groupby('Company')['Calories'].sum()
        
        # Find the company with the highest total calories
        highest_calories_company = company_calories.idxmax()
        highest_calories_value = company_calories.max()

        return highest_calories_company, highest_calories_value

    except Exception as e:
        logger.error(f"Error reading Excel file: {e}")
        return None, 0

def process_excel_file():
    """Read an Excel file, determine the company with the highest total calories, and save the result."""
    input_file = pathlib.Path(fetched_folder_name, "fastfood_data.xlsx")
    output_file = pathlib.Path(processed_folder_name, "excel_company_calories.txt")
    
    # Find the company with the highest calorie count
    company, calories = find_company_with_highest_calories(input_file)
    
    # Check if data is found
    if company is None:
        logger.error("Could not determine the company with the highest calories.")
        return

    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Write the result to the output file
    with output_file.open('w') as file:
        file.write(f"The Company with the highest total calorie count is '{company}' with {calories} calories\n")
    
    logger.info(f"Processed Excel file: {input_file}, Results saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting Excel processing...")
    process_excel_file()
    logger.info("Excel processing complete.")
