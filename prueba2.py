import numpy as np
from PIL import Image

n = np.array([[1,2,3,4,5], [1,2,3,4,5], [0,0,0,0,0],[1,2,3,4,5], [1,2,3,4,5]])
# print(n, "\n", n.shape, "\n")

# # Nueva columna
# b = np.array([[0,0,0]])
# print("Nueva columna\n", b, "\n")

# n = np.append(n, b, axis=0)
# print(n)

# # Nueva fila

# a = np.array([[0], [0], [0], [0]])
# print("Nueva fila\n", a, "\n")

# n = np.append(n, a, axis=1)
# print(n)

# n = np.zeros((1,512))
# print(n)
print(n)
cuadranteA = n[:3, :3]
cuadranteB = n[:3, 2:6]
cuadranteC = n[2:6, :3]
cuadranteD = n[2:6,2:6]
print(cuadranteA) 
print(cuadranteB) 
print(cuadranteC) 
print(cuadranteD) 