import projects
import story
import streamlit as st
from gpt import gpt_3
import config as c
import prompt as p


st.set_page_config(
    page_title="Adrian's Job Interview",
    layout="centered")

PAGES = {
    "Story": story,
    "Projects": projects
}

name = st.text_input("Please, write your name")
api_key = st.text_input("OpenAI API Key:", type="password")

col1, col2 = st.columns([4, 1])

if name:
    title = gpt_3(name, c.NAME_TEMP, p.generate_prompt_greetings)
    col1.header(title)

if api_key:
    selection = col2.radio('Go to:', list(PAGES.keys()))
    page = PAGES[selection]
    with st.spinner("Processing..."):
        page.Interface().run()
