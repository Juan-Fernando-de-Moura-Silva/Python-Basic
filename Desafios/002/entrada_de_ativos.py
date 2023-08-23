def main():
    try:
        # Solicita a quantidade de ativos
        quantidade_ativos = int(input("Digite a quantidade de ativos: "))

        # Cria uma lista para armazenar os ativos
        ativos = []

        # Solicita os tipos de ativos e os adiciona à lista
        for _ in range(quantidade_ativos):
            tipo_ativo = input("Digite o tipo do ativo: ")
            ativos.append(tipo_ativo)

        # Organiza a lista de ativos em ordem alfabética
        ativos.sort()

        # Exibe a lista de ativos organizada
        print("Ativos organizados:")
        for ativo in ativos:
            print(ativo)

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar um número inteiro" +
              "para a quantidade de ativos.")


if __name__ == "__main__":
    main()
