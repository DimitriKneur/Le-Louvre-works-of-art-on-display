import streamlit as st
import pandas as pd

st.set_page_config(page_title="🖼 Le Louvre Artworks", 
                   page_icon=":rocket:", 
                   layout="wide")

st.title("Middle Ages, Renaissance, Modern Times Art Objects and Sculptures on Display Database - Le Louvre Museum")

st.text("")

st.write("You will find here the table showing the artworks of the following categories :")

st.markdown("- Middle Ages, Renaissance & Modern Times Art Objects")
st.markdown("- Middle Ages, Renaissance & Modern Times Scupltures")

st.text("")

st.write("If you want to display in full width, click on the top-right corner 'Fullscreen' ⛶ button of the table :")

# Charger les données
df = pd.read_csv('data/simplified_le_louvre_works_of_art_on_display_middle_ages_renaissance_modern_times_sculptures_objects.csv')

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