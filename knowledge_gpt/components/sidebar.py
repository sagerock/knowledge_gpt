import streamlit as st

from knowledge_gpt.components.faq import faq
from dotenv import load_dotenv
import os

load_dotenv()


def sidebar():
    with st.sidebar:
       
        api_key_input = st.secrets["API_KEYS"]["OPENAI_API_KEY"]

        st.session_state["OPENAI_API_KEY"] = api_key_input

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "This allows you to ask questions about your "
            "documents and get accurate answers with instant citations. "
        )
        st.markdown("---")

        faq()
