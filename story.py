import streamlit as st
import config as c
import prompt as p
from image import download


class Interface:
    def __init__(self, GPT):
        self.topic = ""
        self.projects = True
        self.gpt = GPT
        self.story = self.gpt.gpt_3(self.topic, c.STORY_TEMP, p.generate_prompt_story)
        self.images = ""
        self.words = self.gpt.gpt_3("", c.SONG_TEMP, p.generate_prompt_music)

    def run(self):

        if self.projects:
            st.markdown("Do you want to hear a story about Adrian's job interview?")
            self.topic = st.select_slider("", ["Horror", "Boring", "Sad", "Funny", "Exciting"], "Funny")
            st.write(self.story)
            topics = self.gpt.gpt_3(self.story, c.TOPIC_TEMP, p.generate_prompt_main_words)
            self.images = [topic for topic in topics.split(',')]
            st.markdown("_Interpretation by images_")
            for no_col, col in enumerate(st.columns(len(self.images) if len(self.images) < 3 else 3)):
                col.image(download(self.images[no_col]))

        st.sidebar.write("Do you want a music?")
        if st.sidebar.button("Youtube"):
            st.sidebar.video(c.VIDEO)
        if st.sidebar.button("Create by you own"):
            st.sidebar.write("Words for you")
            for line in self.words.splitlines():
                st.sidebar.write(line)

