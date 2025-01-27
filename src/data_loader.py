import pandas as pd

class DataLoader():
    def load_data(self, filepath) -> pd.DataFrame:
        """Load row data from a provided Excel file."""
        try:
            return pd.read_excel(filepath, header=None)  # Load without header, as data is unstructured
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{filepath}' was not found.")
        except Exception as e:
            raise Exception(f"An error occurred while loading the data: {e}")

if __name__ == '__main__':
    data_loader = DataLoader()
    data = data_loader.Load_data(r"C:\Users\panag\OneDrive\Documents\coding\Projects\MTT plate analyzer\example_data\rawdata.xlsx")
    print(data)