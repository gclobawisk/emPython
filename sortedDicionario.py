import random

resultados = {}
for i in range(1,6):
    x = random.randint(1, 10)
    resultados[f'jogador{i}'] = x

for i in sorted(resultados, key = resultados.get, reverse=True):
    print(f'{i}: {resultados[i]} pontos')