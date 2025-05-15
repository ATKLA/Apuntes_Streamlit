import streamlit as st
import time
from datetime import datetime, date


st.set_page_config(page_title="Demo de streamlit", page_icon=":)",layout="wide")

#------Seccion 1 arriba ---------
with st.container():
    st.title("Sección superior")
    st.header("Esto es un encabezado")
    st.subheader("Esto es un sub-encabezado")
    st.write("Esto es un write")
    st.markdown("---")#linea divisoria

#------Seccion 2 medio---------
with st.container():
    st.title("Sección central")
    #--------------------------------input texto
    name = st.text_input(
        label='Nombre',
        placeholder='Escribe tu nombre aquí...',  # Indicador
    )

    # Mostrar mensaje solo si se ha ingresado texto
    if name:  # Si name no está vacío
        st.success(f"✅ Nombre introducido: {name}")
    else:
        st.warning("⚠️ Por favor ingresa tu nombre")

    # Selector múltiple

    Ingredientes = st.multiselect(
        "Ingredientes:",
        options = ["Avena", "Miel", "Platano", "Leche"],
        placeholder = "Selecciona al menos un ingrediente...",
        default = None
    )

    #-------------------------------input numérico
    numero = st.number_input(
            label="Selecciona un número",
            min_value=0,
            max_value=100,
            step=2
    )
    st.write(f"Valor seleccionado: {numero}")


    #-------------------------------input fecha
    fecha = st.date_input(
        label='Selecciona una fecha'
    )

    #-------------------------------BOTONES
    if st.button("Saludar"):
        st.write(f"Hola, {name}!")

    if st.checkbox("Acepto términos"):
        st.markdown("***Términos aceptados***")  # Texto en cursiva y negrita

    option = st.radio("Opción", ["A", "B", "C"])

    #-------------------------------BARRA DE PROGRESO
    st.subheader("Barra de progreso ")
    progreso = st.progress(0)
    for porcentaje in range(0, 101, 20):
        time.sleep(0.5)
        progreso.progress(porcentaje)


#------Seccion 3 abajo---------
with st.container():
    st.title("Seccion inferior")
    col1, col2 = st.columns(2)

    with col1:
        fecha = st.slider(
            label="Selecciona una fecha",
            min_value=date(2020,12,31),
            max_value=date(2030,12,31),
            value=date.today(),
            format="DD/MM/YYYY"
        )
        st.write(f"Fecha seleccionada: {fecha}")
    with col2:
        minutos = st.slider(
            label="Selecciona minutos",  # Texto descriptivo
            min_value=0,  # Valor mínimo
            max_value=120,  # Valor máximo
            value=0,  # Valor por defecto
            step=1  # Incremento (opcional)
        )
        st.write(f"Minutos seleccionada: {minutos}")

    st.markdown("---")#linea divisoria

with st.expander("Ver codigo en Python"):  # Contenido plegable
     st.code('''
import streamlit as st
import time
from datetime import datetime, date


st.set_page_config(page_title="Demo de streamlit", page_icon=":)",layout="wide")

#------Seccion 1 arriba ---------
with st.container():
    st.title("Sección superior")
    st.header("Esto es un encabezado")
    st.subheader("Esto es un sub-encabezado")
    st.write("Esto es un write")
    st.markdown("---")#linea divisoria

#------Seccion 2 medio---------
with st.container():
    st.title("Sección central")
    #--------------------------------input texto
    name = st.text_input(
        label='Nombre',
        placeholder='Escribe tu nombre aquí...',  # Indicador
    )

    # Mostrar mensaje solo si se ha ingresado texto
    if name:  # Si name no está vacío
        st.success(f"✅ Nombre introducido: {name}")
    else:
        st.warning("⚠️ Por favor ingresa tu nombre")

    # Selector múltiple

    Ingredientes = st.multiselect(
        "Ingredientes:",
        options = ["Avena", "Miel", "Platano", "Leche"],
        placeholder = "Selecciona al menos un ingrediente...",
        default = None
    )

    #-------------------------------input numérico
    numero = st.number_input(
            label="Selecciona un número",
            min_value=0,
            max_value=100,
            step=2
    )
    st.write(f"Valor seleccionado: {numero}")


    #-------------------------------input fecha
    fecha = st.date_input(
        label='Selecciona una fecha'
    )

    #-------------------------------BOTONES
    if st.button("Saludar"):
        st.write(f"Hola, {name}!")

    if st.checkbox("Acepto términos"):
        st.markdown("***Términos aceptados***")  # Texto en cursiva y negrita

    option = st.radio("Opción", ["A", "B", "C"])

    #-------------------------------BARRA DE PROGRESO
    st.subheader("Barra de progreso ")
    progreso = st.progress(0)
    for porcentaje in range(0, 101, 20):
        time.sleep(0.5)
        progreso.progress(porcentaje)


#------Seccion 3 abajo---------
with st.container():
    st.title("Seccion inferior")
    col1, col2 = st.columns(2)

    with col1:
        fecha = st.slider(
            label="Selecciona una fecha",
            min_value=date(2020,12,31),
            max_value=date(2030,12,31),
            value=date.today(),
            format="DD/MM/YYYY"
        )
        st.write(f"Fecha seleccionada: {fecha}")
    with col2:
        minutos = st.slider(
            label="Selecciona minutos",  # Texto descriptivo
            min_value=0,  # Valor mínimo
            max_value=120,  # Valor máximo
            value=0,  # Valor por defecto
            step=1  # Incremento (opcional)
        )
        st.write(f"Minutos seleccionada: {minutos}")

    st.markdown("---")#linea divisoria

with st.expander("Ver codigo en Python"):  # Contenido plegable
     # st.code(''' ''', language='python')
''', language='python')

