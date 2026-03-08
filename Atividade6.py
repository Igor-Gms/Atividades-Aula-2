qnt = int(input("Quantas Notas Deseja Digitar: "))

soma_notas = 0

for i in range(1, qnt + 1):
    while True:
        nota = float(input(f"Digite a Nota {i} (0 a 10): "))
        if 0 <= nota <= 10:
            break
        else:
            print("Nota Invalida! Digite Um Valor de 0 a 10.")

    soma_notas = soma_notas + nota

media = soma_notas / qnt

print(f"A Média Final Das {qnt} Notas é: {media:.2f}")