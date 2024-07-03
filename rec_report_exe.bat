@echo off
REM Run the Streamlit app
streamlit run rec_report.py

REM Wait for a few seconds to allow the server to start
timeout /t 10

REM Open the browser to localhost:8501
start http://localhost:8501
