from PIL import Image
import numpy as np
from funciones import padding, varCanal

def main():
    path = 'tp2-pizarro-pereyra/image.png'
    red, green, blue = padding(path)

    imagen = np.stack([red, green, blue], 0) # Junto de nuevo las 3, la dimensión queda (3, 516, 516)

if __name__ == '__main__':
    main()
    