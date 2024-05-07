import numpy as np
from PIL import Image
from funciones import kuwahara

filtro = kuwahara('prueba7.png')

filtro = Image.fromarray(filtro)

filtro.save('preuba7_kuwahara.png')