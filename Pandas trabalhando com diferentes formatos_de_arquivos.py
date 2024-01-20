# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 15:17:26 2023

@author: usuario
"""

'''

    arquivo.csv 'comma-separated values' 
    valores separados por vírgula

'''

import pandas as pd
# import sqlalchemy
#from sqlalchemy import create_engine, MetaData, Table, inspect


url = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/superstore_data.csv'
dados_mercado = pd.read_csv(url)

dados_mercado.head()


# importando os dados so que agora separando dor ';'
url2 = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/superstore_data_ponto_virgula.csv'
dados_mercado2 = pd.read_csv(url2, sep=';')

dados_mercado.head()

#usando o paramentro nrows mostrando 5 linha 
dados_primeiras_linhas = pd.read_csv(url, nrows=5)

# usando o paramentro usecols que carrega so as coluna digitadas
dados_selecao = pd.read_csv(url, usecols=['Id', 'Year_Birth', 'Income'])

# usando o parametro usecols so que passando o indice das coluna em vez do nome 
dados_selecao2 = pd.read_csv(url, usecols=[0, 1, 4])

# salvando o dataframe em csv tirando o indice 
dados_selecao.to_csv('cliente_mercado.csv', index=False)


#----------- Trabalhando com o excel -----------------------

url_planilha = 'https://github.com/alura-cursos/Pandas/blob/main/emissoes_CO2.xlsx?raw=True'

dados_planilha = pd.read_excel(url_planilha)

dados_planilha.head()

# descobrindo quantas paginas tem uma planilha  e passa o nome delas
pd.ExcelFile(url_planilha).sheet_names

#abrindo a pagina emissoes_percapita sendo que tem três 
excel_percapita = pd.read_excel(url_planilha, sheet_name='emissoes_percapita')

excel_percapita.head()

#abrindo a pagina fontes sendo que tem três
excel_fontes = pd.read_excel(url_planilha, sheet_name='fontes')

excel_fontes.head()

intervalo = pd.read_excel(url_planilha, sheet_name='emissoes_percapita', usecols='a:d')

#
intervalo_2 = pd.read_excel(url_planilha, sheet_name='emissoes_percapita', usecols='a:d', nrows=10)

#salvando e retirando o indice do dataframe
excel_percapita.to_excel('co2_percapita.xlsx', index=False)


#---------------------carregando dados google planilha------------------------------

#link 
'https://docs.google.com/spreadsheets/d/1lzq0k-41-MbbS63C3Q9i1wPvLkSJt9zhr4Jolt1vEog/edit?usp=sharing'

sheet_id = '1lzq0k-41-MbbS63C3Q9i1wPvLkSJt9zhr4Jolt1vEog'

url_planilha_google = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet'

dados_excel_google = pd.read_csv(url_planilha_google)

dados_excel_google.head()

sheet_id = '1lzq0k-41-MbbS63C3Q9i1wPvLkSJt9zhr4Jolt1vEog'

sheet_name = 'emissoes_percapita'

url_planilha_google2 = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'

dados_excel_google2 = pd.read_csv(url_planilha_google2)

#---------------------carregando dados json------------------------------

# json javascript object notacion em portugues objeto de notação javaScript

dados_paciente = pd.read_json(r'C:\Users\usuario\Documents\Pandas python\pacientes.json')

dados_paciente2 =pd.read_json(r'C:\Users\usuario\Documents\Pandas python\pacientes_2.json')

#usando o normalize 
df_normalizando = pd.json_normalize(dados_paciente2['Pacientes'])

df_normalizando.to_json('arquivo_json_salvo_e_normalizado')


#--------------------- carregando dados html / xml  ------------------------------


dados_html = pd.read_html(r'C:\Users\usuario\Documents\Pandas python\filmes_wikipedia.html')

len(dados_html)

type(dados_html)

top_filme_html = pd.read_html(r'C:\Users\usuario\Documents\Pandas python\filmes_wikipedia.html')[1]

#
top_filme_html.to_html('top_filme_html.html')

#
top_filme_html.to_csv('top_filme_html.csv', index=False)

#abrindo arquivo xml
dados_xml = pd.read_xml(r'C:\Users\usuario\Documents\Pandas python\imdb_top_1000.xml')

dados_xml.to_xml('filme_imdb.xml')


#--------------------- carregando dados do banco de dados  ------------------------------

import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, inspect

engine = create_engine('sqlite:///:memory:')

url_bd = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/clientes_banco.csv'

dados_bd = pd.read_csv(url_bd)

dados_bd.to_sql('Clientes', engine, index=False)

query = 'SELECT * FROM Clientes WHERE Categoria_de_renda = "Empregado"'

Empregado = pd.read_sql(query, engine)

#
Empregado.to_sql('empregados', con=engine, index=False)


pd.read_sql_table('empregados', engine)

# usei o columns trazendo o numero da coluna em vez do nome 
pd.read_sql_table('empregados', engine, columns=[0, 2, 8])


query = 'SELECT * FROM clientes'

pd.read_sql(query, engine) 

query = 'DELETE FROM clientes WHERE ID_Cliente = 5008804'
with engine.connect() as conn:
    conn.execute(query)


pd.read_sql_table('clientes', engine)



query = 'UPDATE clientes SET Grau_escolaridade="Ensino superior" WHERE ID_Cliente=5008808'
with engine.connect() as conn:
    conn.execute(query)

pd.read_sql_table('clientes', engine)


query = 'INSERT INTO clientes (ID_Cliente, Idade, Grau_escolaridade, Estado_civil, ' \
        'Tamanho_familia, Categoria_de_renda, Ocupacao, Anos_empregado, ' \
        'Rendimento_anual, Tem_carro, Moradia) ' \
        'VALUES (6850985, 33, "Doutorado", "Solteiro", 1, "Empregado", "TI", ' \
        '2, 290000, 0, "Casa/apartamento próprio")'

with engine.connect() as conn:
    conn.execute(query)

pd.read_sql_table('clientes', engine)









