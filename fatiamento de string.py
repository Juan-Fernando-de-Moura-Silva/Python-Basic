# Exemplo de uso do fatiamento de strings

text = "Hello, world!"

# Obtendo os primeiros 5 caracteres da string
substring1 = text[:5]
print(substring1)  # Saída: "Hello"

# Obtendo os caracteres a partir do índice 7 até o final da string
substring2 = text[7:]
print(substring2)  # Saída: "world!"

# Obtendo os caracteres do índice 7 até o índice 11 (não incluso)
substring3 = text[7:11]
print(substring3)  # Saída: "worl"

# Obtendo os últimos 6 caracteres da string
substring4 = text[-6:]
print(substring4)  # Saída: "world!"

# Obtendo os caracteres do índice -13 até o índice -9 (não incluso)
substring5 = text[-13:-9]
print(substring5)  # Saída: "Hello"

# Obtendo os caracteres o espelhamento dos caracteres
substring6 = text[::-1]
print(substring6)  # Saída: "!dlrow ,olleH"
