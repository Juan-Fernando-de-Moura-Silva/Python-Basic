saldo_atual = float(input())
valor_deposito = float(input())
valor_retirada = float(input())


def Calculo_de_conta(saldo_atual, valor_deposito, valor_retirada):
    saldo_final = saldo_atual + valor_deposito - valor_retirada
    print(f"Saldo atualizado na conta: {saldo_final}")
    return saldo_final


Calculo_de_conta(saldo_atual, valor_deposito, valor_retirada)
