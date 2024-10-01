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
import matplotlib.pyplot as plt
import seaborn as sns

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
        return contar_nulos

    # contagem de valores unicos
    def valor_unico(self):    
        valores_unicos = self.df.nunique()
        return valores_unicos

    # contagem de colunas categóricas
    def nao_numericos(self):
        categorico = self.df.select_dtypes(include = 'object').describe()
        return categorico


    # descrição de valores de colunas numéricas 
    def descricao_dados(self):
        df_descricao = self.df.select_dtypes(include = np.number).describe().round(2)
        return df_descricao

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

# gráfico de distribuição de colunas categóricas x numérica
    def categorica_x_numerica(self):
     
        column_numeros = self.df.select_dtypes(include=[np.number]).columns
        column_categorias = self.df.select_dtypes(include=['object']).columns

        classificadata = pd.DataFrame({
            'Tipo de Coluna': ['Numéricas', 'Categóricas'],
            'Colunas': [', '.join(column_numeros), ', '.join(column_categorias)]
        })

        print("Distribuição de Colunas Numéricas e Categóricas:")
        print(classificadata)


# gráfico de distribuição de colunas numéricas x colunas categóricas 
    def distribuicao_dados(self):

        numericos = len(self.df.select_dtypes(include=np.number).columns)
        categoricos = len(self.df.select_dtypes(include = "object").columns)

        labels = ['Numéricas', 'Não Numéricas']
        sizes = [numericos, categoricos]  

        def sem_porcentagem(val):
          a = int(np.round(val / 100 * sum(sizes)))  # Converte porcentagem para valor absoluto
          return f'{a} colunas'

        plt.figure(figsize=(6,6))
        plt.pie(sizes, labels=labels, autopct=sem_porcentagem, startangle=90, colors=['skyblue', 'grey'], wedgeprops=dict(width=0.6))
        plt.title('Quantidade de colunas por tipo')
        plt.axis('equal')  
        plt.show()


# gráfico de nulos
    def nulos(self):
       
        nulls = self.valornulo()
        nulls = nulls[nulls > 0]
        if nulls.empty:
            print("Não existem colunas com valores nulos")
            return
        
        plt.figure(figsize=(10,6))
        sns.barplot(x = nulls.index, y = nulls.values, width=0.1)
        plt.title("Valores nulos por coluna")
        plt.ylabel("Nº de valores nulos")
        plt.xlabel("Colunas")
        plt.xticks(rotation=45)
        plt.show()


