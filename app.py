import streamlit as st

st.set_page_config(page_title="Emotion Chat App", page_icon="💬")
st.title("Emotion Chat App")
st.write("Chat with me in English. I will detect your emotion from every message.")

if "messages" not in st.session_state:
    st.session_state.messages = []

def detect_emotion(text):
    text = text.lower()
    if any(word in text for word in ["happy", "great", "awesome", "excited", "wonderful", "joy", "smile", "good", "nice"]):
        return "Happy"
    elif any(word in text for word in ["sad", "cry", "lonely", "depressed", "hurt", "bad", "upset", "tired"]):
        return "Sad"
    elif any(word in text for word in ["angry", "mad", "annoyed", "furious", "hate", "frustrated"]):
        return "Angry"
    elif any(word in text for word in ["scared", "afraid", "fear", "nervous", "worried", "anxious"]):
        return "Fearful"
    elif any(word in text for word in ["surprise", "surprised", "wow", "amazing", "shocked"]):
        return "Surprised"
    elif any(word in text for word in ["love", "like", "beautiful", "cute", "sweet"]):
        return "Love"
    else:
        return "Neutral"

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Type your message here...")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    emotion = detect_emotion(user_input)
    reply = "I detected your emotion: " + emotion + ". Thanks for sharing, tell me more."
    with st.chat_message("assistant"):
        st.write(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
