import numpy as np
from PIL import Image

def kuwahara(path: str) -> np.ndarray:
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

def msg_cypher(msg: str) -> list:
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '.', ',', '?', '!', '¿', '¡', '(', ')', ':', ';', '-', '“', '‘', 'á', 'é', 'í', 'ó', 'ú', 'ü', 'ñ']

    secuencia = [(numero, letra) for numero, letra in enumerate(letras,1)]

    msg_lower = msg.lower()

    msg_list = list(msg_lower)

    for i in range(len(msg) - 1):
        msg_list.insert(i * 2 + 1,-1)
        
    for i,l in enumerate(msg_list):
        if l != -1:
            for n,k in secuencia:
                if l == k:
                    msg_list[i] = n
                    break

    z = False

    for i, l in enumerate(msg_list):
        if z:
            z = False
            continue
        
        if l != -1:
            if l >= 10:
                z = True
                msg_list.pop(i)
                for j, k in enumerate(str(l)):
                    msg_list.insert(i+j, int(k) + 1)
            else:
                msg_list[i] = msg_list[i] + 1

    msg_list.append(0)
        
    return msg_list

def cypher(msg: str, image: str) -> np.ndarray:
    image_k = kuwahara(image)
    msg_c = msg_cypher(msg)
    
    y = 1
    x = 1
    
    for l in msg_c:
    # for y in range(1, len(image_k), 2):
    #     for x in range(1, len(image_k), 2):
    #         l += 1
        entorno = image_k[y-1 : y+1, x-1 : x+1, :]
        
        var_r = np.var([entorno[0,0,0], entorno[0,1,0], entorno[1,0,0]])
        var_g = np.var([entorno[0,0,1], entorno[0,1,1], entorno[1,0,1]])
        var_b = np.var([entorno[0,0,2], entorno[0,1,2], entorno[1,0,2]])
        
        if min(var_r, var_g, var_b) == var_r:
            average = np.average([entorno[0,0,0], entorno[0,1,0], entorno[1,0,0]])
        elif min(var_r, var_g, var_b) == var_g:
            average = np.average([entorno[0,0,1], entorno[0,1,1], entorno[1,0,1]])
        else:
            average = np.average([entorno[0,0,2], entorno[0,1,2], entorno[1,0,2]])
        
        new_value = 256
        
        image_k[y,x] = new_value
        
        if x >= len(image_k):
            y += 2
            x = 0
            continue
        x += 2
        
    return image_k