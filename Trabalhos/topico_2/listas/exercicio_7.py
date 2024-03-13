l = int(input())
c = int(input())

f = 0

n = []

for i in range(l):
    for j in range(c):
        if n[i][j] != 0:
            f = 1
if f == 0:
    print("matriz nula")
