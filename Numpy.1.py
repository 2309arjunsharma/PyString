import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])
print(arr[:4])
print(arr[4:])
print(arr[-3:-1])
print(arr[3:5:2])
print(arr[3:6])
print(arr[1:5:2])
print(arr[::2])

y = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
print(y[1, 0:4])
print(y[0, ::2])
print(y[0, :2:])

import numpy as np

ar = np.array([1, 2, 3, 4])

print(ar.dtype)
r = np.array(["Banana", "Apple", "Cherry"])
print(r.dtype)


import numpy as np

a = np.array([1, 2, 3, 4], dtype='S')

print(a)
print(a.dtype)


rr = np.array([1.7, 2, 3, 4.123], dtype='f')

print(rr)
print(rr.dtype)


import numpy as np

v = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(v)
print(x)

f = np.array([0, 2, 3, 4, 5])
q = arr.view()
arr[0] = 42

print(f)
print(q)


import numpy as np

p = np.array([1, 2, 3, 4, 5, 6])

w = arr.copy()
e = arr.view()

print(w.base)
print(e.base)

