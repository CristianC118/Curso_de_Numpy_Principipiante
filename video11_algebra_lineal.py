

import numpy as np

m= np.array([[1, -1, 2], [3, 2, 0]])
print(m)

print('---------------------')

m2= np.array([[1], [2], [3]])
print(m2)

# Matriz Transpuesta: Se obtiene cambiando sus filas por columnas (o viceversa).

print(np.transpose(m2))

print('Ejercicio 1')

a= np.array([[2, 1, -2], [3, 0, 1], [1, 1, -1]])
b= np.array([[-3], [5], [-2]])

print(a)
print('')
print(np.transpose(b))

print('----------------------')

x= np.linalg.solve(a, b)
print(x)

# Para confirmar si está bien hecho
print(np.allclose(np.dot(a, x), b))


print('Ejercicio 2')

ejer1= np.array([[2, 7, 3], [2, 8, 2], [1, 3, 1]])
print(ejer1)

ejer2= np.array([1, 1, 0])
ejer2.shape= (3, 1)
print(ejer2)

print('')

print(np.linalg.solve(ejer1, ejer2))

