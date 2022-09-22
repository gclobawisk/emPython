def DecimalToBinario(decimal):
    restos = ''
    dividendo = decimal
    while True:
        if decimal == 0:
            return 0
        elif decimal == 1:
            return 1
        elif dividendo < 2:
            break
        else:
            print(dividendo)
            resultado = int(dividendo / 2)
            restoDivisao = dividendo % 2
            restos = str(restoDivisao) + restos
            dividendo = resultado

    restos = str(resultado) + restos
    return int(restos)


binario = DecimalToBinario(45)
print(f"em Binário: {binario}")


