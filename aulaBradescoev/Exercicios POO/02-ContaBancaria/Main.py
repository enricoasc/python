from ContaBancaria import ContaBancaria
class Main:
    opc = 1
    while opc != 0:
        opc = (input('''\nOlá, digite (1) para acessar as opções do Banco ou (0) para sair do sistema.: '''))
        if opc == '1':
            opc2 = (input('''
  - (0) para Sair
  - (1) para Abrir conta
  - (2) para Deposito 
  - (3) para Saque 
  - (4) para Saldo
Opção .: '''))
            if opc2 == '1':
                titular = input('\n ------------ \n Digite o nome do titular.: ')
                num_conta = input('\n ------------ \n Digite o numero da conta.: ')
                nova_conta = ContaBancaria(num_conta,titular)

            elif opc2 == '2':
                nova_conta.deposita(float(input('\n ------------ \n Digite o valor de Depósito .: ')))

            elif opc2 == '3':
                nova_conta.sacar(float(input('\n ------------ \n Digite o valor de Saque .: ')))

            elif opc2 == '4':
                nova_conta.saldo_titular()
        elif opc == '0':
            print('\n\n...: OBRIGADO POR USAR ESSE BANCO , ATÉ MAIS ! ..:\n\n ')
        else :
            print('Opção Invalida , tente outra vez ..: ')