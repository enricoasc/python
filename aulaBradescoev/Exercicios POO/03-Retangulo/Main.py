from Retanngulo import Retangulo
class Main:
    retangulo1 = Retangulo(float(input('Infome a Largura ..: ')),float(input('infome a Altura ..: ')))
    print('\nA área do retangulo é ',retangulo1.area())
    print('O perimetro do retangulo é ',retangulo1.perimetro())