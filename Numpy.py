import numpy

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr))


import numpy as np
print(np.__version__)


import numpy as np
NumPy = np.array((range(6)))
print(NumPy)


import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[[1, 2, 3], [4, 5, 6]]], [[[9, 10, 11], [7, 8, 12]]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

y = np.array([range(10)], ndmin=6)
print(y)
print("The number of dimensions are",y.ndim,"-D")

t = np.array([range(11)])
print(t**t)
print(t*t)

import numpy as np

b = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('5th element on 1st row: ', b[0, 4])
print('Last element from 2nd dim: ', b[1, -1])

a7 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(a7[0, 1, 2])
print(a7[1, 0, 2])



