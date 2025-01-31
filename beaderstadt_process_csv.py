"""
Process a CSV file on Netflix titles, to analyze the release year column and save statistics.
"""

#####################################
# Import Modules
#####################################

import pathlib
import csv
import statistics
from utils_logger import logger

fetched_folder_name: str = "beaderstadt_data"
processed_folder_name: str = "beaderstadt_processed"

def analyze_release_year(file_path: pathlib.Path) -> dict:
    """Analyze the release year column from Netflix titles to calculate min, max, mean, and stdev."""
    try:
        # Initialize an empty list to store the release years
        release_year_list = []
        with file_path.open('r', encoding='utf-8-sig') as file:
            # csv.DictReader() method to read into a DictReader so we can access named columns in the csv file
            dict_reader = csv.DictReader(file)
            for row in dict_reader:
                try:
                    release_year = int(row["release_year"])  # Extract and convert to release year to int
                    # Append the release year to the list
                    release_year_list.append(release_year)
                except ValueError as e:
                    logger.warning(f"Skipping invalid row: {row} ({e})")

        # Check if there are no valid release years
        if not release_year_list:
            logger.warning("No valid release year data found.")
            return {}
        
        # Calculate statistics
        stats = {
            "min": min(release_year_list),
            "max": max(release_year_list),
            "mean": statistics.mean(release_year_list),
            "stdev": statistics.stdev(release_year_list) if len(release_year_list) > 1 else 0,
        }
        return stats
    except Exception as e:
        logger.error(f"Error processing CSV file: {e}")
        return {}

def process_csv_file():
    """Read a CSV file, analyze release year data, and save the results."""
    input_file = pathlib.Path(fetched_folder_name, "netflix_movies.csv")
    output_file = pathlib.Path(processed_folder_name, "netflix_movies_stats.txt")
    
    stats = analyze_release_year(input_file)

    if not stats:
        logger.error("No valid statistics to save.")
        return
    
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with output_file.open('w') as file:
        file.write("Netflix Title Release Year Statistics:\n")
        file.write(f"Minimum: {stats['min']:.2f}\n")
        file.write(f"Maximum: {stats['max']:.2f}\n")
        file.write(f"Mean: {stats['mean']:.2f}\n")
        file.write(f"Standard Deviation: {stats['stdev']:.2f}\n")
    
    logger.info(f"Processed CSV file: {input_file}, Statistics saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting CSV processing...")
    process_csv_file()
    logger.info("CSV processing complete.")
