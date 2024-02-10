import streamlit as st
from spello.model import SpellCorrectionModel
import re

# Function to preprocess the text
def preprocess_text(text):
    # Remove tabs
    text = re.sub('\\t', ' ', text)
    # Remove single quotes
    text = re.sub("\\'", "", text)
    # Remove special characters
    text = re.sub(r'[^a-zA-Z]+', ' ', text)
    # Remove leading and trailing spaces
    text = text.strip()
    return text

# Load and preprocess the data
with open("big.txt", "r") as f:
    big = f.readlines()

big_preprocessed = [preprocess_text(text) for text in big if text.strip() != '']

# Train the spell correction model
sp = SpellCorrectionModel(language='en')
sp.train(big_preprocessed)

# Streamlit App
st.title("Spell Correction App")

# User input
user_input = st.text_area("Enter a sentence:")

# Spell correction on button click
if st.button("Correct Spelling"):
    # Preprocess user input
    user_input_preprocessed = preprocess_text(user_input)
    # Spell correction
    corrected_result = sp.spell_correct(user_input_preprocessed)
    # Display corrected text
    st.write(f"Corrected Text: {corrected_result['spell_corrected_text']}")
    # Access correction dictionary if needed
    correction_dict = corrected_result['correction_dict']
    st.write(f"Correction Dictionary: {correction_dict}")

