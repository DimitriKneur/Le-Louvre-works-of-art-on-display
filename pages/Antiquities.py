import streamlit as st
import pandas as pd

st.title("Antiquities on Display Database - Le Louvre Museum")

st.text("Welcome !")

df = pd.read_csv('data/simplified_le_louvre_works_of_art_on_display_antiquities.csv')

st.dataframe(df, use_container_width=True)