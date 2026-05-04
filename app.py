import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Exploración de Datos", layout="wide")

st.title("📊 Exploración de Datos con Streamlit")

# Subir archivo
archivo = st.file_uploader("Sube tu archivo CSV", type=["csv"])

if archivo is not None:
    df = pd.read_csv(archivo)

    st.success("✅ Archivo cargado correctamente")

    # Mostrar primeras filas
    st.subheader("Vista previa de los datos")
    st.dataframe(df.head())

    # Selección de columnas
    st.subheader("Selecciona columnas para correlación")

    columnas_numericas = df.select_dtypes(include=["float64", "int64"]).columns.tolist()

    columnas_seleccionadas = st.multiselect(
        "Elige al menos 2 columnas",
        columnas_numericas
    )

    if len(columnas_seleccionadas) >= 2:
        df_corr = df[columnas_seleccionadas]

        # Matriz de correlación
        corr = df_corr.corr()

        st.subheader("Matriz de correlación")
        st.dataframe(corr)

        # Heatmap
        st.subheader("🔥 Heatmap de correlación")

        fig, ax = plt.subplots()
        sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)

        st.pyplot(fig)

    else:
        st.warning("⚠️ Selecciona al menos 2 columnas numéricas para calcular la correlación")
