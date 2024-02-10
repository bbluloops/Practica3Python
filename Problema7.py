import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Cuadrante 1"
        elif self.x < 0 and self.y > 0:
            return "Cuadrante 2"
        elif self.x < 0 and self.y < 0:
            return "Cuadrante 3"
        elif self.x > 0 and self.y < 0:
            return "Cuadrante 4"
        elif self.x == 0 and self.y != 0:
            return "Sobre el eje Y"
        elif self.x != 0 and self.y == 0:
            return "Sobre el eje X"
        else:
            return "Origen"

    def vector(self, otro_punto):
        return Punto(otro_punto.x - self.x, otro_punto.y - self.y)

    def distancia(self, otro_punto):
        return math.sqrt((otro_punto.x - self.x)**2 + (otro_punto.y - self.y)**2)


class Rectangulo:
    def __init__(self, punto1=Punto(), punto2=Punto()):
        self.punto1 = punto1
        self.punto2 = punto2

    def base(self):
        return abs(self.punto2.x - self.punto1.x)

    def altura(self):
        return abs(self.punto2.y - self.punto1.y)

    def area(self):
        return self.base() * self.altura()

p1 = Punto(3, 4)
p2 = Punto(-2, 5)

print("Coordenadas del punto p1:", p1)
print("Coordenadas del punto p2:", p2)
print("Cuadrante del punto p1:", p1.cuadrante())
print("Cuadrante del punto p2:", p2.cuadrante())
print("Vector entre p1 y p2:", p1.vector(p2))
print("Distancia entre p1 y p2:", p1.distancia(p2))

rect = Rectangulo(p1, p2)
print("Base del rectángulo:", rect.base())
print("Altura del rectángulo:", rect.altura())
print("Área del rectángulo:", rect.area())
