saldo = 2000
saque = 2500

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")

# Exemplo de uso da expressão condicional ternária

# Usando a expressão condicional ternária
# para determinar se um número é par ou ímpar
number = 10

parity = "par" if number % 2 == 0 else "ímpar"
print(f"O número {number} é {parity}.")

# Usando a expressão condicional ternária para
# verificar se um número é positivo, negativo ou zero
number = -5

sign = "positivo" if number > 0 else "negativo" if number < 0 else "zero"
print(f"O número {number} é {sign}.")
