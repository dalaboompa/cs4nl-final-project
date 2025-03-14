import os
import re
import pandas as pd

def merge_excel_files(data_paths_list, output_file, verbose=False):
    """
    Merge multiple Excel files specified in the data_paths_list into a single Excel file such that each 
    Excel file corresponds to one sheet in the output Excel file. In particular, the name of each sheet 
    should be 'part_*' extracted from the name of the input files.
    """
    # Create an ExcelWriter object using a context manager for proper resource handling.
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        for file_path in data_paths_list:
            # Extract the file name from the path.
            file_name = os.path.basename(file_path)
            
            # Use regex to extract the substring matching 'part_[0-9]' from the file name.
            match = re.search(r'(part_[0-9])', file_name)
            if match:
                sheet_name = match.group(1)
            else:
                # If no 'part_*' is found, use the file name without its extension.
                sheet_name = os.path.splitext(file_name)[0]
            
            # Ensure the sheet name is valid:
            # - Truncate to 31 characters (Excel's maximum sheet name length).
            # - Replace illegal characters with an underscore.
            sheet_name = sheet_name[:31]
            for illegal_char in [':', '\\', '/', '?', '*', '[', ']']:
                sheet_name = sheet_name.replace(illegal_char, '_')
            
            # Read the Excel file (default: reading the first sheet) into a DataFrame.
            df = pd.read_excel(file_path)
            if verbose:
                print(f"Adding sheet '{sheet_name}' from file '{file_path}'")
            
            # Write the DataFrame to a new sheet in the merged Excel file.
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    
    if verbose:
        print(f"Merged Excel file saved as '{output_file}'")

# a function that read all sheets from an excel file and return a single dataframe
def sheets_to_dataframe(file_path):
    """
    Read all sheets from an Excel file and return a single DataFrame.
    
    Parameters:
        file_path (str): The path to the Excel file.
        
    Returns:
        pd.DataFrame: A DataFrame containing all data from all sheets.
    """
    # Read all sheets into a dictionary of DataFrames
    all_sheets = pd.read_excel(file_path, sheet_name=None)
    
    # Concatenate all DataFrames into a single DataFrame
    combined_df = pd.concat(all_sheets.values(), ignore_index=True)
    
    return combined_df
