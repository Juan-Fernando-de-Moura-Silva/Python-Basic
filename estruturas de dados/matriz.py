matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz)
print(matriz[0])  # [1, "a", 2]
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"

# Matriz de tuplas #

matriz_tupla = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz_tupla[0])  # (1, "a", 2)
print(matriz_tupla[0][0])  # 1
print(matriz_tupla[0][-1])  # 2
print(matriz_tupla[-1][-1])  # "c"
