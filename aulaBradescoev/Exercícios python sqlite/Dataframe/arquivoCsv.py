import pandas as pd

autor = ['sun tzu','Fernando Pessoa','thomas Mann', 'João Guimarães Rosa']
livro = ['a arte da guerra','poesias selecionadas','a montanha mágica', 'Primeiras Estórias']
ano = [2000,2004,2015,2017]

dados = {
    'Autor': autor,
    'Livro': livro,
    'Ano': ano
}

# print(type(dados))
df = pd.DataFrame(dados)
# print(type(df))
# print((df))

df.to_csv('autores.csv')

autores = pd.read_csv('autores.csv',index_col=0)
# print(autores.head())
# print(autores.info)
# print(autores.columns)
# print(autores.index)

casas = pd.read_csv('california_housing_train.csv')
print(casas.head())
print(casas.describe())
# print(casas.columns)
# print(casas.index)