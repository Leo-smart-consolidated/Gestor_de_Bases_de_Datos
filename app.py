import streamlit as st
import pandas as pd

st.title("Gestor de Bases de Datos")

# Datos iniciales
if "tabla" not in st.session_state:
    st.session_state.tabla = pd.DataFrame(
        columns=[
            "ID",
            "Nombre",
            "Descripción"
        ]
    )

# Hoja de cálculo editable
st.session_state.tabla = st.data_editor(
    st.session_state.tabla,
    num_rows="dynamic",
    use_container_width=True
)

# Vista previa de los datos
st.subheader("Datos almacenados")

st.dataframe(st.session_state.tabla)
