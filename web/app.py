import pandas as pd

import streamlit as st

st.title("Proyecto Netflix")

st.subheader("Resumen - datos")
df = pd.read_csv(".../../data/clean/popular_movies.csv")
st.write(df.head(3))
st.write(df["title"].count())