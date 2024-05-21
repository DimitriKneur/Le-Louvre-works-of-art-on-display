import streamlit as st
import pandas as pd

st.title("Paintings on Display Database - Le Louvre Museum")

st.text("")

st.text("Le Louvre is known to host some of the finest paintings in the art history.")
st.text("Have a look.")

st.text("")

st.text("If you want to display in full width, click on the top-right corner 'Fullscreen'⬇️")
st.text("button of the table :")

# Charger les données
df = pd.read_csv('data/simplified_le_louvre_works_of_art_on_display_paintings.csv')

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

st.text("Short of inspiration ? Some of the most famous paintings are :")
st.markdown("- La Joconde")
st.markdown("- Les Noces de Cana")
st.markdown("- La Liberté guidant le peuple")
st.markdown("- Le radeau de la Méduse")

st.text("")