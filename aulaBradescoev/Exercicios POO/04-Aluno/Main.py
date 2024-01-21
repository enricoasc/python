from Aluno import Aluno
class Main:
    opc=''
    while opc.upper() != 'SAIR':
        opc=input('''\nSistema de alunos, digite a opção desejada :
        1- Criar aluno 
        2- Lançar nota
        3- Verificar Resultado 
        4- Relatorio
        ou digite "sair" para finalizar o sistema .: ''')

        if opc == '1':
            novo_aluno=Aluno()
            novo_aluno.nome = input('------\nNome no Aluno :')

        elif opc== '2':
            novo_aluno.lanca_nota( float(input('------\nDigite o numero da nota de [0.0] a [10.0] .: ')) )

        elif opc=='3':
            novo_aluno.resultado()

        elif opc=='4':
            novo_aluno.relatorio()

        elif opc.upper()  =='SAIR':
            print(':... Finalizando sistema Aluno ...:')
        else:
            print(':... Opção Invalida ! ...:')

