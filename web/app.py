import pandas as pd
import streamlit as st

st.title("Proyecto Netflix")

st.subheader("Resumen - datos")

df= pd.read_csv("../data/clean/popular_movies.csv")

st.write(df.head(3))

col1, col2, col3 = st.columns(3)

col1.metric("Número de películas", df["title"].count())

col2.metric("Valoración media", df["vote_average"].mean())

import matplotlib.pyplot as plt
import ast

generos = df["genre_ids"] \
    .apply(ast.literal_eval).explode().value_counts() \
    .reset_index()

st.write(generos.head(2))

fig, ax = plt.subplots()
ax.barh(generos["genre_ids"], generos["count"])
ax.invert_yaxis()
st.pyplot(fig)

st.sidebar.header("Filtros")

# st.sidebar.selectbox
# st.sidebar.date
nota_seleccionada = st.sidebar.slider("Nota", 0, 10)

df_filtrado = df[df["vote_average"] > nota_seleccionada]
st.write(df_filtrado.sort_values("vote_average", ascending=False))
