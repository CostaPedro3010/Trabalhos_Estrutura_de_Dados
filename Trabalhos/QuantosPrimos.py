
# i = 1
# totPrimo = 0
# numPrimo = int(input())
# if numPrimo == 0 or numPrimo == 1:
#     print(0)
# while numPrimo > 1:
#     numDivisores = 0
#     while numPrimo >= i:
#         if numPrimo % i == 0:
#             numDivisores += 1
#         i += 1
#     if numDivisores == 2:
#         totPrimo += 1
#     if numPrimo == 0:
#         break
#     numPrimo = int(input())
# print(totPrimo)

i = 1
tot_primo = 0

# Loop principal
while True:
    # Obtenha o próximo número a ser verificado
    num = int(input("Digite um número natural positivo (0 para encerrar): "))

    # Verifique se o número é primo
    if num > 1:
        # Inicialize a contagem de divisores
        num_divisores = 0
        # Verifique a divisibilidade de cada número a partir de 2
        for j in range(2, num):
            if num % j == 0:
                num_divisores += 1
                break
        # Se o número tiver apenas 2 divisores, ele é primo
        if num_divisores == 1:
            tot_primo += 1
    elif num == 0:
        # Se 0 for digitado, encerre o loop principal
        break

# Exiba a contagem de números primos
print("A quantidade de números primos digitados foi:", tot_primo)