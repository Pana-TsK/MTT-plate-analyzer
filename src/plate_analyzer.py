import os
import argparse
from data_loader import DataLoader
from plate_identifier import PlateIdentifier
from plate_processor import PlateProcessor
from viabilities_calculator import ViabilitiesCalculator
from results_saver import ResultsSaver

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Automate MTT assays processing.")
    parser.add_argument("input_file", help="Path to the input raw data Excel file")
    parser.add_argument("output_file", help="Path to save the processed results")
    return parser.parse_args()

def load_data(file_path):
    """Load raw data from an Excel file."""
    try:
        return DataLoader().load_data(file_path)
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def identify_plates(dataframe):
    """Identify plates from the loaded data."""
    try:
        return PlateIdentifier().identify_plates(dataframe)
    except Exception as e:
        print(f"Error identifying plates: {e}")
        return []

def process_plates(raw_plates):
    """Process the raw plates."""
    try:
        plate_processor = PlateProcessor()
        return plate_processor.process(raw_plates)
    except Exception as e:
        print(f"Error processing plates: {e}")
        return []

def calculate_viabilities(processed_data):
    """Calculate viabilities from processed data."""
    try:
        viabilities_calculator = ViabilitiesCalculator()
        return viabilities_calculator.calculate_viabilities(processed_data)
    except Exception as e:
        print(f"Error calculating viabilities: {e}")
        return []

def save_results(viabilities, output_filepath):
    """Save the calculated viabilities to a file."""
    try:
        results_saver = ResultsSaver()
        results_saver.save(viabilities, filepath=output_filepath)
    except Exception as e:
        print(f"Error saving results: {e}")

def main(input_file, output_file):
    """Main function to execute the full pipeline."""
    # Load the raw data
    dataframe = load_data(input_file)
    if dataframe is None:
        return  # Exit early if data loading fails

    # Identify the plates from the raw data
    raw_plates = identify_plates(dataframe)
    if not raw_plates:
        return  # Exit early if plates identification fails

    # Process the plates
    processed_data = process_plates(raw_plates)
    if not processed_data:
        return  # Exit early if plates processing fails

    # Calculate the viabilities
    viabilities = calculate_viabilities(processed_data)
    if not viabilities:
        return  # Exit early if viabilities calculation fails

    # Save the results
    save_results(viabilities, output_file)

if __name__ == "__main__":
    input_filepath = r"C:/Users/panag/OneDrive/Documents/coding/Projects/MTT plate analyzer/example_data/rawdata.xlsx"
    output_filepath = r"C:/Users/panag/OneDrive/Documents/coding/Projects/MTT plate analyzer/outputs/results3.xlsx"
    main(input_filepath, output_filepath)
