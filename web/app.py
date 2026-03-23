import pandas as pd
import streamlit as st

st.title("Mi primera web")

st.subheader("Resumen - datos")

df= pd.read_csv("../data/clean/popular_movies.csv")

st.write(df.head(3))

col1, col2, col3 = st.columns(3)

col1.metric("Número de películas", df["title"].count())

col2.metric("Valoración media", df["vote_average"].mean())

import matplotlib.pyplot as plt
import ast

generos = df["genre_ids"].apply(ast.literal_eval).explode().value_counts().reset_index()

generos.columns = ['id_genero', 'conteo']

st.write(generos.head(2))

fig, ax = plt.subplots()

ax.bar(generos["id_genero"], generos["conteo"])

ax.set_xlabel("ID del Género")
ax.set_ylabel("Cantidad de Películas")
plt.xticks(rotation=45)

st.pyplot(fig)
