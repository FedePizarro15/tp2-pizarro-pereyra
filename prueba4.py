import numpy as np

# entorno5x5 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

# matrizEntorno = np.array([entorno5x5[x * 5:x * 5 + 5] for x in range(5)])

# matrizEntorno2 = np.array([[entorno5x5[0:5]], [entorno5x5[5:10]], [entorno5x5[10:15]], [entorno5x5[15:20]], [entorno5x5[20:25]]]) # Creo el ndarray con las 5 filas de 'entorno5x5'

# print(matrizEntorno)
# print(matrizEntorno2)

# cuadranteA = matrizEntorno[:3, :3]
# cuadranteB = matrizEntorno[:3, 2:6]
# cuadranteC = matrizEntorno[2:6, :3]
# cuadranteD = matrizEntorno[2:6, 2:6]

# print(cuadranteA)
# print(cuadranteB)
# print(cuadranteC)
# print(cuadranteD)

def varCanal(canales : list):
    for i in range(3,515):
        for j in range(3,515): # Bucle por cada elemento del canal
            
            entorno5x5 = []
            
            for y in range(i-2, i+3): 
               for x in range(j-2, j+3):
                
                    entornos5x5 = [canal[x][y] for canal in canales]
                    
                    matrizEntorno = np.array([entorno5x5[x * 5:x * 5 + 5] for x in range(5)])
            
                    cuadranteA, cuadranteB, cuadranteC, cuadranteD = matrizEntorno[:3, :3], matrizEntorno[:3, 2:6], matrizEntorno[2:6, :3], matrizEntorno[2:6, 2:6]

                    varA = np.var(cuadranteA)
                    varB = np.var(cuadranteB)
                    varC = np.var(cuadranteC)
                    varD = np.var(cuadranteD)
                
                    '''

                    Calcularía este for dentro de cada iteración, no los guardaria en una lista que tenga los entornos, a no ser que despues nos hagan falta.

                    '''
                         # Crear 4 arrays de los 4 cuadrantes
                            # Calcular varianza de cada cuadrante(numpy.var)
    return

varCanal([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])