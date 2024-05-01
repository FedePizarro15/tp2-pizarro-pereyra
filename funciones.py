import numpy as np
from PIL import Image

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'espacio', '.', ',', '?', '!', '¿', '¡', '(', ')', ':', ';', '-', '“', '‘', 'á', 'é', 'í', 'ó', 'ú', 'ü', 'ñ']

secuencia = [(numero, letra) for numero, letra in enumerate(letras,1)]

def kuwahara(path: str):
    '''
    Aplica el efecto "Kuwahara", un filtro de suavizado no lineal.
    Argumentos:
    - path --> ubicación de la imagen a la cuál se le aplicará el filtro
    Returns:
    - numpy.ndarray de la imagen con el filtro aplicado
    '''
    
    # Transformo la imagen a un numpy.ndarray y le aplico un padding de 2 en la altura y en la anchura
    imagenOriginal = np.array(Image.open(path))
    imagenPad = np.pad(imagenOriginal, ((2,2), (2,2), (0,0)), 'edge') # dim --> (516,516,3)
    
    altura, anchura, profundidad = imagenPad.shape # Tomo las dimensiones del array para poder hacer el bucle sin tomar elementos del padding
    imagenResultado = np.zeros_like(imagenPad)
    
    for y in range(2,altura-2):
        for x in range(2,anchura-2):
            
            # Entorno 5x5 sin agarar el pad
            entorno = imagenPad[y-2:y+3,x-2:x+3,:] # entorno dim --> (5,5,3) 

            # Agarro caudrantes de 3x3x3
            cuadranteA = entorno[:3, 0:3, :] 
            cuadranteB = entorno[:3, 2:6, :]
            cuadranteC = entorno[2:6, 0:3, :]
            cuadranteD = entorno[2:6, 2:6, :]
            
            # Sumo las varianzas de cada canal
            sumaA = sum( (np.var(cuadranteA[:,:,0]), np.var(cuadranteA[:,:,1]), np.var(cuadranteA[:,:,2])) )
            sumaB = sum( (np.var(cuadranteB[:,:,0]), np.var(cuadranteB[:,:,1]), np.var(cuadranteB[:,:,2])) )
            sumaC = sum( (np.var(cuadranteC[:,:,0]), np.var(cuadranteC[:,:,1]), np.var(cuadranteC[:,:,2])) )
            sumaD = sum( (np.var(cuadranteD[:,:,0]), np.var(cuadranteD[:,:,1]), np.var(cuadranteD[:,:,2])) )

            # Me quedo con el cuadrante cuya varianza sea menor
            if min(sumaA, sumaB, sumaC, sumaD) == sumaA:
                cuadranteElegido = cuadranteA
            elif min(sumaA, sumaB, sumaC, sumaD) == sumaB:
                cuadranteElegido = cuadranteB
            elif min(sumaA, sumaB, sumaC, sumaD) == sumaC:
                cuadranteElegido = cuadranteC
            else:
                cuadranteElegido = cuadranteD
            
            # El pixel en el que estoy se convierte en el promedio del cuadrante elegido (por canal)
            imagenResultado[y,x,0] = np.average(cuadranteElegido[:,:,0])
            imagenResultado[y,x,1] = np.average(cuadranteElegido[:,:,1])
            imagenResultado[y,x,2] = np.average(cuadranteElegido[:,:,2])

    return imagenResultado[2:-2, 2:-2, :]