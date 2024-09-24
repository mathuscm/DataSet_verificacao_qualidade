'''Crie seu dataquality
Utilizando de POO, crie um módulo que importado para um jupyter notebook crie um relatório como no pandas-profiling/YData-profiling/SweetViz.

Neste módulo, tera um método geral para análise de qualquer dataset:

Contagem de nulos
Contagem de valores únicos
.value_counts em colunas categóricas
.describe nas colunas numéricas
gráficos de distribuição de colunas categóricas
gráficos de distribuição de colunas numéricas
...'''

#-----------------------------------------------------------------------#
# importar bibliotecas pandas, numpy, matplotlib.pyplot
# usar a sigla 'df' como padrão (será aplicado para qualquer arquivo que subir)
# algumas variáveis estão direcionadas a colunas específicas, caso utilizado esta parte do script, as colunas devem ser renomedas para não quebrar o código


#
import pandas as pd 
import numpy as np 

#
'''class ItegridadeDados:
    def __init__(self, df):
        df = self.df'''


# 
df = pd.read_csv('caminho-do-seu-arquivo-aqui.csv', sep = ',')
print(df)

# coluna de ano pode ser uma string, não há necessidade de manipulação
df['Year'] = df['Year'].astype(str)

# filtro para contagem de nulos
def valornulo(df):
    contar_nulos = df.isnull().sum()

# contagem de valores unicos
def valor_unico(df):    
    valores_unicos = df.nunique()

# contagem de colunas categóricas


# descrição de valores de colunas numéricas 
def descricao_dados(df):
    df_descricao = df.describe()
    print(df_descricao)

# gráfico de distribuição de colunas categóricas


# gráfico de distribuição de colunas numéricas
    

# chamando funções
vunico = valor_unico(df)
print(vunico)

vnulo = valornulo(df['Previous Year Rank'])
print(vnulo)

vdescricao = descricao_dados(df)
print(vdescricao)

# considerar valores NaN como 0
#df['Previous Year Rank'] = df['Previous Year Rank'].fillna(0).astype(int)
#print(df)




#print(df['Previous Year Rank']).nunique()

#consulta = df[(df['Current Rank'] == 0) | (df['earnings ($ million)'] == 0) | (df['Previous Year Rank'])]
#print(consulta)

# tipagem das colunas
#tipo_1 = df['earnings ($ million)'].dtype
#print(tipo_1)

#tipo_2 = df['Previous Year Rank'].dtype
#print(tipo_2)    