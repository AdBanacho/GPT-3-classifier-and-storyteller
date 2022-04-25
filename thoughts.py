import streamlit as st

tho1 = """I like working in a methodology that looks like design thinking. Firstly I think who is a customer. What do they like, and what is important for them?
        Customer: Possibly my future employer, Founder AI company 
        
        Then I started thinking about what tools I had. What they can make, where are the borders of them, how can I connect them.
        Streamlit: text inputs
        GPT-3: AI for transforming text inputs
        
        After that, I connected the dots and I created an app to show you that:
        I understand the GPT-3, 
        I can create a custom classifier with GPT-3
        I'm able to connect tools/apps/frameworks to work together
        I can implement an app that is able to write a story and present it with images
        """

tho2 = """I had real fun with GPT-3, this is amazing how it understands the text. One part of my app is creating greeting with GPT-3. The input is a name, I prepared my training data to create a greeting as an "Adrian's Portfoilio". I feel so good when I saw "oh, hay Adrian! Welcome to your portfolio" when I wrote my name as an input. 
        
        This is the future of AI. In a few lines of text, everybody at my streamlit app can create a classifier. This is mindblowing that you don't have to know how the AI works, how to code, or how to prepare data. The only thing that is needed is a text."""


class Interface:
    def __init__(self, GPT):
        self.gpt = GPT

    def run(self):
        st.header("How was your path of thoughts behind creating the application")
        for line in tho1.splitlines():
            st.write(line)

        st.header("What are your views on GPT-3, Codex and other modern AI technologies")
        for line in tho2.splitlines():
            st.write(line)