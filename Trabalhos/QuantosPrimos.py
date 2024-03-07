
numDigitado = int(input())
contadorPrimos = 0
contadorDivisores = 1

while (numDigitado != 0):
    contadorDivisores = 1

    if (numDigitado == 0):
        print(contadorPrimos)

    while contadorDivisores < numDigitado:
        if numDigitado % contadorDivisores == 0:
            contadorDivisores += 1

    if (contadorDivisores == 2):
        contadorPrimos += 1

    numDigitado = int(input())

print(contadorPrimos)

#
#
# contadorPrimos = 0
#
# numDigitado = int(input("Digite um número (ou zero para encerrar): "))
#
# while numDigitado != 0:
#     if numDigitado >= 2:
#         primo = 1
#         contadorDivisores = 2
#
#         while contadorDivisores <= numDigitado:
#             if numDigitado % contadorDivisores == 0:
#                 primo = 0
#             contadorDivisores += 1
#
#         contadorPrimos += primo
#
#     numDigitado = int(input("Digite um número (ou zero para encerrar): "))
#
# print("Quantidade de números primos digitados:", contadorPrimos)