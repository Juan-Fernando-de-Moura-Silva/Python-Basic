while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue

    print(numero)

# Exemplo de uso do comando break em uma estrutura de repetição

# Usando break para sair de um loop while quando um valor é encontrado
search_number = 5
counter = 0

while counter <= 10:
    if counter == search_number:
        print(f"Valor {search_number} encontrado!")
        break
    print(counter)
    counter += 1
else:
    print("Valor não encontrado no loop while.")

# Usando break para sair de um loop for quando um valor é encontrado
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == search_number:
        print(f"Valor {search_number} encontrado!")
        break
    print(num)
else:
    print("Valor não encontrado no loop for.")
# for numero in range(100):

#     if numero % 2 == 0:
#         continue

#     print(numero, end=" ")
