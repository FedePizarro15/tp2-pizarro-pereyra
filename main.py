from PIL import Image
import numpy as np
from funciones import *

def main():
    path = 'jirafa.png'
    
    # prueba kuwahara
    filtro = kuwahara(path)
    imagen = Image.fromarray(filtro)
    imagen.save("jirafa_kuwahara.png")

if __name__ == '__main__':
    main()
    