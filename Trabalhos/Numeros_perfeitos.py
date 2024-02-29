soma = 0
n = int(input())
x = 1

while x <= n / 2:
    if n % 2 == 0:
        soma += x
    x += 1

if n == soma:
    print("sim")
else:
    print("não")
