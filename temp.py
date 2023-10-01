# from spellchecker import SpellChecker
# import re

# def correct_text(text):
#     # Replace newline characters with spaces
#     text = text.replace('\n', ' ')
    
#     # Remove excessive spaces
#     text = re.sub(' +', ' ', text)
    
#     # Initialize spell checker
#     spell = SpellChecker()
    
#     # Correct misspelled words
#     misspelled = spell.unknown(text.split())
#     for word in misspelled:
#         # Get the one most likely answer
#         corrected_word = spell.correction(word)
#         text = text.replace(word, corrected_word)

#     return text

# # Sample text (as a stand-in for one of your PDF extracts)
# sample_text = """Tofind theprime factorization ofacomposite number, find any two factors ofthenumber and use them tocreate two
# branches. Ifafactor isprime, that branch iscomplete. Circlethat prime. Otherwise itiseasy tolose trackoftheprime
# numbers."""

# # Correct the text
# corrected_text = correct_text(sample_text)
# print(corrected_text)

import re

def initial_cleaning(text):
    # Remove excessive spaces
    text = re.sub(' +', ' ', text)
    # Fix broken apart words (e.g., "e xpression" -> "expression")
    text = re.sub(r'(?<=\w) (?=\w)', '', text)
    return text

text = """Tosimplify an e xpression , do all oper ations in the e xpression."""
cleaned_text = initial_cleaning(text)
print("Initial Cleaning:", cleaned_text)

import nltk
from nltk.corpus import words

# Download the word list
nltk.download('words')

# Create a set for faster lookup
word_list = set(words.words())

def segment_words(text):
    text = text.lower()
    n = len(text)
    dp = [False] * (n + 1)
    dp[0] = True
    actual_words = []
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and text[j:i] in word_list:
                dp[i] = True
                actual_words.append(text[j:i])
                
    return ' '.join(actual_words)

segmented_text = segment_words(cleaned_text)
print("Segmented Text:", segmented_text)

from keras.models import Model
from keras.layers import Input, Dense, LSTM

input_shape = (100,)  # Assuming 100 characters in sequence
input_layer = Input(shape=input_shape)

# Encoder
encoded = LSTM(64)(input_layer)

# Decoder
decoded = Dense(100, activation='softmax')(encoded)

# Autoencoder
autoencoder = Model(input_layer, decoded)

# Compile the model
autoencoder.compile(optimizer='adam', loss='categorical_crossentropy')

# Assume x_train and x_test are your training and test data
# autoencoder.fit(x_train, x_train, epochs=50, batch_size=256, validation_data=(x_test, x_test))
