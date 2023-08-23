# Entrada de dados
saldo_total = int(input())
valor_saque = int(input())

# TODO: Criar as condições necessárias para impressão da saída,
# vide tabela de exemplos.


def realizar_saque(saldo_total, valor_saque):
    if saldo_total >= valor_saque:
        novo_saldo = saldo_total - valor_saque
        print(f"Saque realizado com sucesso. Novo saldo: {novo_saldo}")
        return f"Saque realizado com sucesso. Novo saldo: {novo_saldo}"
    else:
        print("Saldo insuficiente. Saque nao realizado!")
        return "Saldo insuficiente. Saque nao realizado!"


realizar_saque(saldo_total, valor_saque)
