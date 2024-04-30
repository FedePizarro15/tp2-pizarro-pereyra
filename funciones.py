import numpy as np
from PIL import Image

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'espacio', '.', ',', '?', '!', '¿', '¡', '(', ')', ':', ';', '-', '“', '‘', 'á', 'é', 'í', 'ó', 'ú', 'ü', 'ñ']

secuencia = [(numero, letra) for numero, letra in enumerate(letras,1)]
'''
Esta parte comentada es el codigo para hacerlo por canal, abajo esta la manera q queremos probar ahora usando al matriz entera
'''


def kuwahara2(path: str):
    imagenOriginal = np.array(Image.open(path))
    imagenPad = np.pad(imagenOriginal, ((2,2), (2,2), (0,0)), 'edge') # dim --> (516,516,3)
    altura, anchura, profundidad = imagenOriginal.shape
    for y in range(2, altura-2):
        for x in range(2, anchura-2):
            
            #entorno 5x5 sin agarar el pad
            entorno = imagenPad[y-2:y+3,x-2:x+3,:] # entorno dim --> (5,5,3) 

            # agarro caudrantes de 3x3x3
            cuadranteA = entorno[:3, 0:3, :] 
            cuadranteB = entorno[:3, 2:6, :]
            cuadranteC = entorno[2:6, 0:3, :]
            cuadranteD = entorno[2:6, 2:6, :]
            
            sumaA = sum( (np.var(cuadranteA[:,:,0]), np.var(cuadranteA[:,:,1]), np.var(cuadranteA[:,:,2])) )
            sumaB = sum( (np.var(cuadranteB[:,:,0]), np.var(cuadranteB[:,:,1]), np.var(cuadranteB[:,:,2])) )
            sumaC = sum( (np.var(cuadranteC[:,:,0]), np.var(cuadranteC[:,:,1]), np.var(cuadranteC[:,:,2])) )
            sumaD = sum( (np.var(cuadranteD[:,:,0]), np.var(cuadranteD[:,:,1]), np.var(cuadranteD[:,:,2])) )

            if min(sumaA, sumaB, sumaC, sumaD) == sumaA:
                cuadranteElegido = cuadranteA
            elif min(sumaA, sumaB, sumaC, sumaD) == sumaB:
                cuadranteElegido = cuadranteB
            elif min(sumaA, sumaB, sumaC, sumaD) == sumaC:
                cuadranteElegido = cuadranteC
            else:
                cuadranteElegido = cuadranteD

            imagenOriginal[y,x,0] = np.average(cuadranteElegido[:,:,0])
            imagenOriginal[y,x,1] = np.average(cuadranteElegido[:,:,1])
            imagenOriginal[y,x,2] = np.average(cuadranteElegido[:,:,2])

    return imagenOriginal
