import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import os

st.title("Lectura de datos desde Firestore")

# Inicializar Firebase (una sola vez)
if not firebase_admin._apps:
    try:
        st.write("Inicializando Firebase...")
        cred = credentials.Certificate(r"C:\Users\Lenovo\Documents\DataScience\EnvData\BootCamp_Xperience\DS_Ecommerce_Web_Platform\serviceAccountKey.json")
        firebase_admin.initialize_app(cred)
        st.success("Firebase inicializado")
    except Exception as e:
        st.error(f"Error al inicializar Firebase: {e}")

# Obtener cliente Firestore
try:
    st.write("Firestore listo")
    db = firestore.client()
except Exception as e:
    st.error(f"No se pudo conectar con Firestore: {e}")

# Leer colección
st.write("Obteniendo documentos de prueba...")
    
try:
    carritos_ref = db.collection("carritos")
    docs = list(carritos_ref.stream())  # Lo forzamos a lista para que no se congele

    if not docs:
        st.warning("No hay documentos en la colección 'carritos'")
    else:
        for doc in docs:
            st.subheader(f"Documento ID: {doc.id}")
            st.json(doc.to_dict())

except Exception as e:
    st.error(f"Error al leer documentos: {e}")