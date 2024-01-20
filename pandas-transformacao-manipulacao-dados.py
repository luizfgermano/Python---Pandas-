# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 23:46:42 2023

@author: usuario
"""

import pandas as pd

# base hospedagem
url = "https://caelum-online-public.s3.amazonaws.com/2928-transformacao-manipulacao-dados/dados_hospedagem.json"

# base moveis disponivel
url1 = "https://caelum-online-public.s3.amazonaws.com/2928-transformacao-manipulacao-dados/moveis_disponiveis.json"


dados = pd.read_json_normalize(url['info_moveis'])






















