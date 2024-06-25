import streamlit as st
import pandas as pd
from io import BytesIO

# Function to process the uploaded file
def process_file(file):
    try:
        xls = pd.ExcelFile(file)
    except ValueError as e:
        st.error("The uploaded file is not a valid Excel file. Please upload a .xlsx file.")
        return None
    except Exception as e:
        st.error(f"An unexpected error occurred while reading the file: {e}")
        return None

    try:
        df = pd.read_excel(xls, sheet_name='Sheet1')
    except ValueError as e:
        st.error("The uploaded Excel file does not contain a sheet named 'Sheet1'. Please check the file and try again.")
        return None
    except Exception as e:
        st.error(f"An unexpected error occurred while reading the sheet: {e}")
        return None

    # Check if necessary columns exist
    required_columns = ['Merchant', 'Floor', 'Reconciliation Date', 'Executed By']
    if not all(column in df.iloc[0].values for column in required_columns):
        st.error(f"Uploaded file is missing one of the required columns: {', '.join(required_columns)}")
        return None

    df.columns = df.iloc[0]
    df = df.drop(0)

    df_cleaned = df[['Merchant', 'Floor', 'Reconciliation Date', 'Executed By']]
    df_cleaned.columns = df_cleaned.columns.str.strip()

    # Ensure proper date parsing with correct format
    try:
        df_cleaned['Reconciliation Date'] = pd.to_datetime(df_cleaned['Reconciliation Date'], dayfirst=True, errors='coerce')
    except Exception as e:
        st.error(f"Error parsing dates: {e}")
        return None

    # Drop rows with invalid dates
    df_cleaned = df_cleaned.dropna(subset=['Reconciliation Date'])

    # Sort and group by 'Merchant' and 'Floor', then get the latest 'Reconciliation Date' for each group
    df_latest = df_cleaned.sort_values('Reconciliation Date').groupby(['Merchant', 'Floor']).tail(1)
    
    # Format the date to dd/mm/yyyy
    df_latest['Reconciliation Date'] = df_latest['Reconciliation Date'].dt.strftime('%d/%m/%Y')

    df_final = df_latest.rename(columns={
        'Merchant': 'MERCHANT',
        'Floor': 'FLOOR',
        'Reconciliation Date': 'DATE',
        'Executed By': 'USER'
    })

    df_final.reset_index(drop=True, inplace=True)
    return df_final

    # Sort the final dataframe by the 'MERCHANT' column alphabetically
    # df_final = df_final.sort_values(by='MERCHANT')

# Streamlit app
st.title('Reconciliation Date Processor')

uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

if uploaded_file is not None:
    processed_data = process_file(uploaded_file)
    
    if processed_data is not None:
        st.write("Processed Data:")
        st.dataframe(processed_data)
        
        buffer = BytesIO()
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            processed_data.to_excel(writer, index=False, sheet_name='Sheet1')
            writer.save()

        st.download_button(
            label="Download Processed Data",
            data=buffer,
            file_name="processed_reconciliation_data.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
