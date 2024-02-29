a = 0
b = 1

i = 1
print(a)
while i < 10:
    i += 1
    a, b = b, a + b
    print(a)
