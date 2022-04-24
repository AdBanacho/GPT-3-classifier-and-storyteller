import streamlit as st
import config as c

key = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


class Interface:
    def __init__(self, GPT):
        self.gpt = GPT

    def run(self):
        st.sidebar.header("**Realised projects:**")
        for no, line in enumerate(c.PROJECTS):
            if no%2 != 0 and st.sidebar.checkbox("Show description", key=key[no]):
                for l in line.splitlines():
                    st.sidebar.write(l)
            elif no%2 == 0:
                st.sidebar.write(line)
        rp = 6
        st.header("Some metrics about me")
        col1, col2, col3 = st.columns(3)
        col1.metric("Years old", "25 yo", "1.0 per year")
        col2.metric("Willingness to learn", "100%", "0%")
        col3.metric("Realised projects", str(rp), f"+{rp - 6} classifiers")

        st.header("Create your own classifier")
        size = st.number_input("Count of examples", value=3)
        examples = []
        labels = []
        for i in range(size):
            example = [st.text_input("Example:", key=i, placeholder="eg. A happy moment")]
            label = st.text_input("Label:", key=-i, placeholder="eg. Positive")
            labels.append(label)
            example.append(label)
            examples.append(example)

        st.header("Time to test it")
        query = st.text_input("Text to test")
        if st.button("Run") and query != "":
            with st.spinner("Processing..."):
                st.write(self.gpt.gpt_3_classification(query, labels, examples))
            st.success('Done')
            rp += 1
            col1, col2, col3 = st.columns(3)
            col1.metric("Years old", "25 yo", "1.0 per year")
            col2.metric("Willingness to learn", "100%", "0%")
            col3.metric("Realised projects", str(rp), f"+{rp-6} classifiers")

