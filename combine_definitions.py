import os


def combine_definitions_to_academic_dictionary(output_folder_path, academic_dictionary_file):
    with open(academic_dictionary_file, 'w') as output_file:
        for filename in os.listdir(output_folder_path):
            if filename.endswith('.txt'):
                word = filename[:-4]  # Remove '.txt' to get the word
                file_path = os.path.join(output_folder_path, filename)

                with open(file_path, 'r') as f:
                    definitions = f.readlines()
                    # Join definitions and remove trailing newline characters
                    definition_text = ' '.join([definition.strip() for definition in definitions])
                    output_file.write(f"{word} : {definition_text}\n")


if __name__ == '__main__':
    output_folder_path = os.path.join(".", "Wordlist_extracted")
    academic_dictionary_file = os.path.join(".", "academic_dictionary.txt")

    combine_definitions_to_academic_dictionary(output_folder_path, academic_dictionary_file)
