"""
Process a JSON file to pair countries with their regions and save the result.

The JSON file has a structure where each country has a 'name' object containing 'common' and a 'region' at the root level.

Example JSON format:
[
    {
        "name": {
            "common": "Aruba",
            "official": "Aruba",
            "native": {
                "nld": {
                    "official": "Aruba",
                    "common": "Aruba"
                },
                "pap": {
                    "official": "Aruba",
                    "common": "Aruba"
                }
            }
        },
        "region": "Americas",
        "subregion": "Caribbean",
        "languages": {
            "nld": "Dutch"
        }
    },
    {
        "name": {
            "common": "Afghanistan",
            "official": "Afghanistan",
            "native": {
                "pes": {
                    "official": "Afghanistan",
                    "common": "Afghanistan"
                }
            }
        },
        "region": "Asia",
        "subregion": "Southern Asia",
        "languages": {
            "pes": "Persian"
        }
    }
]
"""


#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import json

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name: str = "beaderstadt_data"
processed_folder_name: str = "beaderstadt_processed"

#####################################
# Define Functions
#####################################

def pair_country_with_region(file_path: pathlib.Path) -> dict:
    """Pair the common country name with the region from a JSON file."""
    try:
        with file_path.open('r', encoding='utf-8') as file:
            data = json.load(file)

        country_region_pair = {}
        
        for country in data:
            # Check if 'name' and 'region' are in the dictionary
            common_name = country.get('name', {}).get('common') 
            region = country.get('region')
            
            if common_name and region:
                country_region_pair[common_name] = region
            else:
                logger.warning(f"Skipping entry with missing 'common' or 'region' field: {country}")
        
        return country_region_pair
    
    except Exception as e:
        logger.error(f"Error reading JSON file: {e}")
        return {}

def process_json_file():
    """Read a JSON file, pair countries with their regions, and save the result."""
    input_file = pathlib.Path(fetched_folder_name, "countries.json")
    output_file = pathlib.Path(processed_folder_name, "country_region_pairs.txt")
    
    # Get the country-region pairs
    country_region_data = pair_country_with_region(input_file)
    
    # Check if any pairs were found
    if not country_region_data:
        logger.error("Could not extract country-region pairs.")
        return

    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with output_file.open('w', encoding='utf-8') as file:
        for country, region in country_region_data.items():
            file.write(f"{country}: {region}\n")
    
    logger.info(f"Processed JSON file: {input_file}, Results saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info
