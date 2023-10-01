import pdfplumber
import os

def extract_with_pdfplumber(folder_path, output_folder_path):
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)
    
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)
            
            with pdfplumber.open(pdf_path) as pdf:
                text = ''
                for page in pdf.pages:
                    text += page.extract_text()
            
            text_filename = f"{filename[:-4]}.txt"
            text_file_path = os.path.join(output_folder_path, text_filename)
            with open(text_file_path, 'w', encoding='utf-8') as f:
                f.write(text)

folder_path = "./Textbooks"
output_folder_path = "./ExtractedTexts_pdfplumber"

extract_with_pdfplumber(folder_path, output_folder_path)
