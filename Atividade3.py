print("==== Contador de Números ====")

n = int(input("Digite um Número: "))

par = 0
impar = 0

for i in range(1, n+1):
    if i % 2 == 0:
        par += 1

    else:
        impar += 1

print(f"Quantidade de Números impares {impar}")
print(f"Quantidade de Números Pares {par}")
