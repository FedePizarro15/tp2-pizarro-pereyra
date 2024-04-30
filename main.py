from PIL import Image
import numpy as np
from funciones import *

def main():
    path = 'tp2-pizarro-pereyra\image.png'
    
    # prueba kuwahara
    a = kuwahara(path)
    imagen = Image.fromarray(a)
    imagen.save("imagen_kuwahara.png")

if __name__ == '__main__':
    main()
    