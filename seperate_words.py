def split_words_into_lines(input_file_path, output_file_path):
    try:
        # Step 1: Read the Text File
        with open(input_file_path, 'r', encoding='utf-8') as infile:
            content = infile.read()
        
        # Step 2: Split the Words
        words = content.split()
        
        # Step 3: Write Words to a New File
        with open(output_file_path, 'w', encoding='utf-8') as outfile:
            for word in words:
                outfile.write(f"{word}\n")
                
        print(f"Successfully separated words into lines and saved in {output_file_path}.")
        
    except FileNotFoundError:
        print(f"File {input_file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
input_file_path = "AWL_WF_By_Headword.txt"
output_file_path = "output.txt"
split_words_into_lines(input_file_path, output_file_path)
