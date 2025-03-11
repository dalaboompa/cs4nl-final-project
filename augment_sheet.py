import os
import pandas as pd

def merge_excel_files(data_dir, output_file, verbose=False):
    """
    Merge multiple Excel files into one, with each file as a separate sheet.
    
    Parameters:
        data_dir (str): The directory containing the input .xlsx files.
        output_file (str): The name of the output .xlsx file (including .xlsx extension).
    """
    # Get all matching files
    file_list = [f for f in os.listdir(data_dir) if f.startswith("mcmaster_reddit_part_") and f.endswith(".xlsx")]
    
    if not file_list:
        print("No matching Excel files found in the directory.")
        return

    # Sort files to maintain order
    file_list.sort()

    # Create a writer object
    output_path = os.path.join(data_dir, output_file)
    with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:
        for file in file_list:
            file_path = os.path.join(data_dir, file)
            sheet_name = file.replace("mcmaster_reddit_", "").replace(".xlsx", "")
            
            try:
                df = pd.read_excel(file_path)
                df.to_excel(writer, sheet_name=sheet_name, index=False)
                if verbose:
                    print(f"Added {file} as sheet: {sheet_name}")
            except Exception as e:
                print(f"Error reading {file}: {e}")
    if verbose:
        print(f"Successfully created {output_file} with {len(file_list)} sheets.")

# Example usage
# merge_excel_files("/path/to/data", "merged_output.xlsx")
