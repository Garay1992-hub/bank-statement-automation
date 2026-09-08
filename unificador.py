import pandas as pd
import glob
import os

def merge_bank_statements(source_folder, output_file):
    print(f"Searching for CSV files in folder: '{source_folder}'...\n")
    
    # 1. Search for all CSV files in the specified folder
    search_path = os.path.join(source_folder, "*.csv")
    csv_files = glob.glob(search_path)
    
    if not csv_files:
        print("No CSV files found in the folder.")
        return

    data_list = []
    
    # 2. Read each found file and append it to our list
    for file in csv_files:
        file_name = os.path.basename(file)
        print(f"Reading: {file_name}")
        
        # Read the CSV file
        df = pd.read_csv(file)
        data_list.append(df)
        
    # 3. Merge all data into a single master dataframe
    complete_data = pd.concat(data_list, ignore_index=True)
    initial_rows = len(complete_data)
    
    # 4. Clean the data: Remove exact duplicates
    clean_data = complete_data.drop_duplicates()
    final_rows = len(clean_data)
    duplicates_removed = initial_rows - final_rows
    
    # 5. Export the result to an Excel file
    clean_data.to_excel(output_file, index=False, engine='openpyxl')
    
    # Operation summary
    print("\n--- Cleaning Summary ---")
    print(f"Total rows processed: {initial_rows}")
    print(f"Duplicates removed: {duplicates_removed}")
    print(f"Final rows in report: {final_rows}")
    print(f"Success! File saved as: {output_file}")

if __name__ == "__main__":
    # Folder configuration 
    folder = "client_data"
    output = "Clean_Accounting_Report.xlsx"
    
    # If the folder doesn't exist, we create it automatically
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"Created folder '{folder}'. Please place some CSV files inside and run again.")
    else:
        merge_bank_statements(folder, output)