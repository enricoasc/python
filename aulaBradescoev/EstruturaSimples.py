A = input("Informe um valor para a variável A: ")
B = input("Informe um valor para a variável B: ")

if (A>B):
    aux=A;
    A=B;
    B=aux;

print('O valor da variavel A agora é : ',A);
print('O valor da variavel B agora é : ',B);


# ------------------

idade = int(input('Digite a idade da pessoa: '))

if idade > 18:
    print('Maior Idade')
else:
    print("Menor Idade")