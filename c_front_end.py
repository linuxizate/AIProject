import streamlit as st
import b_backend

if 'preguntas' not in st.session_state:
    st.session_state.preguntas = []

if 'respuestas' not in st.session_state:
    st.session_state.respuestas = []

st.title("App para Usuario de Negocio")
st.write("Puedes hacerme a mi todas las preguntas y dejar trabajar al equipo de Sistemas!!")

def click():
    if st.session_state.user != '':
        pregunta = st.session_state.user
        respuesta = b_backend.consulta(pregunta)

        st.session_state.preguntas.append(pregunta)
        st.session_state.respuestas.append(respuesta)
        
        # Limpiar el input de usuario después de enviar la pregunta
        st.session_state.user = ''

with st.form('my-form'):
    query = st.text_input('¿En qué te puedo ayudar?:', key='user', help='Pulsa Enviar para hacer la pregunta')
    submit_button = st.form_submit_button('Enviar', on_click=click)

if st.session_state.preguntas:
    for i in range(len(st.session_state.preguntas) - 1, -1, -1):
       st.write(st.session_state.preguntas[i], st.session_state.respuestas [i])

    # Opción para continuar la conversación
    continuar_conversacion = st.checkbox('Quieres hacer otra pregunta?')
    if not continuar_conversacion:
        st.session_state.preguntas = []
        st.session_state.respuestas = []
    
# cuales son los 3 países en los que tenemos más ventas totales.  Saca una tabla con el país  y su total de ventas
# que porcentaje de las ventas totales representan las ventas de UK?
# dame los 5 productos que mas se han vendido en cantidad, en una tabla que tenga el nombre del producto y el porcentaje sobre el total de unidades de todos los productos. 
