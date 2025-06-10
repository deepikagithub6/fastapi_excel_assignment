# FastAPI Excel Data API

## Project Overview
This project is a FastAPI application designed to read data from an Excel workbook containing multiple sheets and expose the data through RESTful API endpoints. It enables users to retrieve the list of available sheets as well as the content of any specified sheet in JSON format.

## Features
- Reads all sheets from an Excel file.
- Lists all available sheets via API.
- Provides data from a specific sheet on demand.
- Handles Excel file reading errors gracefully.

## Prerequisites
- Python 3.8 or higher installed on your system.
- Excel file (`capbudg.xlsx`) placed inside the `Data` directory of the project.

## Setup Instructions

1. **Create a virtual environment:**

   ```bash
   python -m venv venv
# Activate the virtual environment:
   **On Windows PowerShell:**
      .\venv\Scripts\Activate.ps1
  **On Windows Command Prompt:**
      .\venv\Scripts\activate
# Install dependencies:
pip install fastapi uvicorn pandas openpyxl
# Ensure the Excel file is present:
Place your Excel file capbudg.xlsx inside the Data folder relative to the project root.
# Running the Application
Run the FastAPI application using Uvicorn:
uvicorn main:app --host 127.0.0.1 --port 9090 --reload
**The API will be accessible at http://127.0.0.1:9090/.**
**The interactive API documentation is available at http://127.0.0.1:9090/docs.**
# API Endpoints
GET /list_tables
Returns a JSON list of all sheet names in the Excel workbook.
GET http://127.0.0.1:9090/list_tables
{
  "tables": ["Initial Investment", "Operating Cashflows", "Working Capital", ...]
}
# Get data from a specific sheet
GET /get_table/{table_name}
Replace {table_name} with the exact name of the Excel sheet you want to fetch.

# Example
GET http://127.0.0.1:9090/get_table/Initial%20Investment
# Response
{
  "data": [
    { "Column1": "Value1", "Column2": "Value2", ... },
    ...
  ]
}
# Notes 
**The Excel file path can be modified in main.py by changing the EXCEL_FILE variable.**

**The current implementation returns the entire sheet data as JSON without pagination or filtering.**

**Ensure the Excel sheet names are URL-encoded when calling the API.**

# Postman collection
# How to Use:

**Open Postman**

**Click Import → Raw Text**

**Paste the contents of postman_collection.json**

**Click Import**

**Use the pre-configured endpoints to test**

# Each request in the collection corresponds to a specific table from the Excel file, like:

Initial Investment

Operating Cashflows

Salvage Value

Discounted CF

Investment Measures

Book Value & Depreciation

## Postman Collection

Use this file to test API endpoints in Postman:

 [Download Collection](./fastapi_excel.postman_collection.json)

### Steps:
1. Open Postman → Import
2. Select the `.json` file
3. Run the saved requests

# Notes

**Make sure your Excel file is named capbudg.xlsx and located inside the /Data directory.**

**Ensure column names in each sheet are structured as headers for correct JSON parsing.**







