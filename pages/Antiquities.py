import streamlit as st
import pandas as pd

st.title("Antiquities on Display Database - Le Louvre Museum")

st.text("You will find in this page the table showing the artworks of the following categories :")

st.markdown("- Greek, Etruscan and Roman Antiquities")
st.markdown("- Oriental Antiquities")
st.markdown("- Egyptian Antiquities")

st.text("Short of inspiration ? Here are some of the most famous artworks of these categories :")
st.markdown("- Victoire de Samothrace")
st.markdown("- Vénus de Milo")
st.markdown("- Sarcophage des époux")
st.markdown("- Le scribe accroupi")
st.markdown("- Sphinx de Tanis")

st.text("If you want to display in full width, click on the top-right corner")
st.text("'Fullscreen' button of the table :")

# Charger les données
df = pd.read_csv('data/simplified_le_louvre_works_of_art_on_display_antiquities.csv')

df = df[["image", "title", "collection", "creatorName", "url",]]

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