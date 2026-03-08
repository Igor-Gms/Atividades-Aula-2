n = int(input("Digite um Número : "))

pares = 0

for i in range(1, n+1):
    if i % 2 == 0:
        pares += 1
        print(f"Quantidade de Números Pares: {pares}")