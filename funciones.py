import numpy as np
from PIL import Image

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'espacio', '.', ',', '?', '!', '¿', '¡', '(', ')', ':', ';', '-', '“', '‘', 'á', 'é', 'í', 'ó', 'ú', 'ü', 'ñ']

secuencia = [(numero, letra) for numero, letra in enumerate(letras,1)]
print(secuencia)

def crearCanales(path : str):
    '''Devuelve los canales RGB de la imagen importada en 3 matrices diferentes'''
    # Se importa la imagen
    imagen = Image.open(path)

    # Se guardan las matrices
    canales = np.array(imagen)

    # Se ordenan las matrices por canales
    red = canales[:,:,0]
    green = canales[:,:,1]
    blue = canales[:,:,2]
    
    return red, green, blue

def padding(path : str):
    red, green, blue = crearCanales(path)
    
    # Agregar padding
    red = np.pad(red,2,'edge')
    green = np.pad(green,2,'edge')
    blue = np.pad(blue,2,'edge')
    
    return red, green, blue

def varCanal(canales : list):
    for i in range(2,5):
        for j in range(2,5): # Bucle por cada elemento del canal
            
            print(f'\n\nElemento [{i},{j}].\n\n')
            
            entorno5x5 = []
            
            for y in range(i-2, i+3): 
               for x in range(j-2, j+3):
                
                    entorno5x5 += [canal[x][y] for canal in canales]
                    
            for l in range(5):
                matrizEntorno = [entorno5x5[k * 3:k * 3 + 3] for k in range(l*5,l*5+5)]
                print(matrizEntorno)
            print()
            
            cuadranteA, cuadranteB, cuadranteC, cuadranteD = matrizEntorno[:3][:3], matrizEntorno[:3][2:5], matrizEntorno[2:5][:3], matrizEntorno[2:5][2:6]
            print(cuadranteA,cuadranteB,cuadranteC,cuadranteD)
            # varAred, varAgreen, varAblue, = np.var(cuadranteA[0])
            # varB = np.var(cuadranteB)
            # varC = np.var(cuadranteC)
            # varD = np.var(cuadranteD)

                         # Crear 4 arrays de los 4 cuadrantes
                            # Calcular varianza de cada cuadrante(numpy.var)

def kawahara(red : np.ndarray, green : np.ndarray, blue : np.ndarray): # Aplicar filtro kawahara        
    pass