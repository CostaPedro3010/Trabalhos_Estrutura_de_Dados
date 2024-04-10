import random

random.seed(0)

Lista = [random.randint(1, 100000)]

for i in range(1, 100000):
    x = random.randint(1, 100000)
    Lista.append(x)
print(Lista)
Lista.sort()
print(Lista)

repetidos = 0
menor = maior = Lista[0]

for i in range(1, len(Lista)):
    if Lista[i] == Lista[i - 1]:
        repetidos += 1
    if Lista[i] > maior:
        maior = Lista[i]
    if Lista[i] < menor:
        menor = Lista[i]

print("Repetidos: ", repetidos)
print("Maior: ", maior)
print("Menor: ", menor)