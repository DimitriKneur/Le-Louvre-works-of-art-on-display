import streamlit as st
import pandas as pd

st.title("Antiquities on Display Database - Le Louvre Museum")

st.text("Welcome !")

# Charger les données
df = pd.read_csv('data/simplified_le_louvre_works_of_art_on_display_antiquities.csv')

# Créer une colonne 'title_with_link' avec les liens cliquables
df["title_with_link"] = [
    f'<a href="{url}">{title}</a>' for title, url in zip(df["title"], df["url"])
]

# Afficher les données avec les liens cliquables
st.write("### Le Louvre Works of Art - Antiquities")
for index, row in df.iterrows():
    st.markdown(f'{row["title_with_link"]}', unsafe_allow_html=True)

# Alternative using data_editor with only titles displayed
# But it doesn't support hyperlink columns directly as of now
# st.data_editor(
#     df[['title', 'snapshot']],  # Display only the title and snapshot columns
#     column_config={
#         "title": st.column_config.LinkColumn(
#             "Artwork Title",
#             help="Name of the artwork",
#             validate="^https://[a-z]+\.streamlit\.app$",
#             max_chars=100,
#             display_text="https://(.*?)\.streamlit\.app"
#         ),
#     },
#     hide_index=True,
# )

st.dataframe(df, use_container_width=True)