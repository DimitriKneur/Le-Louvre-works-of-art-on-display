import streamlit as st

st.set_page_config(page_title="🖼 Le Louvre Artworks", 
                   page_icon=":rocket:")

st.title("Le Louvre Artworks on Display")

st.text("")

st.write("Welcome, dear explorer!")

st.write("")
st.write("The objective of this application is to show you an interactive table of artworks that are currently on display at one of the most prestigious museums worldwide: the famous Le Louvre museum in Paris, France!")
st.text("")

st.write("Navigate now through all the artworks by clicking the link below : ")

# Lien vers la section "All_Artworks"
st.page_link("pages/All_Artworks.py", label="All Artworks", icon="💯")

st.write("")
st.write("I wish you a wonderful journey through this treasure trove of artistic masterpieces.")
st.write("")
st.write("Regards,")
st.write("Dimitri Kneur")