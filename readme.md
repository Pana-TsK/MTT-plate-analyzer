# PlateAnalyzer

**PlateAnalyzer** is a Python-based tool designed to automate the processing of MTT assay data. This application takes raw data from Excel files, processes it through multiple stages (plate identification, processing, viability calculation), and saves the results in an easy-to-use format.

MTT assays are widely used in cell biology research to measure cell viability and cytotoxicity in response to various treatments, such as drug candidates or experimental conditions.

## Features
- **Load Raw Data**: Supports Excel files as input for MTT assay data.
- **Identify Plates**: Automatically detects plates and organizes raw data for processing.
- **Process Plates**: Cleans, organizes, and prepares the plate data for analysis.
- **Viability Calculation**: Calculates viabilities from the processed plate data.
- **Save Results**: Exports calculated viabilities to a specified output file.

## Installation
### Prerequisites
- Python 3.8 or higher
- Required Python libraries (install via `pip`):

```bash
pip install pandas openpyxl argparse
```

### Clone Repository
Clone the repository to your local machine:

```bash
git clone https://github.com/Pana-TsK/MTT-plate-analyzer
cd plate_analyzer
```
## Biological context
### Control wells
The bottom row of each plate contains untreated cells (no drugs or treatments), which are assumed to represent 100% viability. These control wells serve as the baseline for normalizing viability calculations.

### Dilution setup
Drug dilutions or experimental conditions can be organized in any direction (row-wise or column-wise).

### Plate Reader Compatibility
(Note: Specific plate reader brands will be added soon for reference.)

## Usage
### Running the Application
You can run the application either by specifying the input and output files in the script or using the command-line interface.

#### Example Script Usage
Modify the file paths in the script:

```python
input_filepath = r"C:/path/to/rawdata.xlsx"
output_filepath = r"C:/path/to/results.xlsx"
analyzer = PlateAnalyzer(file_path=input_filepath, save_results=True)
analyzer.run(output_filepath)
```

Run the script:

```bash
python plate_analyzer.py
```

#### Command-Line Usage
To use the command-line interface, uncomment the argument parser in the script and run:

```bash
python plate_analyzer.py /path/to/rawdata.xlsx /path/to/results.xlsx
```

### Input/Output Files
- **Input File**: An Excel file containing raw MTT assay data.
- **Output File**: An Excel file to save the processed results (default format).

## Project Structure
```
C:.
│   LICENSE
│   readme.md
│   requirements.txt
│
├───example_data
│       rawdata.xlsx
│
├───outputs
│       results.xlsx
│       results3.xlsx
│
└───src
        data_loader.py
        plate_analyzer.py
        plate_identifier.py
        plate_processor.py
        results_saver.py
        utils.py
        viabilities_calculator.py
        __init__.py
```

## Modules
### `DataLoader`
Loads raw MTT assay data from the input Excel file.

### `PlateIdentifier`
Identifies and organizes plates within the raw data.

### `PlateProcessor`
Cleans and processes the identified plates to prepare for viability calculations.

### `ViabilitiesCalculator`
Performs viability calculations based on processed plate data.

### `ResultsSaver`
Exports calculated viabilities to an output Excel file.

## Error Handling
Each stage of the pipeline has exception handling to notify users of potential issues, such as:
- File not found errors during data loading.
- Plate identification failures.
- Errors during viability calculations or saving results.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

## License
This project is licensed under the MIT License. See `LICENSE` for more details.

## Contact
For questions or support, please contact:
- **Author**: Panagiotis Tsampanis
- **Email**: panagiotis.tsampanis@ulb.be

---
Thank you for using PlateAnalyzer! If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

