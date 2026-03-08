texto = input("Digite um texto: ")
caractere_procurado = input("Digite o caractere que deseja contar: ")

contador = 0

caractere_procurado = caractere_procurado.lower()

for letra in texto:
    if letra.lower() == caractere_procurado:
        contador += 1

print(f"O caractere '{caractere_procurado}' aparece {contador} vezes no texto.")