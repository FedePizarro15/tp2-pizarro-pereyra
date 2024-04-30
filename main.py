from PIL import Image
import numpy as np
from funciones import *

def main():
    path = 'tp2-pizarro-pereyra\image.png'
    
    a = kuwahara2(path)
    imagen = Image.fromarray(a)
    imagen.save("imagen_kuwahara.png")

if __name__ == '__main__':
    main()
    