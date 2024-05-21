import streamlit as st
import pandas as pd

st.title("Antiquities on Display Database - Le Louvre Museum")

st.text("Welcome !")

# Charger les données
df = pd.read_csv('data/simplified_le_louvre_works_of_art_on_display_antiquities.csv')

# Ajouter une colonne de liens cliquables à la colonne "title"
df["title"] = [
    f'<a href="{url}">{title}</a>' for title, url in zip(df["title"], df["url"])
]

# Fonction pour afficher le DataFrame avec les liens cliquables
def render_dataframe_with_links(dataframe):
    for index, row in dataframe.iterrows():
        # Concaténer les colonnes avec un formatage HTML
        row_html = "".join([f"<td>{row[col]}</td>" if col != "title" else f"<td>{row['title']}</td>" for col in dataframe.columns])
        st.markdown(f"<tr>{row_html}</tr>", unsafe_allow_html=True)

# Afficher les données
st.write("### Le Louvre Works of Art - Antiquities")

st.dataframe(df, use_container_width=True)