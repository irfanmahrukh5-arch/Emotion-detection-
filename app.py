import streamlit as st

st.set_page_config(page_title="Emotion Detection", page_icon="😊")
st.title("😊 Emotion Detection App")
st.write("Apna jumla likho, app batayega emotion kya hai.")

text = st.text_area("Yahan likho:", "I am very happy today!")

def detect_emotion(text):
    text = text.lower()
    if any(w in text for w in ["happy", "great", "love", "khush", "awesome", "good"]):
        return "Happy 😊", "Tum khush lag rahi ho!"
    elif any(w in text for w in ["sad", "cry", "alone", "udas", "tired"]):
        return "Sad 😢", "Udas lag rahi ho, sab theek ho jayega."
    elif any(w in text for w in ["angry", "mad", "gussa", "hate"]):
        return "Angry 😡", "Thora gussa aa raha hai."
    elif any(w in text for w in ["scared", "fear", "dar"]):
        return "Scared 😨", "Dar lag raha hai?"
    elif any(w in text for w in ["surprise", "wow", "hairan"]):
        return "Surprised 😮", "Hairani wali baat hai!"
    else:
        return "Neutral 😐", "Normal emotion hai."

if st.button("Detect Emotion"):
    emotion, msg = detect_emotion(text)
    st.success(f"Emotion: {emotion}")
    st.write(msg)
