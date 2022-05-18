#!/usr/bin/env python
# coding: utf-8

# # Tarefa 01
# 
# - Leia os enunciados com atenção
# - Saiba que pode haver mais de uma resposta correta
# - Insira novas células de código sempre que achar necessário
# - Em caso de dúvidas, procure os tutores
# - Divirta-se :)
# 
# #### 1)  crie uma série do pandas a partir de uma lista com os dados abaixo:
# 
# Em um estudo sobre alteração na tempreatura global, A NASA disponibiliza dados de diferenças de de temperatura média da superfície terrestre relativos às médias de temperatura entre 1951 e 1980. Os dados originais podem ser vistos no site da NASA/GISS, e estão dispostos a cada década na tabela abaixo.
# 
# |ano|anomalia termica|
# |:-:|:----:|
# | 1900 | -0.08 |
# | 1920 | -0.27 |
# | 1940 | 0.12 |
# | 1960 | -0.03 |
# | 1980 | 0.26 |
# | 2000 | 0.40 |
# | 2020 | 1.02 |
# 
# Crie uma séries do Pandas a partir de uma lista com esses dados.

# In[7]:


import pandas as pd
import numpy as np

anomalia_termica = [-0.08, -0.27, 0.12, -0.03, 0.26, 0.40, 1.02]
Serie_anomalia = pd.Series(anomalia_termica)
Serie_anomalia


# #### 2) Coloque os anos nos índices conforme a tabela.

# In[9]:



ano = [1990, 1920, 1940, 1960, 1980, 2000, 2020]
Serie_anomalia_index = pd.Series(anomalia_termica, index = ano)
Serie_anomalia_index


# #### 3) A partir do dicionário abaixo, crie uma séries do Pandas:

# In[11]:


dic_temperaturas = {1900: -.08, 1920: -.27, 1940: .12, 1960: -.03, 1980: .26, 2000: .40, 2020: 1.02}

Serie_dic_anomalia = pd.Series(dic_temperaturas)
Serie_dic_anomalia


# #### 4) Transforme o ndarray abaixo em um dataframe. 
# O numpy é capaz de gerar arrays n-dimensionais com números pseudo-aleatórios de acordo com uma variedade de distribuições, como no exemplo abaixo. Transforme esse nd-array em um DataFrame.

# In[30]:


arr = np.random.normal(100, 10, (20,3))

pd.DataFrame(arr)


# #### 5) Nomeie os índices das linhas com inteiros de 1 a 20, e as colunas com os nomes "x1", "x2", e "x3" respectivamente.

# In[47]:



tabela = pd.DataFrame(arr, index = list(range(1,21)), columns=['x1','x2','x3'])
tabela


# #### 6) No DataFrame do exercício 5, crie uma nova coluna como sendo a média das três colunas, e dê a ela o nome de "media" (não recomendo colocar acentos em nomes de variáveis).

# In[49]:


tabela['media'] = (tabela['x1'] + tabela['x2'] + tabela['x3'])/3
tabela


# #### 7) No DataFrame do exercício 6, crie uma nova coluna chamada "log_med", contendo o logaritmo natural da média calculada no exercício 6 <br>

# In[52]:



tabela['log_med'] = np.log(tabela['media'])
tabela

