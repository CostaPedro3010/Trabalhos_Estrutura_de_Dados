import random

random.seed(0)

Lista = [random.randint(1, 100000)]

for i in range(1, 100000):
    x = random.randint(1, 100000)
    Lista.append(x)

