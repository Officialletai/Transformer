import os
import tabula

def extract_tables_with_tabula(folder_path, output_folder_path):
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)
            dfs = tabula.read_pdf(pdf_path, multiple_tables=True, pages='all')
            
            # Save each table to a separate CSV file
            for i, df in enumerate(dfs):
                csv_filename = f"{filename[:-4]}_table_{i+1}.csv"
                csv_file_path = os.path.join(output_folder_path, csv_filename)
                df.to_csv(csv_file_path, index=False)

folder_path = "./Textbooks"
output_folder_path = "./ExtractedTables_tabula"

extract_tables_with_tabula(folder_path, output_folder_path)
