import streamlit as st

st.title("Le Louvre Works of Art on Display - Databases")

st.text("Welcome, dear explorer!")
st.text("The objective of this application is to show you an interactive table of the works")
st.text("of art that are currently on display at one of the most prestigious museums")
st.text("worldwide: the famous Le Louvre museum in Paris, France!")

st.text("For performance optimization reasons, the works of art have been separated")
st.text("into two distinct parts :")

st.text("")

# Lien vers la section "Antiquities"
st.page_link("pages/Antiquities.py", label="Antiquities", icon="1️⃣")
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