#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# ##### Abrindo Pacote *basedosdados* e demais 

# In[ ]:


import basedosdados as bd


# In[444]:


import matplotlib.pyplot as plt


# In[445]:


import seaborn as sbs


# In[446]:


import pandas as pd


# In[447]:


import plotly.express as px


# ---
# ## Avaliando Produtividade Agrícola de Arroz e Feijão
# ##### Datalake **Censo Agropecuário**
# ---

# A produtividade da agrícola pode ser definida como a razão entre o **produção total (em Tonaladas)** e a **area total (em Hectares)**. Dessa meneira, é um parâmetro capaz de indicar que regiões são mais produtivas que as outras, levando em consideração a produção gerada em relação à área que foi plantada.
# 
# Alguns pontos importantes a serem analisados:
# * Relação entre valor total e área total plantada;
# * Produtividade total por estado brasileiro em 2017;
# * Produtividade municipal média por estado brasileiro em 2017.

# In[81]:


# Acessar o datalake

df = bd.read_table(dataset_id='br_ibge_censo_agropecuario',
table_id='municipio', billing_project_id="basedosdados-360312")


# In[354]:


# Conhecer base de dados
display(df)


# In[403]:


# Criando tabela de dados
dados = df[["ano","sigla_uf", "id_municipio", "producao_total_arroz" , "area_arroz","producao_total_feijao" , "area_feijao"]]


# In[404]:


# Deletando linhas vazias
dados = dados.dropna()


# In[405]:


# Filtrando dados de 2017
dados_2017 = dados.loc[(dados['ano'] == 2017)]


# In[430]:


#Convertendo ano em string
dados_2017= dados_2017.replace([2017],"2017")


# ---
# ### ARROZ

# In[409]:


# Criando a variavel de produtividade
dados_2017["produtividade_arroz"] = (dados_2017["producao_total_arroz"] / dados_2017["area_arroz"])


# In[431]:


#Gráfico de dispersão
Graf_dis_arroz = px.scatter(dados,
                            x="producao_total_arroz", y="area_arroz", color="ano",
                            title= "GRÁFICO DE DISPERSÃO PRODUÇÃO TOTAL X ÁREA PLANTADA - ARROZ")
Graf_dis_arroz.show()


# In[432]:


#PRODUTIVIDADE TOTAL DO ARROZ POR ESTADO
#É o somatório de produtividade dos municípios de cada estado
produtividade_total_arroz= dados_2017.groupby('sigla_uf').sum()
produtividade_total_arroz= produtividade_total_arroz[['produtividade_arroz']].sort_values(by= 'produtividade_arroz', ascending= False)

#GRÁFICO DE BARRAS
graf_total_arroz = px.bar(produtividade_total_arroz,
                          x = produtividade_total_arroz.index,
                          y = "produtividade_arroz",
                          title = "PRODUTIVIDADE TOTAL DE ARROZ POR ESTADO")
graf_total_arroz.show()


# In[427]:


#PRODUTIVIDADE MÉDIA MUNICIPAL DO ARROZ POR ESTADO
produtividade_media_arroz= dados_2017.groupby('sigla_uf').mean()
produtividade_media_arroz= produtividade_media_arroz[['produtividade_arroz']].sort_values(by= 'produtividade_arroz', ascending= False)

#GRÁFICO DE BARRAS
graf_media_arroz = px.bar(produtividade_media_arroz,
                          x = produtividade_media_arroz.index,
                          y = "produtividade_arroz",
                          title = "PRODUTIVIDADE MÉDIA MUNICIPAL DE ARROZ POR ESTADO")
graf_media_arroz.show()


# ### **Insights**
# 
# * O gráfico de dispensão indica `forte correlação` levemente `positiva` entre as variáveis *produção total de arroz* e *área total destinada ao plantio de arroz*, mostrando que as duas variáveis tendem a diminuir ou aumentar juntas;
# * O estado com `maior` produtividade total de arroz foi o `Mato Grasso (MT)`, com produção média de `4159,41 T/Ha`;
# * O estado com `menor` produtividade total de arroz foi o `Distrito Federal (DF)`, com produção média de `0,87 T/Ha`;
# * O estado com `maior` produtividade média municipal de arroz foi o `Mato Grasso (MT)`, com produção de `30,14 T/Ha`;
# * O estado com `menor` produtividade média municipal de arroz foi o `Paraíba(PB)`, com produção de `0,36 T/Ha`.
# 
# 

# ---
# ### FEIJÃO

# In[428]:


# Criando a variavel de produtividade
dados_2017["produtividade_feijao"] = (dados_2017["producao_total_feijao"] / dados_2017["area_feijao"])


# In[433]:


#Gráfico de dispersão
Graf_dis_feijao = px.scatter(dados,
                            x="producao_total_feijao", y="area_feijao", color="ano",
                            title= "GRÁFICO DE DISPERSÃO PRODUÇÃO TOTAL X ÁREA PLANTADA - FEIJÃO")
Graf_dis_feijao.show()


# In[434]:


#PRODUTIVIDADE TOTAL DO FEIJAO POR ESTADO
produtividade_total_feijao= dados_2017.groupby('sigla_uf').sum()
produtividade_total_feijao= produtividade_total_feijao[['produtividade_feijao']].sort_values(by= 'produtividade_feijao', ascending= False)

#GRÁFICO DE BARRAS
graf_total_feijao = px.bar(produtividade_total_feijao,
                          x = produtividade_total_feijao.index,
                          y = "produtividade_feijao",
                          title = "PRODUTIVIDADE TOTAL DO FEIJÃO POR ESTADO")
graf_total_feijao.show()


# In[436]:


#PRODUTIVIDADE MÉDIA MUNICIPAL DE FEIJÃO POR ESTADO
produtividade_media_feijao= dados_2017.groupby('sigla_uf').mean()
produtividade_media_feijao= produtividade_media_feijao[['produtividade_feijao']].sort_values(by= 'produtividade_feijao', ascending= False)

#GRÁFICO DE BARRAS
graf_media_feijao = px.bar(produtividade_media_feijao,
                          x = produtividade_media_feijao.index,
                          y = "produtividade_feijao",
                          title = "PRODUTIVIDADE MÉDIA MUNICIPAL DE FEIJÃO POR ESTADO")
graf_media_feijao.show()


# ### **Insights**
# 
# * O gráfico de dispensão indica `forte correlação positiva` entre as variáveis *produção total de feijao* e *área total destinada ao plantio de feijao*, mostrando que as duas variáveis tendem a diminuir ou aumentar juntas;
# * O estado com `maior` produtividade total de feijão foi o `Mato Grosso (MT)`, com produção média de `144.090,82 T/Ha`;
# * O estado com `menor` produtividade total de feijão não nula foi o `Pernambuco (PE)`, com produção média de `1.33 T/Ha`;
# * O estado com `maior` produtividade média municipal de feijão foi o `Piauí (PI)`, com produção de `1323,22 T/Ha`;
# * O estado com `menor` produtividade média municipal de feijão foi o `Pernambuco (PE)`, com produção de `0,16 T/Ha`.
