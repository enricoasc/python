qtd = 0
soma = 0
media = 0
valor = float(input('Digite um valor: '))

while valor>0.0 :
    soma = soma + valor
    qtd = qtd +1
    # entrada de valores
    valor = float(input('Digite um valor '))

# caso digite um valor negativo  o laço encerra
media = soma / qtd
print('\n Total da Soma: %.2f'%soma)
print('\n Quantidade de valroes digitados: %i'%qtd)
print('\n Média dos valores: %.2f'%media)