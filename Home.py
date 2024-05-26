import streamlit as st

st.set_page_config(page_title="🖼 Le Louvre Artworks", 
                   page_icon=":rocket:", 
                   layout="wide")

st.title("Le Louvre Works of Art on Display - Databases")

st.text("")

st.write("Welcome, dear explorer!")

st.write("")
st.write("The objective of this application is to show you an interactive table of the works of art that are currently on display at one of the most prestigious museums worldwide: the famous Le Louvre museum in Paris, France!")
st.text("")

st.write("Navigate now through all the artworks by clicking the link below : ")

# Lien vers la section "All_Artworks"
st.page_link("pages/All_Artworks.py", label="All Artworks", icon="💯")

st.write("")

st.write("Maybe you prefer explore only certain categories ?")
st.write("Here are the most famous ones : ")

st.text("")

# Lien vers la section "Antiquities"
st.page_link("pages/Antiquities.py", label="Antiquities", icon="🏺")
with st.expander("Click here to see what you will find inside"):
    st.markdown("- Greek, Etruscan and Roman Antiquities")
    st.markdown("- Oriental Antiquities")
    st.markdown("- Egyptian Antiquities")

st.text("")

# Lien vers la section "Middle Ages, Renaissance and Modern Times"
st.page_link("pages/Middle_Ages_Renaissance_Modern_Times_Objects_&_Sculptures.py", label="Middle Ages, Renaissance, Modern Times Art Objects & Sculptures", icon="⚒️")
with st.expander("Click here to see what you will find inside"):
    st.markdown("- Middle Ages, Renaissance & Modern Times Art Objects")
    st.markdown("- Middle Ages, Renaissance & Modern Times Scupltures")

st.text("")

# Lien vers la section "Paintings"
st.page_link("pages/Paintings.py", label="Paintings", icon="🎨")
st.write("Le Louvre is known to host some of the finest paintings in the art history. Have a look.")
st.text("")
st.write("I wish you a wonderful journey through this treasure trove of artistic masterpieces.")
st.write("Regards,")
st.write("Dimitri Kneur")