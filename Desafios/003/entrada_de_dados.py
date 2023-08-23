def realizar_saque(saldo_total, valor_saque):
    if saldo_total >= valor_saque:
        novo_saldo = saldo_total - valor_saque
        return f"Saque realizado com sucesso! Novo saldo: {novo_saldo}"
    else:
        return "Saldo insuficiente. Saque não realizado!"

# Exemplos de entrada e saída


exemplos = [
    (1000, 200),  # Saque realizado com sucesso! Novo saldo: 800
    (1500, 1800),  # Saldo insuficiente. Saque não realizado!
    (300, 200),   # Saque realizado com sucesso! Novo saldo: 100
]

for saldo_total, valor_saque in exemplos:
    resultado = realizar_saque(saldo_total, valor_saque)
    print(resultado)
