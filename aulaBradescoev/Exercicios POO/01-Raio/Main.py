from Circulo import Circulo
class Main:
    circ = Circulo(float(input('Digite o Raio do Circulo ..: ')))
    print('Seu Perímetro é ',circ.calc_perimetro(),' Sua área é ',circ.calc_area())

