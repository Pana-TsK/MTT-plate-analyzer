import os
import pandas as pd
from data_loader import DataLoader
from plate_identifier import PlateIdentifier
from plate_processor import PlateProcessor
from utils import create_directory
from viabilities_calculator import ViabilitiesCalculator

class ResultsSaver:
    def save(self, viabilities, filepath="results.xlsx"):
        """Save the results to an Excel file."""
        # Ensure the directory exists
        directory = os.path.dirname(filepath)
        create_directory(directory)

        # Write results to Excel file
        with pd.ExcelWriter(filepath) as writer:
            for i, plate in enumerate(viabilities):
                rows = list('ABCDEFGH') * 12
                plate.index = rows[:len(plate)]
                plate.to_excel(writer, sheet_name=f"Plate_{i + 1}")

if __name__ == "__main__":
    # Load the raw data
    dataframe = DataLoader().load_data(r"C:\Users\panag\OneDrive\Documents\coding\Projects\MTT plate analyzer\example_data\rawdata.xlsx")
    
    # Identify the plates from the raw data
    raw_plates = PlateIdentifier().identify_plates(dataframe)
    
    # Process the plates
    plate_processor = PlateProcessor()
    processed_data = plate_processor.process(raw_plates)

    # Calculate the viabilities
    viabilities_calculator = ViabilitiesCalculator()
    viabilities = viabilities_calculator.calculate_viabilities(processed_data)

    # Save the results (ensure full path, including filename)
    output_filepath = r"C:/Users/panag/OneDrive/Documents/coding/Projects/MTT plate analyzer/outputs/results2.xlsx"
    results_saver = ResultsSaver()
    results_saver.save(viabilities, filepath=output_filepath)
