import streamlit as st
import pandas as pd

st.title("Antiquities on Display Database - Le Louvre Museum")

st.text("Welcome !")

# Charger les données
df = pd.read_csv('data/simplified_le_louvre_works_of_art_on_display_antiquities.csv')

st.data_editor(
    df,
    column_config={
        "url": st.column_config.LinkColumn(
            "Link", display_text="Link to artwork"
        ),
    },
    hide_index=True,
)



# Afficher les données
st.write("### Le Louvre Works of Art - Antiquities")

st.dataframe(df, use_container_width=True)