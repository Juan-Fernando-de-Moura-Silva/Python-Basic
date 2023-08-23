class Banco:
    def __init__(self):
        self.saldo = 0.0

    def realizar_deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Deposito realizado com sucesso!")
            print(f"Saldo atual: R$ {self.saldo:.2f}")
        elif valor == 0:
            print('Encerrando o programa...')
        else:
            print("Valor invalido! Digite um valor maior que zero.")

    def executar(self):
        print("Bem-vindo ao Banco!")
        while True:
            try:
                valor = float(input("Digite o valor do deposito: "))
                self.realizar_deposito(valor)
            except ValueError:
                print("Valor invalido! Digite um valor numerico.")
                continue
            continuar = input("Deseja realizar outro deposito? (S/N): ")
            if continuar.lower() != 's':
                print("Encerrando o programa...")
                break


banco = Banco()


banco.executar()
