qtd = int(input("Quantos números deseja digitar? "))

soma = 0
maior = None
menor = None
positivos = 0
negativos = 0
zeros = 0

for i in range(qtd):
    num = float(input(f"Digite o {i+1}º número: "))
    
    # Acumular a soma
    soma += num
    
    if maior is None or num > maior:
        maior = num
    if menor is None or num < menor:
        menor = num
        
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        zeros += 1

media = soma / qtd if qtd > 0 else 0

# Passo 5: Exibir resultados
print("\n--- Resultados ---")
print(f"Soma total: {soma}")
print(f"Média: {media:.2f}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Zeros: {zeros}")
