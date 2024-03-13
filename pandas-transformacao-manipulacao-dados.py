

import pandas as pd
import numpy as np

dados = pd.read_json(r'C:\Users\luiz9\OneDrive\Documentos\Pandas python\dados_hospedagem.json')

dados.head()

# Aplicando json_normalize na coluna info_moveis
dados = pd.json_normalize(dados['info_moveis'])


#criando uma variavel com o nomes das coluna do dataframe dados
colunas = list(dados.columns)


#normalizando as outras colunas para não ser mais lista, da coluna 3 em diante
for coluna in colunas[3:]:
    dados = dados.explode(coluna)



dados.reset_index(inplace=True, drop=True)

#dados.head(25)

dados.info()



dados['max_hospedes'] = dados['max_hospedes'].astype(np.int64)


col_numericas = ['quantidade_banheiros','quantidade_quartos','quantidade_camas']










dados[col_numericas] = dados[col_numericas].astype(np.int64)


















'''


for i in dados:
    print(i)
    
    
    
    


for i in dados['comodidades'].unique():
    print(i)



'''





