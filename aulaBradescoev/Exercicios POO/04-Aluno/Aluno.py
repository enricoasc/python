import random
class Aluno:
    def __init__(self):
        self.nome=''
        self.matricula = random.randint(102024001,102024999)
        self.notas=[]

    def lanca_nota(self,nota):
        if nota <0 or nota > 10:
            print('....: Nota invalida :....')
        else:
            self.notas.append(nota)
    def calc_media(self):
        total=0
        if len(self.notas) == 0:
            print('--------\n ...: Insira as notas :... ')
        else:
            qtd = len(self.notas)
            for i in range(len(self.notas)):
                total += self.notas[i]
            return total / qtd
    def resultado(self):
            if self.calc_media() >= 7:
                print('\n....: APROVADO COM A NOTA {:.2f} '.format(self.calc_media()))
            else:
                print('\n....: REPROVADO COM A NOTA {:.2f} '.format(self.calc_media()))

    def relatorio(self):
        print('''\n ---------------\nAluno : {0}
Matricula : {1}
Notas : {2}'''.format(self.nome,self.matricula,self.notas))