import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Emotion Detection", page_icon="😊")

st.title("Emotion Detection App")
st.write("Enter a sentence and I will detect the emotion.")

text = st.text_input("Enter your sentence here:")

if st.button("Detect Emotion"):
    if text == "":
        st.warning("Please enter some text first!")
    else:
        text_lower = text.lower()

        if "happy" in text_lower or "great" in text_lower or "good" in text_lower or "excited" in text_lower:
            st.success("Emotion: Happy 😊")
        elif "sad" in text_lower or "cry" in text_lower or "bad" in text_lower or "lonely" in text_lower:
            st.info("Emotion: Sad 😢")
        elif "angry" in text_lower or "mad" in text_lower or "annoyed" in text_lower:
            st.error("Emotion: Angry 😡")
        elif "love" in text_lower or "like" in text_lower or "beautiful" in text_lower:
            st.success("Emotion: Love ❤️")
        elif "fear" in text_lower or "scared" in text_lower or "afraid" in text_lower:
            st.warning("Emotion: Fear 😨")
        else:
            st.warning("Emotion: Neutral 😐")
