import streamlit as st
import pandas as pd

st.title("Antiquities on Display Database - Le Louvre Museum")

st.text("Welcome !")

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