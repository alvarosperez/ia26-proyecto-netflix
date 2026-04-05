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



#  SECCIÓN DE SERIES 
st.markdown("---") 
st.title("Sección de Series")

df_series = pd.read_csv("../data/clean/popular_series.csv") 

st.write(df_series.head(3))

s_col1, s_col2 = st.columns(2)
nombre_col = "name" if "name" in df_series.columns else "title"

s_col1.metric("Número de series", df_series[nombre_col].count())
s_col2.metric("Valoración media series", round(df_series["vote_average"].mean(), 2))

st.subheader("Géneros de Series")
generos_s = df_series["genre_ids"].apply(ast.literal_eval).explode().value_counts().reset_index()
generos_s.columns = ['id_genero', 'conteo']

fig2, ax2 = plt.subplots()
ax2.bar(generos_s["id_genero"].astype(str), generos_s["conteo"], color="orange")
ax2.set_ylabel("Cantidad de Series")
plt.xticks(rotation=45)
st.pyplot(fig2)