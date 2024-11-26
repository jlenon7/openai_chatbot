import streamlit as st
from openai import OpenAI

def create_gpt():
  gpt = OpenAI(api_key=st.secrets['OPENAI_API_KEY'])

  return gpt
