from PIL import Image
import numpy as np
from funciones import kuwahara

profe = np.array(Image.open('kuwahara_baboon.png'))
nuestro = np.array(Image.open('kuwahara_baboon_nuestro.png'))

for i in range(len(nuestro)):
    if np.all(nuestro[i] == profe[i]):
        continue
    print('fallo')
    print(i)
    print(nuestro[i])
    print(profe[i])
            
# if np.all(nuestro == profe):
#     print(True)
# else:
#     print(False)