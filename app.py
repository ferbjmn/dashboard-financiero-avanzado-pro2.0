import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from modulos.modulo_comparador_acciones import obtener_datos_acciones
from modulos.modulo_analisis_valoracion import analisis_valoracion
from modulos.modulo_rentabilidad_eficiencia import rentabilidad_eficiencia
from modulos.modulo_estructura_deuda import estructura_deuda
from modulos.modulo_crecimiento_historico import crecimiento_historico

# Título del Dashboard
st.title("Análisis Financiero Avanzado")

# Subtítulo
st.subheader("Bienvenido al Dashboard de Análisis Financiero")

# Ingreso de tickers
tickers_input = st.text_input("Ingresa los tickers de las empresas (separados por coma)", "AAPL, MSFT, GOOGL")
tickers = [ticker.strip() for ticker in tickers_input.split(",")]

if tickers:
    # Cargar datos de las acciones
    st.subheader("Comparador de Acciones")
    df_comparativo = obtener_datos_acciones(tickers)
    st.dataframe(df_comparativo)

    # Análisis de valoración
    st.subheader("Análisis de Valoración")
    analisis_valoracion(df_comparativo)

    # Rentabilidad y eficiencia
    st.subheader("Rentabilidad y Eficiencia")
    rentabilidad_eficiencia(df_comparativo)

    # Estructura de deuda
    st.subheader("Estructura de Capital y Deuda")
    estructura_deuda(df_comparativo)

    # Crecimiento histórico
    st.subheader("Crecimiento Histórico")
    crecimiento_historico(df_comparativo)
