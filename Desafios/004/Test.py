def calcular_juros_compostos(valor_inicial, taxa_juros, periodo):
    valor_final = valor_inicial * (1 + taxa_juros) ** periodo
    return round(valor_final, 2)


exemplos = [
    (5000, 0.08, 5),   # Valor final do investimento: R$ 7346.64
    (1000, 0.06, 3),   # Valor final do investimento: R$ 1191.02
    (20000, 0.04, 10)  # Valor final do investimento: R$ 29604.89
]

for valor_inicial, taxa_juros, periodo in exemplos:
    valor_final = calcular_juros_compostos(valor_inicial, taxa_juros, periodo)
    print(f"Valor final do investimento: R$ {valor_final:.2f}")
