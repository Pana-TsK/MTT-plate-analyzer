import pandas
from data_loader import DataLoader
from plate_identifier import PlateIdentifier
from plate_processor import PlateProcessor

class ViabilitiesCalculator():
    def calculate_viabilities(self, corrected_plates) -> list:
        """Calculate viabilities based on untreated cell mean."""
        viability_plates = []
        for plate in corrected_plates:
            control_means = plate.iloc[-1, :].mean()
            viability_plate = (plate.T / control_means).T * 100
            viability_plates.append(viability_plate)

        return viability_plates
    
if __name__ == '__main__':
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
    
    # Print the processed data
    print(viabilities)