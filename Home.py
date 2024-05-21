import streamlit as st

st.title("Le Louvre Works of Art on Display - Databases")

st.text("")

st.text("Welcome, dear explorer!")

st.text("")
st.text("The objective of this application is to show you an interactive table of the works")
st.text("of art that are currently on display at one of the most prestigious museums")
st.text("worldwide: the famous Le Louvre museum in Paris, France!")

st.text("")

st.text("Navigate now through all the artworks by clicking the link below : ")

# Lien vers la section "All_Artworks"
st.page_link("pages/All_Artworks.py", label="All Artworks", icon="💯")

st.text("")

st.text("Maybe you prefer explore only certain categories ?")
st.text("Here are the most famous ones : ")

st.text("")

# Lien vers la section "Antiquities"
st.page_link("pages/Antiquities.py", label="Antiquities", icon="🏺")
with st.expander("Click here to see what you will find inside"):
    st.markdown("- Greek, Etruscan and Roman Antiquities")
    st.markdown("- Oriental Antiquities")
    st.markdown("- Egyptian Antiquities")

st.text("")

# Lien vers la section "Middle Ages, Renaissance and Modern Times"
st.page_link("pages/MA_Ren_ModTimes.py", label="Middle Ages, Renaissance, Modern Times Art Objects & Sculptures", icon="⚒️")
with st.expander("Click here to see what you will find inside"):
    st.markdown("- Middle Ages, Renaissance & Modern Times Art Objects")
    st.markdown("- Middle Ages, Renaissance & Modern Times Scupltures")

st.text("")

# Lien vers la section "Paintings"
st.page_link("pages/Paintings.py", label="Paintings", icon="🎨")
st.text("Le Louvre is known to host some of the finest paintings in the art history.")
st.text("Have a look.")

st.text("")

st.text("I wish you a wonderful journey through this treasure trove of artistic masterpieces.")
st.text("Regards,")
st.text("Dimitri Kneur")