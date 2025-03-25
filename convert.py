#Convert files to .csv format 

import pandas as pd

def convert_xlsx_to_csv(xlsx_file, csv_file):
    df = pd.read_excel(xlsx_file, engine='openpyxl')  # Read the Excel file
    df.to_csv(csv_file, index=False)  # Save as CSV without the index column
    print(f"Conversion complete: {csv_file}")

# Replace this with your actual file paths
#xlsx_path = ""
#csv_path = ""

convert_xlsx_to_csv(xlsx_path, csv_path)
