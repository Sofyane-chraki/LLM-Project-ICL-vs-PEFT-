import os
import pandas as pd
import tabula

# Function to extract tables from a PDF file
def extract_tables_from_pdf(pdf_path):
    tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True, encoding="latin1")
    return tables

# Path to the folder containing PDF files
folder_path = "D:\\Documents\\Ecole\\Matieres\\Riga project"

# Initialize an empty list to store all DataFrames
all_dfs = []

# Iterate over all PDF files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        # Construct the full path to the PDF file
        pdf_path = os.path.join(folder_path, filename)
        
        # Extract tables from the PDF file
        try:
            tables = extract_tables_from_pdf(pdf_path)
            
            # Concatenate all tables into a single DataFrame
            df = pd.concat(tables)
            
            # Add the DataFrame to the list
            all_dfs.append(df)
            
            print(f"PDF file '{filename}' processed successfully")
        except Exception as e:
            print(f"Error processing PDF file '{filename}': {e}")

# Concatenate all DataFrames into one
combined_df = pd.concat(all_dfs, ignore_index=True)

# Save the combined DataFrame to a CSV file
combined_csv_path = os.path.join(folder_path, "combined_data.csv")
combined_df.to_csv(combined_csv_path, index=False)

print(f"All PDF files processed. Combined data saved to '{combined_csv_path}'")
