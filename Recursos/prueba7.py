import numpy as np
from PIL import Image
from funciones import *

image = []

for i in range(5):
    for j in range (5):
        image += [[]]
        for k in range(3):
            image[j] += [(k+1)*(j+1)*(i+1)]
            
image = [image]

image = Image.fromarray(image)

image.save('prueba7.png')