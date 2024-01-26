from dotenv import load_dotenv

load_dotenv()  

import streamlit as st
import os
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

os.getenv("API_KEY")
genai.configure(api_key=os.getenv("API_KEY"))

def gemini(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

# initialize our streamlit app

st.set_page_config(page_title="LLM")

st.header("LLM Application")

input=st.text_input("Input: ",key="input")


submit=st.button("Click Here")

## If ask button is clicked

if submit:
    
    response=gemini(input)
    st.subheader("Response")
    st.write(response)
