# exemplo 1 #
name = "Alice"
age = 30
message = f"My name is {name} and I am {age} years old."
print(message)
# Saída: "My name is Alice and I am 30 years old."

# exemplo 2 #
name = "Bob"
age = 25
message = "My name is {} and I am {} years old.".format(name, age)
print(message)
# Saída: "My name is Bob and I am 25 years old."

# exemplo 3 #
name = "Charlie"
age = 40
message = "My name is %s and I am %d years old." % (name, age)
print(message)
# Saída: "My name is Charlie and I am 40 years old."

# exemplo 4 #
name = "David"
age = 28
message = "My name is " + name + " and I am " + str(age) + " years old."
print(message)
# Saída: "My name is David and I am 28 years old."
