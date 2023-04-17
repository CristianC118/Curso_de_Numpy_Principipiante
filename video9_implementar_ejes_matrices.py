

# axis 1 filas, axis 0 columnas
# axis/ejes controla el parámetro para cada función
# para aplicar ejes solo se usan matrices de 2 ejes

import numpy as np

m1= np.array([[0, 1, 2], [4, 2, 3]])
print(m1)

print('-------------------------------')

print(np.sum(m1, axis= 0))


m2= np.array([[1, 1], [1, 1]])
m3= np.array([[8, 8], [8, 8]])

print(m2)
print('-------------------------------')
print(m3)

print('-------------------------------')

print(np.concatenate([m2, m3], axis= 1))

# Axis/Eje 0 para matrices en una sola dimensión