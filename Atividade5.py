qnt = int(input("Quantos Numeros Você Deseja Digitar: "))

maior = 0
menor = 0

for i in range(1, qnt+1):
    num = int(input(f"Digite o {i}º Número: "))
    if i == 1:
        maior = num
        menor = num

    else:
        if num > maior:
            maior = num

        if num < menor:
            menor = num

print(f"O Maior Número Digitado Foi: {maior}")
print(f"O Menor Número Digitado Foi: {menor}")
