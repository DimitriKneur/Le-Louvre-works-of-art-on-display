import streamlit as st

from streamlit_extras.switch_page_button import switch_page

def example():
    want_to_contribute = st.button("I want to contribute!")
    if want_to_contribute:
        switch_page("Antiquities")

st.title("Le Louvre Works of Art on Display - Databases")

st.text("Welcome, dear explorer!")
st.text("The objective of this application is to show you an interactive table of the works")
st.text("of art that are currently on display at one of the most prestigious museums")
st.text("worldwide: the famous Le Louvre museum in Paris, France!")

st.text("For performance optimization reasons, the works of art have been separated")
st.text("into two distinct parts :")

st.text("")

# Lien vers la section "Antiquities"
st.link_button("Antiquities", "https://dimitri-kneur-le-louvre-works-of-art-on-display.streamlit.app/Antiquities")
with st.expander("Click here to see what you will find inside"):
    st.markdown("- Greek, Etruscan and Roman Antiquities")
    st.markdown("- Oriental Antiquities")
    st.markdown("- Egyptian Antiquities")

st.text("")

# Lien vers la section "Other Collections"
st.link_button("Other collections", "https://dimitri-kneur-le-louvre-works-of-art-on-display.streamlit.app/Other_Collections")
with st.expander("Click here to see what you will find inside"):
    st.markdown("- Paintings")
    st.markdown("- Medieval, Renaissance and Modern Works of Art")
    st.markdown("- Medieval, Renaissance and Modern Sculpture")
    st.markdown("- Islamic Arts")
    st.markdown("- Louvre History Department")
    st.markdown("- Byzantine and Oriental Christian Arts")
    st.markdown("- Eugène-Delacroix National Museum")

st.text("")

st.text("I wish you a wonderful journey through this treasure trove of artistic masterpieces.")
st.text("Regards,")
st.text("Dimitri Kneur")