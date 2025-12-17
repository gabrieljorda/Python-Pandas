import random
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd
import names


pasta_datasets = Path(__file__).parent / "datasets"

pasta_datasets.mkdir(parents=True , exist_ok=True)


LOJAS = [
    {'estado': 'SP', 'cidade': 'São Paulo' , 
     "vendedores": ['Ana Silva', 'Bruno Souza']},
    {'estado': 'RJ', 'cidade': 'Rio de Janeiro' , 
     "vendedores": ['Carla Lima', 'Diego Alves']},
    {'estado': 'MG', 'cidade': 'Belo Horizonte' , 
     "vendedores": ['Eduardo Costa', 'Fernanda Rocha']},
    {'estado': 'BA', 'cidade': 'Salvador' , 
     "vendedores": ['Gabriela Santos', 'Hugo Pereira']},
    {'estado': 'RS', 'cidade': 'Porto Alegre' , 
     "vendedores": ['Isabela Fernandes', 'João Carvalho']},
]

Produtos = [
    {'nome': 'Notebook', 'id':0 ,'preco': 3500.00},
    {'nome': 'Smartphone', 'id':1 ,'preco': 2500.00},
    {'nome': 'Tablet', 'id':2 ,'preco': 1500.00},
    {'nome': 'Monitor', 'id':3 ,'preco': 800.00},
    {'nome': 'Teclado', 'id':4 ,'preco': 200.00},
    {'nome': 'Mouse', 'id':5 ,'preco': 100.00},
    ]

FORMA_PAGAMENTO = ['Dinheiro', 'Cartão de Crédito', 'Cartão de Débito', 'Pix']
GENERO_CLIENTES = ['Masculino', 'Feminino',]    

compras = []

for _ in range(2000):
    loja = random.choice(LOJAS)
    vendedor = random.choice(loja['vendedores'])
    produto = random.choice(Produtos)
    hora_compra = datetime.now() - timedelta(
        days = random.randint(0, 365),
        hours = random.randint(-5 , 5),
        minutes = random.randint(-30,30)
    )
    genero_cliente = random.choice(GENERO_CLIENTES)
    nome_cliente = names.get_full_name(genero_cliente)
    form_pagamento = random.choice(FORMA_PAGAMENTO)
    
    compras.append({
        'data': hora_compra,
        'id_compra':0,
        'loja':loja['cidade'],
        'vendedor':vendedor,
        'produto':produto['nome'],
        'cliente_nome':nome_cliente,
        'cliente_genero':genero_cliente,
        'forma_pagamento':form_pagamento,
    })

df_compras = pd.DataFrame(compras).set_index("data").sort_index()
df_compras['id_compra'] = [i for i in range(len(df_compras))]

df_lojas = pd.DataFrame(LOJAS)
df_produtos = pd.DataFrame(Produtos)

df_compras.to_csv(pasta_datasets / "compras.csv" , decimal =',', sep = ';')
df_lojas.to_csv(pasta_datasets / "lojas.csv" , decimal =',', sep = ';', )
df_produtos.to_csv(pasta_datasets / "produtos.csv" , decimal =',', sep = ';', )


df_compras.to_excel(pasta_datasets / "compras.xlsx")
df_lojas.to_excel(pasta_datasets / "lojas.xlsx" )
df_produtos.to_excel(pasta_datasets / "produtos.xlsx")

    

