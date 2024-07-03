# Reconciliation Date Processor

This Streamlit application allows users to upload an Excel file containing reconciliation data, process the data to clean and format it, and download the cleaned data as a new Excel file.

## Features

- **Upload Excel File**: Upload an Excel file with reconciliation data.
- **Process Data**: Clean and format the data, including date parsing.
- **Display Data**: View the cleaned data in the app.
- **Download Data**: Download the processed data as a new Excel file.

## Installation

To install and run the application, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/mkmagaya/rec_report.git
    cd rec_report
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    You can either run the application manually or use the provided batch script to automate the initiation process.

### Manual Run

    ```bash
    streamlit run rec_report.py
    ```

### Automated Run

    Use the `rec_report_exe.bat` script to automate the initiation service. The script will start the Streamlit app and open it in your default web browser.

#### Batch Script: `rec_report_exe.bat`

    ```batch
    @echo off
    REM Run the Streamlit app
    streamlit run rec_report.py

    REM Wait for a few seconds to allow the server to start
    timeout /t 10

    REM Open the browser to localhost:8501
    start http://localhost:8501
    ```

    To run the batch script, simply double-click on the `rec_report_exe.bat` file or run it from the command line:

    ```cmd
    rec_report_exe.bat
    ```

## Usage

1. Open the application in your browser.
2. Upload an Excel file with the required format.
3. View the cleaned data in the app.
4. Download the processed data as a new Excel file.

## File Format

The uploaded Excel file should have the following format:

- A sheet named "Sheet1".
- Columns: `Merchant`, `Floor`, `Reconciliation Date`, `Executed By`.

## Example

To see an example of the file format, you can refer to the `sample.xlsx` file provided in the repository.

## Troubleshooting

If you encounter any issues while using the application, check the error messages displayed in the app for guidance. Common issues include:

- Uploading a file that is not a valid Excel file.
- Missing required columns in the uploaded file.
- Errors in date parsing due to incorrect date formats.

For further assistance, please contact [makomagaya05@gmail.com].
