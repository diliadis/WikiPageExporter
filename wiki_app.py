import streamlit as st
import wikipediaapi
import nltk
nltk.download('punkt')
import os

st.title("Wiki page exporter")

st.write(
    "A simple app that uses the [wikipedia-api](https://pypi.org/project/Wikipedia-API/) to export a wiki page to a .txt file"
)


page_name = st.text_input("Wikipedia page name", "Belgium")

wiki = wikipediaapi.Wikipedia(
    language="en", extract_format=wikipediaapi.ExtractFormat.WIKI
)

page_wiki = wiki.page(page_name)

if page_wiki.exists():
    st.header("Output:")
    text_to_save = os.linesep.join([s for s in page_wiki.text.splitlines() if s])
    text_to_save = text_to_save.replace("\n", " ")
    tokens = nltk.word_tokenize(text_to_save)
    text_to_save = " ".join(tokens)
    st.text_area("", value=text_to_save, height=500)

    st.download_button(
        label="Download data as .txt file",
        data=text_to_save,
        file_name=page_name+".txt",
        mime="text/csv",
    )
else:
    st.error("The supplied wiki page name does not exist ")
