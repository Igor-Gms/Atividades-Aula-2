numero_str = input("Digite um Número Inteiro Positivo: ")

soma = 0

for digito in numero_str:
    soma += int(digito)

print(f"A Soma Dos Digitos De {numero_str} É: {soma}")

