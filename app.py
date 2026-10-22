import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Your Personal Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("Your Personal Assistant")

st.subheader("What can your personal assistant do?")

st.markdown("""
1. Answer questions on various topics.
2. Arrange calendar events and meetings.
3. Read, summarize, and reply to emails.
4. Manage tasks and to-do lists.
5. Take quick notes.
6. Track expenses and budgets.
""")

st.subheader("💬 Chat with your assistant")

WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL", "").strip()


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get the user's message
user_message = st.chat_input("Ask me anything...")

if user_message:
    if not WEBHOOK_URL:
        st.error("Webhook URL is not configured.")
        st.stop()

    # Display and save the user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })

    with st.chat_message("user"):
        st.markdown(user_message)

    # Send the message to n8n
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    WEBHOOK_URL,
                    json={"message": user_message},
                    timeout=120
                )

                response.raise_for_status()
                data = response.json()

                # Handle common n8n response formats
                if isinstance(data, list) and data:
                    data = data[0]

                if isinstance(data, dict):
                    ai_response = (
                        data.get("output")
                        or data.get("text")
                        or data.get("response")
                        or data.get("message")
                    )
                else:
                    ai_response = None

                if ai_response is None:
                    ai_response = (
                        "The webhook responded, but I couldn't find "
                        "the AI output. Check the n8n response format."
                    )
                elif not isinstance(ai_response, str):
                    ai_response = str(ai_response)

                st.markdown(ai_response)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": ai_response
                })

            except requests.exceptions.Timeout:
                st.error(
                    "n8n took too long to respond. "
                    "Check your workflow and try again."
                )

            except requests.exceptions.RequestException:
                st.error(
                    "Could not connect to the assistant. "
                    "Please try again later."
                )

            except ValueError:
                st.error(
                    "n8n did not return valid JSON. "
                    "Check the Webhook response settings."
                )
