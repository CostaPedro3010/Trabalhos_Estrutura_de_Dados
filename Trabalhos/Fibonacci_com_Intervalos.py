limite_inicial = int(input())
limite_final = int(input())

a, b = 0, 1


while a <= limite_final:
    if a >= limite_inicial:
        print(a)
    proximo_numero = a + b
    a, b = b, proximo_numero