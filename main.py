from PIL import Image
import numpy as np
from funciones import padding, varCanal

def main(path : str):
    red, green, blue = padding(path)
    print("Red\n\n", red, "\n\nGreen\n\n", green, "\n\nBlue\n\n", blue)
    
    canales = red, green, blue

    varCanal(canales)
    #     print(f"Cuadrante {i} \n {e}")


if __name__ == '__main__':
    main('image.png')