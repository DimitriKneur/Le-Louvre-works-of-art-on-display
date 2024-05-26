import streamlit as st
import pandas as pd

st.set_page_config(page_title="🖼 Le Louvre Artworks", 
                   page_icon=":rocket:", 
                   layout="wide")

st.title("All Artworks on Display - Le Louvre Museum")

st.text("")

st.write("Here is the table of every Le Louvre Museum artwork that is currently on display.")

st.text("")

st.write("If you want to display in full width, click on the top-right corner 'Fullscreen' ⛶ button of the table :")

# Charger les données
df = pd.read_csv('data/simplified_le_louvre_works_of_art_on_display_all_dpts.csv')

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
