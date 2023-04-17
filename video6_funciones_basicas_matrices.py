

import numpy as np

# Función linspace genera matrices
m= np.arange(27).reshape(3, 3, 3)

# Devuelve info
print(m.shape)

# Devuelve las dimensiones
print(m.ndim)

# Devuelve el número total de elementos
print(m.size)

print(m)