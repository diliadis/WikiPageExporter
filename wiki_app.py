import streamlit as st
import wikipediaapi
import os

st.title("Wiki page exporter")

st.write(
    "A simple app that uses the [wikipedia-api](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py) to export a wiki page to a .txt file"
)


page_name = st.text_input("Wikipedia page name", "Belgium")

wiki = wikipediaapi.Wikipedia(
    language="en", extract_format=wikipediaapi.ExtractFormat.WIKI
)

page_wiki = wiki.page(page_name)

if page_wiki.exists():
    st.header("Output:")
    text_to_save = os.linesep.join([s for s in page_wiki.text.splitlines() if s])
    text_to_save = text_to_save.strip().replace("\n", "")
    st.text_area("", value=text_to_save, height=500)

    st.download_button(
        label="Download data as .txt file",
        data=text_to_save,
        file_name="page_name.txt",
        mime="text/csv",
    )
else:
    st.error("The supplied wiki page name does not exist ")