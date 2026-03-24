import pandas as pd
import streamlit as st
import os

st.title("Proyecto Netflix")

st.subheader("Resumen - datos")

# 🔧 ARREGLO DE RUTA
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(base_dir, "data", "clean", "popular_movies.csv")

df = pd.read_csv(csv_path)

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

st.pyplot(fig)