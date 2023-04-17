
"""
  Listas:

    Es una colección de elementos que pueden contener elementos de múltiples tipos de datos.
    Ejemplo:
      lista= [1, 'Subaru', ['a', 'e']]

  Arrays:

    Una matriz o Array es un vector que contiene elementos homogéneos, es decir, que pertenecen al mismo tipo de datos.
    Ejemplo:
      a = arr.array('d', [1.1, 3.5, 4.5])
"""

import numpy as np

lista= [1, 3, 5]
matriz= np.array([2, 4, 6])

lista.append(7)

# De esta forma se le añade valor a cada uno de los valores anteriormente añadidos
matriz = matriz + np.array([8])

print(lista)
print(matriz)


# Listas: no pueden manejar operaciones aritméticas directamente
# Array: sí pueden manejar operaciones aritméticas directamente


a= [1, 2, 3]
b= [4, 5, 6]

print(a + b)


c = np.array([1, 2, 3])
d = np.array([4, 5, 6])

print(c * d)