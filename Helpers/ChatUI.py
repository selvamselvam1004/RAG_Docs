import streamlit as st
from base_line import retrieve_text


def renderChatUI(index, text, model):
    # Initialize chat history if it doesn't exist
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        if message['role'] == 'user':
            with st.chat_message("user"):
                st.markdown(f"**You:** {message['content']}")
        else:
            with st.chat_message("assistant"):
                st.markdown(f"**Assistant:** {message['content']}")

    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Add user message to chat history and display it
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get assistant's response and display it
        response = retrieve_text(prompt, index, text, model)  # Assuming this function returns a string
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        with st.chat_message("assistant"):
            st.markdown(response)

    # Clear chat option
    if st.button("Clear Chat"):
        st.session_state.messages = []
