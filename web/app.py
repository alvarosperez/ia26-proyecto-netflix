import streamlit as st
import pandas as pd

st.title("Mi primera web")

st.subheader("Resumen - datos")

df = pd.read_csv("../data/clean/population.csv")

st.write(df.head(3))

col1, col2 = st.columns(2)

col1.metric("Número de películas", df["title"].count())
col2.metric("Valoración media", df["vote_average"].mean())

