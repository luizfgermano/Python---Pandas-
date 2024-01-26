

#link para ve correção 
#https://github.com/alura-cursos/pandas-conhecendo-a-biblioteca/blob/main/aula-4/projeto_imobiliaria_final.ipynb

#import matplotlib.pyplot as plt
import pandas as pd


url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
pd.read_csv(url)

pd.read_csv(url, sep=';')

dados = pd.read_csv(url, sep=';')

dados.tail()

type(dados)

dados.shape

dados.columns

dados.info()

dados['Tipo']

dados[['Quartos', 'Valor']]

dados['Valor'].mean()

agrupado = dados.groupby('Tipo')['Valor'].mean().sort_values()

agrupado.plot(kind='barh', figsize=(14, 10), color='purple')

#plt.show()  # Exibe o gráfico

dados.Tipo.unique()

imoveis_comerciais = ['Conjunto Comercial/Sala', 
                      'Prédio Inteiro', 'Loja/Salão', 
                      'Galpão/Depósito/Armazém', 
                      'Casa Comercial', 'Terreno Padrão',
                      'Loja Shopping/ Ct Comercial',
                      'Box/Garagem', 'Chácara',
                      'Loteamento/Condomínio', 'Sítio',
                      'Pousada/Chalé', 'Hotel', 'Indústria']

dados.query('@imoveis_comerciais in Tipo')

df = dados.query('@imoveis_comerciais not in Tipo')

df.Tipo.unique()

df_preco_tipo_imoveis_residencial = df.groupby('Tipo')['Valor'].mean().sort_values()

df_preco_tipo_imoveis_residencial.plot(kind='barh', figsize=(14,10), color ='purple')


df.Tipo.unique()

df.Tipo.value_counts(normalize=True)

df_percentual_tipo = df.Tipo.value_counts(normalize=True)

df_percentual_tipo.plot(kind='bar', figsize=(14,10), color='orange')

#---------------------tratando valores nulos no dataframe------------------


# verifica valores nulos nas colunas
df.isnull()

#contando os valores nulos por coluna 
df.isnull().sum()

# substituindo os valores nulos por 0
df = df.fillna(0)

#contando os valores nulos por coluna 
df.isnull().sum()

#---------------------------------------------------------------------


df.query('Valor == 0 or Condominio == 0')

registro_remover = df.query('Valor == 0 or Condominio == 0').index

# removendo linhas 
df.drop(registro_remover, axis=0, inplace= True) 

df.query('Valor == 0 or Condominio == 0')

df.Tipo.unique()

remover = ['Quitinete', 'Flat', 'Casa de Condomínio', 'Casa', 'Casa de Vila', 'Loft', 'Studio']

df.drop(df[df['Tipo'].isin(remover)].index, axis=0, inplace=True)

df.Tipo.unique

df.drop('Tipo', axis=1, inplace=True)

df.head()

# --------------filtrando os dados------------------------------- 

# apartamento possuem 1 quarto e aluguel menor que 1200
selecao1 = df.query('Quartos == 1 and Valor < 1200')

#apartamento que possuem 2 quartos, aluguel menor que 3000 e area > 70
selecao2 = df.query('Quartos == 2 and Valor < 3000 and Area > 70')


df.to_csv('dados_apartamento.csv', index=False)

selecao_final = [selecao1] and [selecao2]

#------------------------------------------------

#mporta novamente a base de dados 

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'

dados2 = pd.read_csv(url, sep=';')

dados2['Valor_por_mes'] = dados2['Valor'] + dados2['Condominio']

dados2['Valor_por_ano'] = dados2['Valor_por_mes'] * 12 + dados2['IPTU']

#-----------------------------------------------------------------

dados2['Descricao'] = dados2['Tipo'] + ' em ' + dados2['Bairro']


# a \ quebra a linha para o codigo nao ficar numa unica linha 
dados2['Descricao'] = dados2['Tipo'] + ' em ' + dados2['Bairro'] + ' com ' + \
                                        dados2['Quartos'].astype(str) + ' quarto(s) ' + \
                                        ' e ' + dados2['Vagas'].astype(str) + ' vaga(s) de garagem.'


dados2['Possui_suite'] = dados2['Suites'].apply(lambda x: "Sim" if x > 0 else "Não")


dados2.to_csv('dados2_completo_dev_.csv', index=False, sep=';')

