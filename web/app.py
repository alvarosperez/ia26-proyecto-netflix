import streamlit as st
import pandas as pd

st.title("Proyecto Netflix")
st.subheader("Resumen - Datos")

# Ruta correcta al CSV
movies_df = pd.read_csv("data/popular_movies.csv")   

st.write(movies_df.head(3))