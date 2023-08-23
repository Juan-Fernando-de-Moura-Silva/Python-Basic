def main():
    try:
        quantidade_ativos = int(input("Digite a quantidade de ativos: "))

        ativos = []
        for _ in range(quantidade_ativos):
            tipo_ativo = input("Digite o tipo do ativo: ")
            ativos.append(tipo_ativo)

        # Remove entradas numéricas da lista de ativos
        ativos = [ativo for ativo in ativos if not ativo.isdigit()]

        # Organiza a lista de ativos em ordem alfabética
        ativos.sort()

        # Exibe a lista de ativos organizados
        print("Ativos organizados:")
        for ativo in ativos:
            print(ativo)

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar um número inteiro "
              + "para a quantidade de ativos.")


if __name__ == "__main__":
    main()
