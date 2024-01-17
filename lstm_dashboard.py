# Prototype dashboard for toxicity detection using LexiGuard LSTM
# Still extremely hackish ...

import streamlit as st
import pickle
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

# Load model architecture from JSON file
with open('data/lstm_architect.json', 'r') as file:
    loaded_model_json = file.read()
loaded_model = model_from_json(loaded_model_json)

# Load model weights
loaded_model.load_weights('data/lstm_weights.h5')

# Load tokenizer for preprocessing
with open('data/lstm_tokenizer.pkl', 'rb') as file:
    tokenizer = pickle.load(file)

# Function to predict toxicity
def predict_toxicity(input_text):
    sequence = tokenizer.texts_to_sequences([input_text])
    max_sequence_length = 100 
    padded_sequence = pad_sequences(sequence, maxlen=max_sequence_length)
    toxicity_prediction = loaded_model.predict(padded_sequence)
    toxicity_percentage = round(float(toxicity_prediction) * 100, 2)  # Convert to percentage
    return toxicity_percentage

# Custom HTML/CSS to change background and text color
html_temp = """
    <style>
        body {
            background-color: #00111f;
            color: white;
        }
        .stApp {
            background-color: #00111f;
            color: white;
        }
        .stTextArea > div > textarea {
            color: white !important;
        }
        .stButton button {
            color: #00111f !important;
        }
        .title-wrapper {
            color: white;
        }
        .st-af {
            color: white !important;
            background-color: white !important;
            border-color: white !important;
            border-radius: 5px !important;
            height: 100px !important;
            width: 750px !important;
        }
        .st-ay {
            color: white !important;
            
        }
    </style>
"""
st.markdown(html_temp, unsafe_allow_html=True)

title_col, logo_col = st.columns([12, 1]) 

# Place title in left column
with title_col:
    st.markdown('<h2 class="title-wrapper">LexiGuard Toxicity Detection</h2>',
        unsafe_allow_html=True)

# Place logo in right column
with logo_col:
    st.image('img/lexiguard_logo.png', width=100)


# Input text area
input_text = st.text_area('', key='text_area',
    help='Enter text you want to check for toxicity ...')

# Button
if st.button('Check for toxicity'):
    toxicity = predict_toxicity(input_text)
    st.write(f'Toxicity probability: {toxicity} %')