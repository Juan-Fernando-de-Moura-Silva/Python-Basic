valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

# TODO: Iterar, baseado no período em anos,
# para calculo do valorFinal com os juros.


def calcular_juros_compostos(valor_inicial, taxa_juros, periodo):
    valor_final = valor_inicial * (1 + taxa_juros) ** periodo

    print("Valor final do investimento: R$", round(valor_final, 2))
    return round(valor_final, 2)


calcular_juros_compostos(valor_inicial, taxa_juros, periodo)
