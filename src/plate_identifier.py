import pandas as pd
from data_loader import DataLoader

class PlateIdentifier():
    def identify_plates(self, rawdata) -> list:
        """Identify plates from raw data"""
        plate_starts = rawdata[rawdata[0].str.contains('Plate:', na=False)].index.tolist()
        plate_starts.append(len(rawdata) - 1)

        raw_plates = []
        for i in range(len(plate_starts) - 1):
            plate_data = rawdata.iloc[plate_starts[i]:plate_starts[i + 1]]
            plate_data = plate_data.reset_index(drop=True)
            raw_plates.append(plate_data)

        return raw_plates


if __name__ == '__main__':
    dataframe = DataLoader().load_data(r"C:\Users\panag\OneDrive\Documents\coding\Projects\MTT plate analyzer\example_data\rawdata.xlsx")
    plate_identifier = PlateIdentifier()
    processed_data = plate_identifier.identify_plates(dataframe)
    print(processed_data)