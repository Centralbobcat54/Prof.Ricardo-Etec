# 2.1 🏞️ Problema “terreno”
largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))
valor_metro = float(input("Digite o valor do metro quadrado: "))
area = largura * comprimento
preco = area * valor_metro
print(f"Area do terreno = {area:.2f}")
print(f"Preco do terreno = {preco:.2f}")

# 2.2 🖼️ Problema “retangulo”
import math
base = float(input("Base do retangulo: "))
altura = float(input("Altura do retangulo: "))
area = base * altura
perimetro = 2 * (base + altura)
diagonal = math.sqrt(base ** 2 + altura ** 2)
print(f"AREA = {area:.4f}")
print(f"PERIMETRO = {perimetro:.4f}")
print(f"DIAGONAL = {diagonal:.4f}")

# 2.3 🧑‍🤝‍🧑 Problema “idades”
print("Dados da primeira pessoa:")
nome1 = input("Nome: ")
idade1 = int(input("Idade: "))
print("Dados da segunda pessoa:")
nome2 = input("Nome: ")
idade2 = int(input("Idade: "))
media = (idade1 + idade2) / 2
print(f"A idade média de {nome1} e {nome2} é de {media:.1f} anos")

# 2.4 ➕ Problema “soma”
x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))
soma = x + y
print(f"SOMA = {soma}")

# 2.5 💸 Problema “troco”
preco = float(input("Preço unitário do produto: "))
quantidade = int(input("Quantidade comprada: "))
dinheiro = float(input("Dinheiro recebido: "))
total = preco * quantidade
troco = dinheiro - total
print(f"TROCO = {troco:.2f}")

# 2.6 ⭕ Problema “circulo”
r = float(input("Digite o valor do raio do circulo: "))
area = math.pi * r ** 2
print(f"AREA = {area:.3f}")

# 2.7 💰 Problema “pagamento”
nome = input("Nome: ")
valor_hora = float(input("Valor por hora: "))
horas = int(input("Horas trabalhadas: "))
pagamento = valor_hora * horas
print(f"O pagamento para {nome} deve ser {pagamento:.2f}")

# 2.8 🚗 Problema “consumo”
distancia = float(input("Distancia percorrida: "))
combustivel = float(input("Combustível gasto: "))
consumo = distancia / combustivel
print(f"Consumo medio = {consumo:.3f}")

# 2.9 📏 Problema “medidas”
a = float(input("Digite a medida A: "))
b = float(input("Digite a medida B: "))
c = float(input("Digite a medida C: "))
quadrado = a ** 2
triangulo = (a * b) / 2
trapezio = ((a + b) * c) / 2
print(f"AREA DO QUADRADO = {quadrado:.4f}")
print(f"AREA DO TRIANGULO = {triangulo:.4f}")
print(f"AREA DO TRAPEZIO = {trapezio:.4f}")

# 2.10 ⏱️ Problema “duracao”
tempo = int(input("Digite a duracao em segundos: "))
horas = tempo // 3600
minutos = (tempo % 3600) // 60
segundos = tempo % 60
print(f"{horas}:{minutos}:{segundos}")
