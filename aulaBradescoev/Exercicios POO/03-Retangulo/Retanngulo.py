class Retangulo:
    def __init__(self,largura,altura):
        self.altura=altura
        self.largura=largura
    def area(self):
        return self.largura*self.altura

    def perimetro(self):
        return (self.largura*2) + (self.altura*2)
