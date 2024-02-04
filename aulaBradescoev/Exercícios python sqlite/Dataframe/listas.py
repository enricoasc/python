import pandas as pd

nome_cidade = pd.Series(['Maringa','Uberaba','Araxá'])
população = pd.Series([403.256,120.589,699.458])

data = pd.DataFrame({'Cidades' : nome_cidade, 'População': população})
# print(data)

cidades = ['Maringá','Itabira','Uberlândia','Salvado','Fortaleza']
populacao = [403.063,120.904,699.097,2.886698,2.686612]

populacao_cidade = dict( zip(cidades,populacao) )
print((populacao_cidade))
print(type(populacao_cidade))
print(populacao_cidade['Uberlândia'])
print('Maringá' in populacao_cidade)

populacao_cidade['Vitória']= 365.898
print(populacao_cidade)

del populacao_cidade['Fortaleza']
print(populacao_cidade)
