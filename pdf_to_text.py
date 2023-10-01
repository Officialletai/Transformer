import os
import PyPDF2

def extract_text_from_all_pdfs_in_folder(folder_path, output_folder_path):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)
        
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)
            with open(pdf_path, 'rb') as f:
                reader = PyPDF2.PdfFileReader(f)
                text = ''
                for i in range(reader.getNumPages()):
                    page = reader.getPage(i)
                    text += page.extractText()
            
            # Save to a new text file in the output folder
            text_filename = f"{filename[:-4]}.txt"  # Remove '.pdf' and append '.txt'
            text_file_path = os.path.join(output_folder_path, text_filename)
            with open(text_file_path, 'w', encoding='utf-8') as f:
                f.write(text)

# Define the folder_path and output_folder_path relative to the script's location
folder_path = os.path.join(".", "Textbooks")
output_folder_path = os.path.join(".", "ExtractedTexts")

# Extract text from all PDFs in the folder and save to new text files
extract_text_from_all_pdfs_in_folder(folder_path, output_folder_path)
