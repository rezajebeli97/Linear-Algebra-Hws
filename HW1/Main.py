import numpy as np

n = 6 # number of values and constraints
A = [ [3.0, -2.0, 0.0, 0.0, 0.0, 0.0],
      [-2.0, 3.0, -2.0, 0.0, 0.0, 0.0],
      [0.0, -2.0, 0.6666666666667, -2.0, 0.0, 0.0],
      [0.0, 0.0, -2.0, 3.0, -2.0, 0.0],
      [0.0, 0.0, 0.0, -2.0, 3.0, -2.0],
      [0.0, 0.0, 0.0, 0.0, -2.0, 3.0]]

b = [ [1.0, -1.0, -3.33333333333, -1.0, -1.0, 1.0] ]
b = np.transpose(b)

A_add = np.concatenate([A, b], axis=1)

print(A_add)
print()

np.set_printoptions(formatter={'float': lambda  x: "{0:0.2f}".format(x)})

for i in range(0, n):
    j = i
    while A_add[j][i] == 0:
        j += 1

    A_add[[i, j]] = A_add[[j, i]]

    pivot = A_add[i][i]

    for k in range(i+1, n):
        coef = A_add[k][i] / pivot
        tmp = np.copy(A_add[i])
        tmp = [x * coef for x in tmp]
        A_add[k] = np.subtract(A_add[k], tmp)

        print(A_add)
        print("\n")

print("\n")

for i in range(n-1, -1, -1):

    pivot = A_add[i][i]

    for k in range(i - 1, -1, -1):
        coef = A_add[k][i] / pivot
        tmp = np.copy(A_add[i])
        tmp = [x * coef for x in tmp]
        A_add[k] = np.subtract(A_add[k], tmp)

        print(np.array(A_add))
        print("\n")

x = []
for i in range(0, n):
    tmp = A_add[i][-1] / A_add[i][i]
    x.append(tmp)

print(np.array(x))