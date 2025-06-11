import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('data/vehicles.csv')
st.write(
    'Bem vindo a página de análise de carros! Aqui trazemos uma análise de milhagem do odômetro e preço. Escolha a opção de vizualizção.')

hist_button = st.checkbox('Criar histograma')
scatter_button = st.checkbox('Criar um gráfico de dispersão')

if hist_button:
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)
elif scatter_button:
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    # criar um gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

    # fig.show()  # exibindo
