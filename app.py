import streamlit as st
from agent.agent_controller import handle_user_input

st.set_page_config(page_title="Agentic Enterprise Assistant")

st.title("Agentic Enterprise Assistant")

user_input = st.text_input("Ask a question or give a command:")

if st.button("Submit") and user_input:
    with st.spinner("Processing..."):
        response = handle_user_input(user_input)

    # Simple detection: JSON responses start with "{"
    if response.strip().startswith("{"):
        st.subheader("Action Output (JSON)")
        st.code(response, language="json")
    else:
        st.subheader("Answer")
        st.write(response)
