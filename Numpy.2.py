import numpy as np
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

n = a.reshape(4, 3)
print(a)
print(a.shape)
print(n)

ar = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
na = ar.reshape(-1)
print(ar)
print(na)

y = np.array([1, 2, 3, 4])
for x in y:
    print(x)


b = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for d in b:
    for g in d:
        print(g)
