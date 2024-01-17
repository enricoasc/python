def lernotas():
    n=float(input('Digite uma nota para o aluno: '))
    return n

def resultado(n1,n2):
    media=(n1+n2)/2
    print("Nota 1: %.2f"%n1)
    print("Nota 2: %.2f" % n2)
    print('Media: %.2f' %media,' Resultado: ',end='')
    if media >= 7:
        print('Aprovado')
    else:
        print('Reprovado')

a = lernotas()
b = lernotas()
resultado(a,b)