import requests
import streamlit as st


st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="centered")

st.title("AI Chatbot")
st.caption("Streamlit UI connected to your FastAPI backend")

with st.sidebar:
    st.header("Settings")
    api_base_url = st.text_input("API Base URL", value="http://127.0.0.1:8000")
    request_timeout = st.slider("Request timeout (seconds)", min_value=10, max_value=120, value=45, step=5)
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


user_prompt = st.chat_input("Type your message...")

if user_prompt:
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    with st.chat_message("user"):
        st.markdown(user_prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    f"{api_base_url.rstrip('/')}/user_input",
                    json={"input_text": user_prompt},
                    timeout=request_timeout,
                )
                response.raise_for_status()
                data = response.json()
                assistant_text = data.get("response", "No response received.")
            except requests.exceptions.Timeout:
                assistant_text = "Request timed out. Increase timeout in the sidebar or check backend/model load."
            except requests.exceptions.RequestException as exc:
                assistant_text = f"Backend request failed: {exc}"

            st.markdown(assistant_text)

    st.session_state.messages.append({"role": "assistant", "content": assistant_text})