base = int(input("Digite o Número Base: "))
limite = int(input("Digite o Valor Limite: "))

print(f"Múltiplos De {base} Entre 1 E {limite}:")

for i in range(base, limite + 1, base):
    print(i)