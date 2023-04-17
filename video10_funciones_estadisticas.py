
"""
"""

import numpy as np

m= np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m)
print('--------------------')

# Valor máximo y mínimo
print(np.amin(m, 1))

# Obtener un rango
print(np.ptp(m, axis= 1))

# Percentil sirve para comparar un conjunto de datos
print(np.percentile(m, 50))

# En caso que sea impar: percentiles= q(n + 1) / 100
# En caso de ser par: percentiles= q X n / 100
# mediana= (n + 1) / 2

print(np.median(m))

# media aritmética= x1 + x2 + ...xn / n
print(np.mean(m))



print('--------------------')
m2= np.array([1, 2, 3, 4, 5, 6])
print(m2)

# Promedio ponderado: PM= x1 * p1 + xn * pn / p
# cuando no hay peso se determina con el valor de 1
print(np.average(m2))


print('--------------------')

# Desviación estandar: std= sqrt(mean(abs(x - x.mean()) ** 2))
print(np.std(m2))