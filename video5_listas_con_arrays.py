
import numpy as np

# Creacion de una matriz en 2D
m2D= np.array([[1, 2, 3], [4, 5, 6]])
print(m2D)

lista= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz= np.array(lista)
print(matriz)

# Generar matriz de 2D de manera rápida
m= np.arange(20).reshape(4, 5)
print(m)