texto = input("Informe um texto: ")
VOGAIS = "AEIOU"


# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()  # adiciona uma quebra de linha


# Exemplo utilizando a função built-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")

# Exemplo de uso da estrutura de repetição for em Python

# Iterando por uma lista
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterando por uma string
for letter in "hello":
    print(letter)

# Iterando por um intervalo numérico
for number in range(1, 6):  # O intervalo vai de 1 a 5 (6 não está incluído)
    print(number)

# Iterando com passos em um intervalo
for even_number in range(2, 11, 2):  # Números pares de 2 a 10
    print(even_number)

# Iterando por elementos de uma lista com índices
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Iterando por chave-valor em um dicionário
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")
