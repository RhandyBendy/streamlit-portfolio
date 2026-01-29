import streamlit as st


st.set_page_config(page_title="My webpage", page_icon=":tada:" , layout="wide")

st.subheader("Hi! My name is Rhandy")
st.title("This is my personal page")
st.write("I do some anime art and training for animation 2D. I'm also taking diploma Agrotechnology at Politeknik Jeli, Kelantan, Malaysia")
st.write("[You can find me here >] (https://www.youtube.com/@RhdyEuNaQL)")

st.image("images/Frieren.jpg",
         caption="My art",
         use_container_width=True)
