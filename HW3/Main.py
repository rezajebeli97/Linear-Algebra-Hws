import numpy as np

np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}".format(x)})

r = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n = len(r)

toeplitz = np.zeros((n, n))
for j in range(0, n):
    z = j
    for i in range(0, j):
        toeplitz[i][j] = r[z]
        z -= 1
    x = 0
    for i in range(j, n):
        toeplitz[i][j] = c[x]
        x += 1

print(toeplitz)
print("\n")

if toeplitz[0][0] == 0:
    for i in range(1, n):
        if toeplitz[i][0] != 0:
            toeplitz[[0, i]] = toeplitz[[i, 0]]
            break

for j in range(0, n):
    for i in range(j + 1, n):
        if toeplitz[i][j] != 0:
            for x in range(j, i):
                if toeplitz[x][j] != 0:
                    coef = toeplitz[i][j] / toeplitz[x][j]
                    toeplitz[i] -= coef * toeplitz[x]
                    break

print(toeplitz)

det = 1
for i in range(0, n):
    det *= toeplitz[i][i]

print(det)