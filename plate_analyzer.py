import numpy as np
import pandas as pd


class PlateAnalyzer:
    def __init__(self, filepath="rawdata.xlsx", save_results=True, compounds=None):
        """
        Initializes the PlateAnalyzer class.
        Args:
            filepath (str): The path to the raw data file. Defaults to "rawdata.xlsx".
            save_results (bool): Whether to save the results after processing. Defaults to True.
            compounds (iterable): A list or range of compounds to analyze. Defaults to range(1, 13).
        Attributes:
            rawdata (DataFrame): The raw data loaded from the file.
            rawplates (list): The identified plates from the raw data.
            corrected_plates (list): The cleaned and processed plates.
            viabilities (list): The calculated viabilities for the plates.
            compounds (iterable): The list or range of compounds to analyze.
        """

        self.rawdata = self.load_data(filepath)  # Load raw data
        self.rawplates = self.identify_plates()  # Identify plates from rawdata
        self.corrected_plates = self.process_clean_plates()  # Clean and process plates
        self.viabilities = self.calculate_viabilities()  # Calculate viabilities
        self.compounds = compounds or range(1, 13)  # Default to range(1, 13) if no compounds are provided

        if save_results:
            self.save_results()

    def load_data(self, filepath) -> pd.DataFrame:
        """Load raw data from the provided Excel file."""
        try:
            return pd.read_excel(filepath, header=None)  # Load without header, as data is unstructured
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{filepath}' was not found.")
        except Exception as e:
            raise Exception(f"An error occurred while loading the data: {e}")

    def __str__(self):
        """Return a string representation of the class"""
        return f"Plates: {self.viabilities}"

    def identify_plates(self) -> list:
        """Identify plates from raw data"""
        plate_starts = self.rawdata[self.rawdata[0].str.contains('Plate:', na=False)].index.tolist()
        plate_starts.append(len(self.rawdata) - 1)

        raw_plates = []
        for i in range(len(plate_starts) - 1):
            plate_data = self.rawdata.iloc[plate_starts[i]:plate_starts[i + 1]]
            plate_data = plate_data.reset_index(drop=True)
            raw_plates.append(plate_data)

        return raw_plates

    def process_clean_plates(self) -> list:
        """Process the plates by cleaning and splitting them."""
        cleaned_plates = []
        for plate in self.rawplates:
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
                cleaned_plates.append(cleaned_plate)

        return cleaned_plates

    def calculate_viabilities(self) -> list:
        """Calculate viabilities based on untreated cell mean."""
        viability_plates = []
        for plate in self.corrected_plates:
            control_means = plate.iloc[-1, :].mean()
            viability_plate = (plate.T / control_means).T * 100
            viability_plates.append(viability_plate)

        return viability_plates

    def save_results(self, filepath="results.xlsx") -> None:
        """Save the results to an Excel file."""
        with pd.ExcelWriter(filepath) as writer:
            for i, plate in enumerate(self.viabilities):
                rows = list('ABCDEFGH') * 12
                plate.index = rows[:len(plate)]

                # Use provided compound names if available
                plate.columns = self.compounds[:len(plate.columns)]

                plate.to_excel(writer, sheet_name=f"Plate_{i + 1}")


def main():
    # Initialize the class with optional compounds argument
    test_experiment = PlateAnalyzer(compounds=[f"Compound {i}" for i in range(1, 13)])
    print(test_experiment)


if __name__ == "__main__":
    main()
