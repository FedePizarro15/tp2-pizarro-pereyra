from PIL import Image
import numpy as np
from funciones import padding, varCanal

def main():
    red, green, blue = padding("image.png")
    print("Red\n\n", red, "\n\nGreen\n\n", green, "\n\nBlue\n\n", blue)

    # n = varCanal(red) 
    
    # for i, e in enumerate(n):
    #     print(f"Cuadrante {i} \n {e}")


if __name__ == '__main__':
    main()