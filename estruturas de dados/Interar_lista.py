carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

frutas = ["maçã", "banana", "laranja"]
for i in range(len(frutas)):
    print(frutas[i])

frutas = ["maçã", "banana", "laranja"]
for i, fruta in enumerate(frutas):
    print(f"Índice {i}: {fruta}")

frutas = ["maçã", "banana", "laranja"]
[print(fruta) for fruta in frutas]
