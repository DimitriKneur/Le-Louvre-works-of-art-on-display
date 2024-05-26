import streamlit as st
import pandas as pd

st.set_page_config(page_title="🖼 Le Louvre Artworks", 
                   page_icon=":rocket:", 
                   layout="wide")

st.title("Antiquities on Display Database - Le Louvre Museum")

st.text("")

st.write("You will find here the table showing the artworks of the following categories :")

st.markdown("- Greek, Etruscan and Roman Antiquities")
st.markdown("- Oriental Antiquities")
st.markdown("- Egyptian Antiquities")

st.text("")

st.write("If you want to display in full width, click on the top-right corner 'Fullscreen' ⛶ button of the table :")

# Charger les données
df = pd.read_csv('data/simplified_le_louvre_works_of_art_on_display_antiquities.csv')

df = df[["image", "title", "creatorName", "startYear", "endYear", "collection", "url",]]

st.data_editor(
    df,
    column_config={
        "url": st.column_config.LinkColumn(
            "Link", display_text="Link to artwork"
        ),
        "image": st.column_config.ImageColumn(
            "Preview Image"
        )
    },
    hide_index=True,
)

st.text("")

st.write("Short of inspiration ? Some of the most famous artworks of these categories are :")
st.markdown("- Victoire de Samothrace")
st.markdown("- Vénus de Milo")
st.markdown("- Sarcophage des époux")
st.markdown("- Le scribe accroupi")
st.markdown("- Sphinx de Tanis")