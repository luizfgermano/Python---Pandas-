

import pandas as pd

# base hospedagem
url = "https://caelum-online-public.s3.amazonaws.com/2928-transformacao-manipulacao-dados/dados_hospedagem.json"

# base moveis disponivel
url1 = "https://caelum-online-public.s3.amazonaws.com/2928-transformacao-manipulacao-dados/moveis_disponiveis.json"


dados = pd.read_json_normalize(url['info_moveis'])






















