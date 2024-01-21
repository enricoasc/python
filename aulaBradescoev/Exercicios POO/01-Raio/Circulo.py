class Circulo:
    def __init__(self,raio):
        self._raio=raio
        self._pi = 3.14
    def calc_area(self):
        return self._pi * (self._raio ** 2)

    def calc_perimetro(self):
        return 2*self._pi * self._raio

