class ContaBancaria:
    def __init__(self,numero,titular):
        self.numero = numero
        self.titular = titular
        self.saldo =0

    def deposita(self,valor):
        self.saldo += valor
        print('...: Depositado com sucesso ..:')

    def sacar(self,valor):
        if self.saldo>=valor:
            self.saldo-=valor
            print('...: Saque realizado com sucesso ..:')
        else:
            print('...: Saldo insuficiente para saque ..:')


    def saldo_titular(self):
        print('''\n------------------
Titular .: {0}
Conta   .: {1}
Saldo   .: {2:.2f} 
-------------------'''.format(self.titular,self.numero,self.saldo))