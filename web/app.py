import streamlit as st
import pandas as pd

st.title("Proyecto Netflix")

st.subheader("Resumen - datos")

df= pd.read_csv("../data/clean/popular_movies.csv")

st.write(df.head(3))

col1, col2, col3 = st.columns(3)


col1.metric("Número de películas", df["title"].count())

col2.metric("Valoración de media", df["vote_average"].mean())

import matplotlib.pyplot as plt
import ast

generos = df["genre_ids"].apply(ast.literal_eval).explode().value_counts().reset_index()

st.write(generos.head(2))

fig, ax = plt.subplots()
ax = plt.barh(generos["genre_ids"], generos["count"])
# ax.invert_yaxis()
st.pyplot(fig)