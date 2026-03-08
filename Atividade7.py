print("=== Contador de Vogais ===")

frase = input("Escreva Uma Frase: ")
vogais = "aeiou"

total_vogais = 0

for i in range(len(frase)):
    if frase [i] in vogais:
        total_vogais += 1

print(f"O Total de Vogais na Frase é: {total_vogais}")