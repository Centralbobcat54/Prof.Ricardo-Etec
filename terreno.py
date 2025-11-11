class Terreno:
    def __init__(self, largura, comprimento):
        self.largura = largura
        self.comprimento = comprimento

    def area(self):
        return self.largura * self.comprimento

if __name__ == "__main__":
    terreno = Terreno(10, 20)
    print("Área do terreno:", terreno.area())