

""" Los números aleatorios en NumPy no significan que sean números diferentes cada vez.
  Aleatorio significa algo que no se puede predecir lógicamente.
"""
import numpy as np

# Generar un número aleatorio
m1= np.random.randint(10)
print(m1)

# Generar números aleatorios en cantidad en una matriz de una sola dimensión
m2= np.random.randint(10, size= (5))
print(m2)

#Generar números aleatorios en cantidad en una matriz de 2 dimensiones
m3= np.random.randint(10, size= (3, 3))
print(m3)

# Generar números aleatorios con decimales
m4= np.random.rand(5)
print(m4)

# Generar un solo valor de una matriz que se encuentre en la lista
m5= np.random.choice([3, 5, 9, 5, 1])
print(m5)

""" Distribución Aleatoria:
  Es una lista de todos los valores posibles y la frecuencia con la que se produce cada valor.
"""

dado= np.random.choice([2, 4, 6], p= [0.5, 0.5, 0.0], size= (1))
print(dado)

ejer= np.random.choice([2, 4, 8, 10], p= [0.3, 0.5, 0.1, 0.1], size= [50])
print(ejer)