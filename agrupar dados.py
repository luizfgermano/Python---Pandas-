# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 14:35:27 2023

@author: usuario
"""

import pandas as pd

url = r'C:\Users\usuario\Documents\Pandas python\dados\1-SEEG10_GERAL-BR_UF_2022.10.27-FINAL-SITE.xlsx'

pd.ExcelFile(url).sheet_names

emissoes_gases = pd.read_excel(url, sheet_name='GEE Estados')

emissoes_gases.info()

emissoes_gases['Emissão / Remoção / Bunker'].unique()


(emissoes_gases['Emissão / Remoção / Bunker'] == 'Remoção NCI') | (emissoes_gases['Emissão / Remoção / Bunker'] == 'Remoção')


emissoes_gases[emissoes_gases['Emissão / Remoção / Bunker'].isin(['Remoção NCI', 'Remoção'])]

emissoes_gases.loc[emissoes_gases['Emissão / Remoção / Bunker'].isin(['Remoção NCI', 'Remoção']), 1970:2021]

emissoes_gases.loc[emissoes_gases['Emissão / Remoção / Bunker'] == 'Bunker', 'Estado'].unique()

emissoes_gases = emissoes_gases[emissoes_gases['Emissão / Remoção / Bunker'] == 'Emissão']

emissoes_gases = emissoes_gases.drop(columns = 'Emissão / Remoção / Bunker')

emissoes_gases.loc[:,'Nível 1 - Setor':'Produto'].columns

colunas_info = list(emissoes_gases.loc[:,'Nível 1 - Setor':'Produto'].columns)

emissoes_gases.loc[:,1970:2021].columns

colunas_emissao = list(emissoes_gases.loc[:,1970:2021].columns)

emissoes_gases.melt(id_vars = colunas_info, value_vars = colunas_emissao, var_name = 'Ano' , value_name = 'Emissão')

emissoes_por_ano = emissoes_gases.melt(id_vars = colunas_info, value_vars = colunas_emissao, var_name = 'Ano' , value_name = 'Emissão')

#
emissoes_por_ano.groupby('Gás')

emissoes_por_ano.groupby('Gás').groups

emissoes_por_ano.groupby('Gás').get_group('CO2 (t)')

'''
--podemos usar o group by com um método agregador abaixo.

-count() para realizar contagem;
-sum() para soma;
-mean() para a média;
-median() para a mediana;
-min() para o valor mínimo;
-max() para o valor máximo;
-std() para o desvio-padrão;
-var() para a variância.

'''

# agrupando e usando um método de agrupamento sum()
#desse jeito ele ja reconhece a coluna numerica Emissão e realizou o calculo
#emissoes_por_ano.groupby('Gás').sum()

#desse jeito eu passo o nome da coluna Emissão para fazer o calculo 
emissoes_por_ano.groupby('Gás')[['Emissão']].sum()

#
emissoes_por_gas = emissoes_por_ano.groupby('Gás')[['Emissão']].sum().sort_values('Emissão', ascending = False)

#criando grafico
emissoes_por_gas.plot(kind = 'barh', figsize = (10,6))

#pegando so os gases de co2
emissoes_por_gas.iloc[0:9]

print('A emissão de CO2 corresponde a {:.2f} % de emissão total de gases estufa no brasil de 1970 a 2021'.format(float(emissoes_por_gas.iloc[0:9].sum() / emissoes_por_gas.sum()) * 100))

#-------------------------------------------------------------------------------------

'''
    -Quais as atividades econômicas mais poluentes para cada tipo de gás;
    -E quais são os gases mais poluentes para cada atividade econômica.
'''

#
gas_por_setor = emissoes_gases.groupby(['Gás', 'Nível 1 - Setor'])[['Emissão']].sum()

emissoes_gases.columns






































