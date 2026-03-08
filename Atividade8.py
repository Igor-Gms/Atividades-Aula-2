texto = input("Digite um Texto: ")

texto_invertido = ""

for i in range(len(texto) -1, -1, -1):
    texto_invertido += texto[i]

print("Texto Original:", texto)
print("Texto Invertido:", texto_invertido)

