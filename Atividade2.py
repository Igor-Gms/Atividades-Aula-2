limite = int(input("Defina Um Limite: "))

soma = 0

for i in range(1, limite+1):
    soma = soma + i
    print(f"A Soma de Todos Os Números Até {limite} é: {soma}")
    