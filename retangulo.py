class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

if __name__ == "__main__":
    r = Retangulo(5, 3)
    print("Área:", r.area())
    print("Perímetro:", r.perimetro())