import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("Proyecto Netflix RYAO")
st.subheader("Resumen - datos")

df = pd.read_csv("data/clean/popular_movies.csv")

st.write(df.head(3))

col1, col2, col3 = st.columns(3)

col1.metric("Número de películas", df["title"].count())
col2.metric("Valoración media", round(df["vote_average"].mean(), 2))

import ast

generos = df["genre_ids"].astype(str).str.strip("[]").str.replace("'", "").str.split(", ").explode().value_counts().head(10)
fig, ax = plt.subplots()
ax.barh(generos.index, generos.values)
ax.invert_yaxis()
st.pyplot(fig)

st.sidebar.header("Filtros")

# st.sidebar.selectbox
# st.sidebar.date
nota_seleccionada = st.sidebar.slider("Nota", 0, 10)

df_filtrado = df[df["vote_average"] > nota_seleccionada]
st.write(df_filtrado.sort_values("vote_average", ascending=False))
