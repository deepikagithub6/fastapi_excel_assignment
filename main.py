from fastapi import FastAPI
import pandas as pd
import os

app = FastAPI()

#  Excel file ka path
EXCEL_FILE = os.path.join("Data", "capbudg.xlsx")

#  Function to load all sheets
def load_excel_sheets():
    try:
        xl = pd.read_excel(EXCEL_FILE, sheet_name=None)  # None loads all sheets
        return xl
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return {}

#  Default route (just to test)
@app.get("/")
def read_root():
    return {"message": "FastAPI is working!"}

#  Main required endpoint: /list_tables
@app.get("/list_tables")
def list_tables():
    sheets = load_excel_sheets()
    print("Sheets loaded:", sheets)  

    return {"tables": list(sheets.keys())}
@app.get("/get_table/Initial Investment")
def get_table(table_name: str):
    sheets = load_excel_sheets()
    if table_name not in sheets:
        return {"error": "Table not found"}
    df = sheets[table_name]
    # Data ko JSON format me convert karo
    data = df.fillna("").to_dict(orient="records")  # Rows ka list
    return {"table_name": table_name, "data": data}
@app.get("/get_row_count/{table_name}")
def get_row_count(table_name: str):
    sheets = load_excel_sheets()
    if table_name not in sheets:
        return {"error": f"Table '{table_name}' not found."}
    
    df = sheets[table_name]
    return {"table_name": table_name, "row_count": len(df)}

