import streamlit as st
import pandas as pd

st.title("Antiquities on Display Database - Le Louvre Museum")

st.text("Welcome !")

# Charger les données
df = pd.read_csv('data/simplified_le_louvre_works_of_art_on_display_antiquities.csv')

df["snapshot"] = [
    '<a href="{url}">'
    '<img src="{image}" width="50" '
    'alt="Snapshot of {image}"></a>'.format(image=image, url=url)
    for image, url in zip(df["image"], df["url"])
]

df["title"] = [
    '<a href="{url}">{title}</a>'.format(title=title, url=url)
    for title, url in zip(df["title"], df["url"])
]

# Déplacer la colonne 'snapshot' en première position
col = df.pop('snapshot')
df.insert(0, 'snapshot', col)

# Supprimer les colonnes 'image' et 'url'
df = df.drop(['image', 'room', 'url'], axis=1)

st.dataframe(df, use_container_width=True)