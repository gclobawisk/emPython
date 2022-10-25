n = int(input("Digite um número: "))
for i in range(1, n+1):
    divisores = 0
    for j in range(1, n+1):
        if i % j == 0:
            divisores = divisores + 1

    if divisores <= 2 and i != 1:
        print (f"{i} é Primo")