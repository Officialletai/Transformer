import json
import os
import requests
from collections import defaultdict


def fetch_definitions(word):
    url = f"https://api.datamuse.com/words?sp={word}&qe=sp&md=d&max=1"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        if data:
            return data[0].get('defs', [])
    return []


def read_words_from_multiple_files(folder_path):
    all_words = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as f:
                all_words.extend([line.strip() for line in f])
    return all_words


def write_definitions_to_file(output_folder_path, word_definitions):
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    for word, definitions in word_definitions.items():
        output_file_path = os.path.join(output_folder_path, f"{word}.txt")
        with open(output_file_path, 'w') as f:
            for definition in definitions:
                f.write(f"{definition}\n")


if __name__ == '__main__':
    folder_path = os.path.join(".", "Wordlist")
    output_folder_path = os.path.join(".", "Wordlist_extracted")

    words = read_words_from_multiple_files(folder_path)
    word_definitions = defaultdict(list)

    for word in words:
        definitions = fetch_definitions(word)
        if definitions:
            word_definitions[word] = definitions
        else:
            print(f"No definitions found for {word}")

    write_definitions_to_file(output_folder_path, word_definitions)