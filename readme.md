# PlateAnalyzer

PlateAnalyzer is a Python project designed to analyze 96-well plate data from laboratory experiments. The project processes absorbance measurements from two wavelengths, calculates cell viability percentages based on untreated control wells, and generates cleaned and normalized data for further analysis.

## Features

- **Data Processing**: Reads raw 96-well plate data from an Excel file and splits it into two 96-well plates for two wavelength absorbance readings.
- **Plate Normalization**: Corrects the data by calculating the difference between absorbance readings from two wavelengths (570 nm and 630 nm).
- **Viability Calculation**: Normalizes data to the untreated control wells and calculates cell viability percentages.
- **Results Export**: Saves the final results as an Excel file with each plate’s data and corresponding viability percentages.
  
## Installation

To get started with **PlateAnalyzer**, you need to set up the project and install the required dependencies. Follow these steps:

### 1. Clone the repository

First, clone the repository to your local machine using `git`:

```bash
git clone https://github.com/Pana-TsK/MTT-plate-analyzer.git
```
### 2. Navigate to the project directory
Once the repository is cloned, move into the project directory:
```bash
cd "MTT-plate-anaylzer"
```
### 3. Install dependencies

Once your virtual environment is activated, install the required dependencies by running the following command:
```bash
pip install -r requirements.txt
```

### 4. Use the PlateAnalyzer
```python
from plate_analyzer import PlateAnalyzer

# Create an instance of the PlateAnalyzer
plate_analyzer = PlateAnalyzer(filepath="path_to_rawdata.xlsx")

# Access the cleaned and analyzed data
print(plate_analyzer.viabilities)
```

## Usage
Perform the MTT assay in a number of 96-well plates, and analyze the data using a Dahaner well plate reader.
Dilutions can be made in any way that is desired, but the very last row should only contain untreated cells.
An example of how the data should be structured is provided, under the name of rawdata.xlsx.

To use PlateAnalyzer, simply instantiate the PlateAnalyzer class with the path to your raw data file. Here's an example of how to use the project
```python
from PlateAnalyzer import PlateAnalyzer

# Initialize the PlateAnalyzer with your raw data file and optional compounds names
analyzer = PlateAnalyzer(filepath="rawdata.xlsx", save_results=True, compounds=range(1, 13))

# Print a summary of the results
print(analyzer)
```
## How MTT Plate Analyzer works
Step 1: Identify Plates
The program reads the raw data and identifies individual plates using the word 'Plate:' as a delimiter. It then splits the data into separate plates.

Step 2: Clean Data
After identifying the plates, the program removes unnecessary rows, columns, and converts the data into numeric values. The two wavelength data are split into two plates: one for 570 nm and one for 630 nm.

Step 3: Calculate Viabilities
Viability is calculated by normalizing the difference between the 570 nm and 630 nm absorbance readings, with the untreated control wells used for normalization.

Step 4: Save Results
The processed data, including viability percentages, is saved into a new Excel file, with each plate's results in separate sheets.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
Panagiotis Tsampanis

## Acknowledgements
Inspired by real-world laboratory data processing needs in the field of Drug Discovery & Cell Biology.
Thanks to the open-source community for the tools that made this project possible.

## Contributions
Feel free to fork this repository and submit pull requests if you find bugs or want to add new features. If you have any suggestions or improvements, please open an issue!
