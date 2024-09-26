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


# coluna de ano pode ser uma string, não há necessidade de manipulação
#df['Year'] = df['Year'].astype(str)

#
class IntegridadeDados:
    def __init__(self, data):
        self.df = data

# filtro para contagem de nulos
    def valornulo(self):
        contar_nulos = self.df.isnull().sum()
        print(contar_nulos)

    # contagem de valores unicos
    def valor_unico(self):    
        valores_unicos = self.df.nunique()
        print(valores_unicos)

    # contagem de colunas categóricas
    def nao_numericos(self):
        categorico = self.df.select_dtypes(include = 'object').describe()
        print(categorico)


    # descrição de valores de colunas numéricas 
    def descricao_dados(self):
        df_descricao = self.df.select_dtypes(include = np.number).describe().round(2)
        print(df_descricao)

    # função de análise geral
    def analise_geral(self):
        print("\nVALORES NULOS POR COLUNA\n")
        self.valornulo()
        print("\nVALORES ÚNICOS POR COLUNA\n")
        self.valor_unico()
        print('\nDESCRIÇÃO DOS DADOS NÃO NUMÉRICOS\n')
        self.nao_numericos()
        print('\nDESCRIÇÃO DOS DADOS NUMÉRICOS - MIN, MAX, MEDIA, MODA E QUARTIS\n')
        self.descricao_dados()

# gráfico de distribuição de colunas categóricas


# gráfico de distribuição de colunas numéricas

df = pd.read_csv('Atletas-ricos.csv', sep = ',')
print(df)   

# chamando funções
resumo_dados = IntegridadeDados(df)
resumo_dados.analise_geral()
#print(resumo_dados)

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