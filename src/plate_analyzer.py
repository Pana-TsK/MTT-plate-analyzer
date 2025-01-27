import os
import argparse
from data_loader import DataLoader
from plate_identifier import PlateIdentifier
from plate_processor import PlateProcessor
from viabilities_calculator import ViabilitiesCalculator
from results_saver import ResultsSaver


import argparse

class PlateAnalyzer:
    def __init__(self, file_path, save_results):
        self.file_path = file_path
        self.save_results_flag = save_results

    @staticmethod
    def parse_args():
        """Parse command line arguments."""
        parser = argparse.ArgumentParser(description="Automate MTT assays processing.")
        parser.add_argument("input_file", help="Path to the input raw data Excel file")
        parser.add_argument("output_file", help="Path to save the processed results")
        return parser.parse_args()

    def load_data(self):
        """Load raw data from an Excel file."""
        try:
            from data_loader import DataLoader  # Replace with your actual DataLoader implementation
            return DataLoader().load_data(self.file_path)
        except Exception as e:
            print(f"Error loading data: {e}")
            return None

    def identify_plates(self, dataframe):
        """Identify plates from the loaded data."""
        try:
            from plate_identifier import PlateIdentifier  # Replace with your actual PlateIdentifier implementation
            return PlateIdentifier().identify_plates(dataframe)
        except Exception as e:
            print(f"Error identifying plates: {e}")
            return []

    def process_plates(self, raw_plates):
        """Process the raw plates."""
        try:
            from plate_processor import PlateProcessor  # Replace with your actual PlateProcessor implementation
            return PlateProcessor().process(raw_plates)
        except Exception as e:
            print(f"Error processing plates: {e}")
            return []

    def calculate_viabilities(self, processed_data):
        """Calculate viabilities from processed data."""
        try:
            from viabilities_calculator import ViabilitiesCalculator  # Replace with your actual ViabilitiesCalculator implementation
            return ViabilitiesCalculator().calculate_viabilities(processed_data)
        except Exception as e:
            print(f"Error calculating viabilities: {e}")
            return []

    def save_results(self, viabilities, output_filepath):
        """Save the calculated viabilities to a file."""
        try:
            from results_saver import ResultsSaver  # Replace with your actual ResultsSaver implementation
            results_saver = ResultsSaver()
            results_saver.save(viabilities, filepath=output_filepath)
        except Exception as e:
            print(f"Error saving results: {e}")

    def run(self, output_filepath):
        """Execute the full pipeline."""
        # Load the raw data
        dataframe = self.load_data()
        if dataframe is None:
            print("Failed to load data.")
            return  # Exit early if data loading fails

        # Identify the plates from the raw data
        raw_plates = self.identify_plates(dataframe)
        if not raw_plates:
            print("Failed to identify plates.")
            return  # Exit early if plate identification fails

        # Process the plates
        processed_data = self.process_plates(raw_plates)
        if not processed_data:
            print("Failed to process plates.")
            return  # Exit early if plate processing fails

        # Calculate the viabilities
        viabilities = self.calculate_viabilities(processed_data)
        if not viabilities:
            print("Failed to calculate viabilities.")
            return  # Exit early if viabilities calculation fails

        # Save the results if the flag is set
        if self.save_results_flag:
            self.save_results(viabilities, output_filepath)


if __name__ == "__main__":
    # Example usage: Run from the command line with input and output file paths
    input_filepath = r"C:/Users/panag/OneDrive/Documents/coding/Projects/MTT plate analyzer/example_data/rawdata.xlsx"
    output_filepath = r"C:/Users/panag/OneDrive/Documents/coding/Projects/MTT plate analyzer/outputs/results3.xlsx"

    # Parse arguments if needed (uncomment to use argparse)
    # args = PlateAnalyzer.parse_args()
    # analyzer = PlateAnalyzer(file_path=args.input_file, save_results=True)

    # Direct usage
    analyzer = PlateAnalyzer(file_path=input_filepath, save_results=True)
    analyzer.run(output_filepath)

