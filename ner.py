import streamlit as st
from newspaper import Article
import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")

import subprocess
@st.cache_resource
def download_en_core_web_sm():
    subprocess.run(["python","-m","spacy","download","en_core_web_sm"])
download_en_core_web_sm()   


st.title("Named Entity Recognition")

if st.button("About"):
    st.text("Hello! I am Sourikta from CSDA,DUK. This is an assignment to learn NLP and Streamlit.")

status = st.radio("Select option: ", ('Enter a URL', 'Enter a Paragraph'))

if status == 'Enter a URL':
    url_input = st.text_input("Enter the URL:")
    if st.button("Analyze"):
        article = Article(url_input)
        article.download()
        article.parse()
        doc = nlp(article.text)
        st.markdown(displacy.render(doc, style='ent'), unsafe_allow_html=True)

else:
    paragraph_input = st.text_area("Enter the Paragraph:")
    if st.button("Analyze"):
        doc = nlp(paragraph_input)
        st.markdown(displacy.render(doc, style='ent'), unsafe_allow_html=True)
