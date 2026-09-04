import streamlit as st
import pandas as pd
from pathlib import Path

ARCHIVO = "datos.xlsx"

# Crear archivo si no existe
if not Path(ARCHIVO).exists():
    df_inicial = pd.DataFrame(
        columns=[
            "Fecha",
            "Concepto",
            "Cantidad",
            "Precio Unitario",
            "Total"
        ]
    )

    df_inicial.to_excel(ARCHIVO, index=False)

# Leer datos
df = pd.read_excel(ARCHIVO)

st.title("Mini Hoja de Cálculo")

# Edición
df_editado = st.data_editor(
    df,
    num_rows="dynamic",
    use_container_width=True
)

# Recalcular total
if not df_editado.empty:

    df_editado["Cantidad"] = pd.to_numeric(
        df_editado["Cantidad"],
        errors="coerce"
    )

    df_editado["Precio Unitario"] = pd.to_numeric(
        df_editado["Precio Unitario"],
        errors="coerce"
    )

    df_editado["Total"] = (
        df_editado["Cantidad"]
        * df_editado["Precio Unitario"]
    )

# Mostrar suma general
total_general = df_editado["Total"].fillna(0).sum()

st.metric(
    "Total General",
    f"${total_general:,.2f}"
)

# Guardar
if st.button("Guardar"):
    df_editado.to_excel(
        ARCHIVO,
        index=False
    )

    st.success("Datos guardados")
