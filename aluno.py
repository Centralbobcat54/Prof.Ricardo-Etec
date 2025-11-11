class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        return (self.nota1 + self.nota2) / 2

    def situacao(self):
        return "Aprovado" if self.media() >= 6 else "Reprovado"

if __name__ == "__main__":
    aluno = Aluno("Maria", 7.5, 8.0)
    print(aluno.nome, "-", aluno.situacao())