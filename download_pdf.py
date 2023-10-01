import os
import requests
from urllib.parse import urlsplit

def download_pdfs_from_txt(txt_file_path, output_folder_path):
    # Create output directory if not exists
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)
        
    # Open and read the txt file
    with open(txt_file_path, 'r') as txtfile:
        for line in txtfile:
            url = line.strip()
            if not url:  # Skip empty lines
                continue

            # Extract filename from the URL
            base_url = urlsplit(url)
            filename = os.path.basename(base_url.path)
            
            # Download PDF
            try:
                response = requests.get(url, stream=True)
                response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

                # Write to PDF file
                pdf_path = os.path.join(output_folder_path, filename)
                with open(pdf_path, 'wb') as pdffile:
                    for chunk in response.iter_content(chunk_size=8192):
                        pdffile.write(chunk)

                print(f"Downloaded {filename}")

            except requests.RequestException as e:
                print(f"Failed to download {filename} due to {e}")

txt_file_path = './pdf_urls.txt'  # Path to the text file containing PDF URLs
output_folder_path = './Downloaded_PDFs'  # Folder where you want to save the PDFs

download_pdfs_from_txt(txt_file_path, output_folder_path)
