import streamlit as st
from transformers import pipeline
import time

# Page setup
st.set_page_config(page_title="English to French Translator", page_icon="🇫🇷")
st.title("🌍 English → French Translator with Typing Effect")

# Load model
@st.cache_resource
def load_model():
    return pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr")

translator = load_model()

# Typing effect function
def typing_effect(text, delay=0.05):
    placeholder = st.empty()
    typed = ""
    for char in text:
        typed += char
        placeholder.markdown(f"**{typed}**")
        time.sleep(delay)

# Input from user
user_input = st.text_input("Enter text in English:", "")

if st.button("Translate"):
    if user_input.strip():
        with st.spinner("Translating..."):
            translation = translator(user_input)[0]['translation_text']
        st.subheader("French Translation:")
        typing_effect(translation)
    else:
        st.warning("Please enter some text to translate.")
