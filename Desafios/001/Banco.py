def main():
    try:
        saldo_atual = float(input("Digite o saldo atual: "))

        deposito = float(input("Digite o valor do depósito: "))

        saque = float(input("Digite o valor do saque: "))

        saldo_final = saldo_atual + deposito - saque

        print(f"Saldo final: {saldo_final:.2f}")

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números válidos.")


if __name__ == "__main__":
    main()
