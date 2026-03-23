import pandas as pd
import streamlit as st
import matplotlib as plt

st.title("Mi primera web")
st.subheader("Resumen - datos")

df = pd.read_csv("../data/clean/popular_movies.csv")

st.write(df.head(3))

col1, col2, col3 = st.columns(3)

col1.metric("Número de películas", df["title"].count())
col2.metric("Valoración media", round(df["vote_average"].mean(), 2))

import ast

generos = df["genre_ids"] \
    .apply(ast.literal_eval).explode().value_counts() \
    .reset_index()

st.write(generos.head(2))

fig, ax = plt.subplots()
ax = plt.bar(generos["genre_ids"], generos["count"])
# ax.invert_yaxis()
st.pyplot(fig)