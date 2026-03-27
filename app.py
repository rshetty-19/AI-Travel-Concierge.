import streamlit as st
from langchain.llms import OpenAI

st.title("AI Travel Assistant ✈️")

api_key = st.text_input("Enter your OpenAI API Key", type="password")

if api_key:
    llm = OpenAI(openai_api_key=api_key)

    user_input = st.text_input("Ask me about travel...")

    if user_input:
        response = llm(user_input)
        st.write(response)
