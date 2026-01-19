import pandas as pd
import json
import logging
import argparse
from pathlib import Path

# --- CONFIGURATION ---
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def process_wine_data(input_csv: str, output_json: str):
    """
    Reads wine ratings, cleans missing data, filters by criteria, 
    and exports the result to a structured JSON file.
    """
    
    # 1. Path Management
    source_path = Path(input_csv)
    target_path = Path(output_json)

    if not source_path.exists():
        logger.error(f"File not found: {source_path}")
        return

    # 2. Load Dataset
    logger.info(f"Loading data from {source_path}...")
    try:
        df = pd.read_csv(source_path, index_col=0)
    except Exception as e:
        logger.error(f"Failed to read CSV: {e}")
        return

    # 3. Data Cleaning
    initial_count = len(df)
    
    # Remove completely empty columns
    df = df.dropna(axis=1, how='all')
    
    # Remove rows missing critical values
    df = df.dropna(subset=['rating', 'variety'])
    
    # Fill remaining empty cells with a placeholder
    df = df.fillna("Not Specified")
    
    cleaned_count = len(df)
    if initial_count > cleaned_count:
        logger.info(f"Data Cleaning: Removed {initial_count - cleaned_count} rows with missing values.")

    # 4. Filtering and Sorting
    logger.info("Filtering Red Wines with rating >= 90...")
    filter_mask = (df["variety"] == "Red Wine") & (df["rating"] >= 90)
    filtered_df = df[filter_mask].sort_values("rating", ascending=False)

    # 5. Export to JSON
    result = filtered_df.to_dict(orient="records")

    try:
        with open(target_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=4, ensure_ascii=False)
        logger.info(f"✅ Success! Exported {len(result)} records to {target_path}")
    except Exception as e:
        logger.error(f"Failed to save JSON: {e}")

def main():
    # --- COMMAND LINE ARGUMENTS ---
    parser = argparse.ArgumentParser(description="Process wine rating data.")
    parser.add_argument("path", help="Path to the input CSV file")
    parser.add_argument("--output", default="filtered_wines.json", help="Output JSON filename")
    
    args = parser.parse_args()
    
    process_wine_data(args.path, args.output)

if __name__ == "__main__":
    main()