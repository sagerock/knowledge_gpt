import streamlit as st

from knowledge_gpt.components.faq import faq
from dotenv import load_dotenv
import os

load_dotenv()

api_key_input = st.secrets["API_KEYS"]["OPENAI_API_KEY"]

st.session_state["OPENAI_API_KEY"] = api_key_input

