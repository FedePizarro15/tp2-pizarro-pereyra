from PIL import Image
import numpy as np
from funciones import padding, varCanal

def main():
    path = 'tp2-pizarro-pereyra/image.png'
    red, green, blue = padding(path)
<<<<<<< HEAD
    print("Red\n\n", red, "\n\nGreen\n\n", green, "\n\nBlue\n\n", blue)
    
    canales = red, green, blue

    varCanal(canales)
    #     print(f"Cuadrante {i} \n {e}")
=======
>>>>>>> 25aa081f5cea9fea64c3b353d2e3eeb9b3e74e04

    imagen = np.stack([red, green, blue], 0) # Junto de nuevo las 3, la dimensión queda (3, 516, 516)

if __name__ == '__main__':
    main()
    