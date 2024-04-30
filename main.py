from PIL import Image
import numpy as np
from funciones import *

def main():
    path = 'tp2-pizarro-pereyra/image.png'
    # red, green, blue = paddingCanal(path)

    # imagen = np.stack([red, green, blue], 0) # Junto de nuevo las 3, la dimensión queda (3, 516, 516)

    # =================================================================

    imagen = matrizParaFiltro(path)
    
    kawahara(imagen)


if __name__ == '__main__':
    main()
    