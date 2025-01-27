import pandas as pd
from data_loader import DataLoader
from plate_identifier import PlateIdentifier

class PlateProcessor:
    def process(self, rawplates):
        """Process and clean plate data."""
        cleaned_plates = []
        for plate in rawplates:
            cleaned_plate = self.clean_plate(plate)
            cleaned_plates.append(cleaned_plate)
        return cleaned_plates

    def clean_plate(self, plate):
        """Process the plates by cleaning and splitting them."""
        measurements = plate.iloc[1:-1].reset_index(drop=True)
        measurements = measurements.drop(measurements.index[0])  # Drop the first row after setting it as the header
        measurements = measurements.iloc[:, 2:]  # Drop the first two columns
        measurements = measurements.apply(pd.to_numeric, errors='coerce')

        empty_cols = measurements.columns[measurements.isna().all()].tolist()
        if empty_cols:
            split_index = measurements.columns.get_loc(empty_cols[0])

            plate_570 = measurements.iloc[:, :split_index]
            plate_630 = measurements.iloc[:, split_index + 1:]

            plate_570.reset_index(drop=True, inplace=True)
            plate_630.reset_index(drop=True, inplace=True)

            plate_570.columns = range(len(plate_570.columns))
            plate_630.columns = range(len(plate_630.columns))

            cleaned_plate = plate_570 - plate_630
            return cleaned_plate
        
        return measurements  # In case there are no empty columns (fall-back)

if __name__ == '__main__':
    # Load the raw data
    dataframe = DataLoader().load_data(r"C:\Users\panag\OneDrive\Documents\coding\Projects\MTT plate analyzer\example_data\rawdata.xlsx")
    
    # Identify the plates from the raw data
    raw_plates = PlateIdentifier().identify_plates(dataframe)
    
    # Process the plates
    plate_processor = PlateProcessor()
    processed_data = plate_processor.process(raw_plates)
    
    # Print the processed data
    print(processed_data)
