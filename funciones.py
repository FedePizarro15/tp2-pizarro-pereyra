import numpy as np
from PIL import Image

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
    for i, fila in enumerate(canal):
        for j, elemento in enumerate(fila): # Bucle por cada elemento del canal
            entorno5x5 = []
            for y in range(max(0, i-5), min(i+5, np.shape(canal)[1])): 
               for x in range(max(0, j-5), min(j+5, np.shape(canal)[0])): 
                    entorno5x5.append(canal[y,x]) # Cada elemento del 5x5 lo agrego a 'entorno5x5'
            matrizEntorno = np.array([[entorno5x5[0:5]], [entorno5x5[5:10]], [entorno5x5[10:15]], [entorno5x5[15:20]], [entorno5x5[20:25]]]) # Creo el ndarray con las 5 filas de 'entorno5x5'
            entornos.append(matrizEntorno)

            for entorno in entornos: # Tomo los cuadrantes y les calculo las varianzas
                cuadranteA = entorno[:3, :3]
                cuadranteB = entorno[:3, 2:6]
                cuadranteC = entorno[2:6, :3]
                cuadranteD = entorno[2:6, :3]
                varA = np.var(cuadranteA)
                varB = np.var(cuadranteB)
                varC = np.var(cuadranteC)
                varD = np.var(cuadranteD)
                
                '''
                
                Calcularía este for dentro de cada iteración, no los guardaria en una lista que tenga los entornos, a no ser que despues nos hagan falta.
                
                '''
                         # Crear 4 arrays de los 4 cuadrantes
                            # Calcular varianza de cada cuadrante(numpy.var)

def kawahara(red : np.ndarray, green : np.ndarray, blue : np.ndarray): # Aplicar filtro kawahara        
    pass