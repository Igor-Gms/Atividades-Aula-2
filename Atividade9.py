n = int(input("Digite um Numero Inteiro n (>= 0): "))

fatorial = 1

for i in range(1, n + 1):
    fatorial *= i

print(f"{n}! = {fatorial}")
