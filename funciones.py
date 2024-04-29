import numpy as np
from PIL import Image

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'espacio', '.', ',', '?', '!', '¿', '¡', '(', ')', ':', ';', '-', '“', '‘', 'á', 'é', 'í', 'ó', 'ú', 'ü', 'ñ']

secuencia = [(numero, letra) for numero, letra in enumerate(letras,1)]

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

def varCanal(canal : np.ndarray):

    entornos = []
    varianzas = {}

    for i, fila in enumerate(canal):
        for j, elemento in enumerate(fila): # Bucle por cada elemento del canal
    # for i in range(1):
    #     for j in range(1):
            entorno5x5 = []

            for y in range(max(0, i-5), min(i+5, np.shape(canal)[1])): 
               for x in range(max(0, j-5), min(j+5, np.shape(canal)[0])): 

                    entorno5x5.append(canal[y,x]) # Cada elemento del 5x5 lo agrego a 'entorno5x5'

            matrizEntorno = np.array([entorno5x5[0:5], entorno5x5[5:10], entorno5x5[10:15], entorno5x5[15:20], entorno5x5[20:25]]) # Creo el ndarray con las 5 filas de 'entorno5x5'
            entornos.append(matrizEntorno)


    for i, entorno in enumerate(entornos,1): # Tomo los cuadrantes y les calculo las varianzas
        cuadranteA = entorno[:3, :3]
        cuadranteB = entorno[:3, 2:6]
        cuadranteC = entorno[2:6, :3]
        cuadranteD = entorno[2:6, 2:6] 

        varA = np.var(cuadranteA)
        varB = np.var(cuadranteB)
        varC = np.var(cuadranteC)
        varD = np.var(cuadranteD)

        varianzas[i] = [varA, varB, varC, varD]
    return varianzas

    # Promedio tomarlo con np.average
def calcVarianza(red : np.ndarray, green : np.ndarray, blue: np.ndarray):
    pass

'''

Calcularía este for dentro de cada iteración, no los guardaria en una lista que tenga los entornos, a no ser que despues nos hagan falta.

'''

def kawahara(red : np.ndarray, green : np.ndarray, blue : np.ndarray): # Aplicar filtro kawahara        
    pass