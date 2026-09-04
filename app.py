import streamlit as st
import pandas as pd
from pathlib import Path

ARCHIVO = "datos.xlsx"

# Crear archivo si no existe
if not Path(ARCHIVO).exists():

    df_nuevo = pd.DataFrame({
        "Concepto": [],
        "Cantidad": [],
        "Precio": []
    })

    df_nuevo.to_excel(ARCHIVO, index=False)

# Leer excel
df = pd.read_excel(ARCHIVO)

st.title("Mini Hoja de Cálculo")

# Tabla editable
df_editado = st.data_editor(
    df,
    num_rows="dynamic",
    use_container_width=True
)

# Cálculo automático
if not df_editado.empty:

    df_editado["Cantidad"] = pd.to_numeric(
        df_editado["Cantidad"],
        errors="coerce"
    )

    df_editado["Precio"] = pd.to_numeric(
        df_editado["Precio"],
        errors="coerce"
    )

    df_editado["Total"] = (
        df_editado["Cantidad"].fillna(0)
        * df_editado["Precio"].fillna(0)
    )

# Mostrar resultado
st.dataframe(df_editado)

st.metric(
    "Suma Total",
    f"${df_editado['Total'].sum():,.2f}"
)

# Guardar
if st.button("Guardar"):

    df_editado.to_excel(
        ARCHIVO,
        index=False
    )

    st.success("Información guardada")
