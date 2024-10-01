## Script base para validação de dados

Modelo de script desenvolvido para validar e verificar aspectos pontuais de um dataset antes da fase de manipulação para análise.
Este script contém funções para verificar: 

- a tipagem dos dados por coluna (numérica ou categórica), 
- a existência de valores nulos,
- a quantidade de valores únicos, 
- a descrição de dados numéricos (.describe()),
- a descrição dos valores categóricos,
- gráfico de rosca comparando quantidade de numéricos x categóricos,
- gráfico de barras para contagem de valores nulos por coluna.
- gráfico tabela de tipagem de dados e as colunas encontradas em cada uma

O script tem uma estrutura projetada para uso amplo e não para um arquivo em específico, podendo ser modularizado. O arquivo principal script_qualificacao_dados.py acompanha o arquivo modulos.ipynb que é responsável por chamar as funções existentes no arquivo principal (seja integral ou por partes).

Este repositório contém dois aqruivos .csv para teste do código, mas pode ser qualquer outro. 

## Modo de uso

1. clone ou baixe o repositório,
2. os arquivos script_qualificacao_dados.py e modulos.ipynb devem estar no mesmo local/pasta, assim como o arquivo .csv que será lido pelo programa,
3. caso deseje realizar a leitura de outro .csv que não seja os dado como exemplo, cole ele na mesma pasta em que os arquivos da instrução 2,
4. após selecionar e armazenar o arquivo na pasta, você pode alterar o caminho dele na seguinte linha do arquivo modulos.ipynb: df = pd.read_csv('caminho-do-seu-arquivo-aqui.csv', sep = ','),
5. execute o arquivo script_qualificacao_dados.py,
6. depois, execute o arquivo modulos.ipynb, pois ele irá gerar a saída

## Bibliotecas necessárias

- pip install pandas
- pip install numpy
- pip install matplotlip.pyplot
- pip install seaborn

