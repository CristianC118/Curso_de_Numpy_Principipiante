

import numpy as np

m1= np.array([90, 7, 9, 4, 2, 1])

# Ordenamos los elementos
print(np.sort(m1))


m2= np.array([2, 3])

# Elevamos al cubo
print(np.power(m2, 3))
print(np.array(m2 ** 3))


m3= np.array([2, 3, 4, 5, 6, 7])

# Identificar valores mediante una clasificación
print(np.array(m3 >= 4))


m4= np.array([2, 3, 4, 5, 6, 7])

# Hallar el valor máximo y mínimo que se encuentra en la matriz
print(np.array(m4.max()))
print(np.array(m4.min()))


m5= np.array([2, 4, 6, 8])
m6= np.array([10, 12, 14, 16])

# Combinar matrices
print(np.concatenate((m5, m6)))


m7= np.array([[1, 2], [3, 4]])
m8= np.array([[5, 6], [7, 8]])

# Suma, Resta, Multiplicación y División de matrices
print(np.add(m7, m8))

print(np.subtract(m7, m8))

print(np.multiply(m7, m8))

print(np.divide(m7, m8))


# Tomar posición de cada uno de los elementos
print(m7.dot(m8))