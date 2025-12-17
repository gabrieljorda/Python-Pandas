from datetime import datetime
import pandas as pd
import streamlit as st

caminho_datasets = 'datasets'

df_compras = pd.read_csv(f'{caminho_datasets}/compras.csv' , sep=';' , index_col=0)
df_lojas = pd.read_csv(f'{caminho_datasets}/lojas.csv' , sep=';' , decimal=',' , index_col=0)
df_produtos = pd.read_csv(f'{caminho_datasets}/produtos.csv' , sep=';' , index_col=0)   

df_lojas["cidade/estado"] = df_lojas["cidade"] + '/' + df_lojas["estado"]
lista_lojas = df_lojas['cidade/estado'].to_list()
loja_selecionada = st.sidebar.selectbox('Selecione a loja:',lista_lojas)

lista_vendedores = df_lojas.loc[df_lojas['cidade/estado'] == loja_selecionada , 'vendedores'].iloc[0]
lista_vendedores = lista_vendedores.strip('][').replace("'" , " ").replace(']' , '').split(', ')
vendedor_selecionado = st.sidebar.selectbox("selecione o vendedor:", lista_vendedores)

lista_produtos = df_produtos['nome'].to_list()
produtos_selecionados = st.sidebar.selectbox("selecione o produto:", lista_produtos)

nome_cliente = st.sidebar.text_input("Nome do cliente:")
genero_selecionado = st.sidebar.selectbox("Genero do cliente:", ['Feminino' , 'Masculino'])

forma_pagamento_selecionado = st.sidebar.selectbox("Forma de Pgamento:", ['Dinheiro' , 'Cartão de Crédito' , 'Cartão de Débito' , 'Pix'])

if st.sidebar.button("adicionar nova conta"):
    lista_adicionar = [df_compras['id_compra'].max() +1 if not df_compras.empty else 1,
                       loja_selecionada,
                       vendedor_selecionado,
                       produtos_selecionados,
                       nome_cliente,
                       genero_selecionado,
                       forma_pagamento_selecionado,
                       ]
    df_compras.loc[datetime.now()] = lista_adicionar

    df_compras.to_csv(f'{caminho_datasets}/compras.csv' , index = False ,sep=';',descimal =',')
    
    st.succes("Compras adicionadas") 
    
st.dataframe(df_compras)