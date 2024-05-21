import streamlit as st
import pandas as pd

st.title("Other Collections on Display Database - Le Louvre Museum")

st.text("")

st.text("You will find here the table showing the artworks of the following categories :")
st.markdown("- Paintings")
st.markdown("- Medieval, Renaissance and Modern Works of Art")
st.markdown("- Medieval, Renaissance and Modern Sculpture")
st.markdown("- Islamic Arts")
st.markdown("- Louvre History Department")
st.markdown("- Byzantine and Oriental Christian Arts")
st.markdown("- Eugène-Delacroix National Museum")

st.text("")

st.text("If you want to display in full width, click on the top-right corner 'Fullscreen'⬇️")
st.text("button of the table :")

# Charger les données
df = pd.read_csv('data/simplified_le_louvre_works_of_art_on_display_other_collections.csv')

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

st.text("")

st.text("Short of inspiration ? Some of the most famous artworks of these categories are :")
st.markdown("- ")

st.text("")