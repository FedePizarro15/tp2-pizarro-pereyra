import numpy as np
from PIL import Image
import math

'''
¿Se puede usar "math"?
¿Se puede usar min(), max()?
'''

def kuwahara(path: str) -> np.ndarray:
    '''
    Aplica el efecto "Kuwahara", un filtro de suavizado no lineal.
    - Argumentos:
    path --> Ubicación de la imagen a la cuál se le aplicará el filtro.
    - Retorna:
    Matriz de la imagen con el filtro aplicado.
    '''

    # Transformación de la imagen a numpy.ndarray y aplicación un padding de 2 de alto y ancho
    original_image = np.array(Image.open(path))
    pad_image = np.pad(original_image, ((2,2), (2,2), (0,0)), 'edge') # dim --> (516,516,3)

    # Dimensiones del array para hacer el bucle sin elementos del padding
    heigth, width, _ = pad_image.shape
    kuwahara_image = np.zeros_like(pad_image)

    for y in range(2,heigth-1):
        for x in range(2,width-1):
            
            # Entorno 5x5 sin el padding
            environment = pad_image[y-2:y+3,x-2:x+3,:] # entorno dim --> (5,5,3) 

            # Cuadrantes 3x3x3
            quadrant_a = environment[:3, 0:3, :]
            quadrant_b = environment[:3, 2:6, :]
            quadrant_c = environment[2:6, 0:3, :]
            quadrant_d = environment[2:6, 2:6, :]
            
            # Suma de las varianzas de cada canal
            sum_a = sum((np.var(quadrant_a[:,:,0]), np.var(quadrant_a[:,:,1]), np.var(quadrant_a[:,:,2])))
            sum_b = sum((np.var(quadrant_b[:,:,0]), np.var(quadrant_b[:,:,1]), np.var(quadrant_b[:,:,2])))
            sum_c = sum((np.var(quadrant_c[:,:,0]), np.var(quadrant_c[:,:,1]), np.var(quadrant_c[:,:,2])))
            sum_d = sum((np.var(quadrant_d[:,:,0]), np.var(quadrant_d[:,:,1]), np.var(quadrant_d[:,:,2])))

            # Selección del cuadrante con menor varianza
            if min(sum_a, sum_b, sum_c, sum_d) == sum_a:
                selected_q = quadrant_a
            elif min(sum_a, sum_b, sum_c, sum_d) == sum_b:
                selected_q = quadrant_b
            elif min(sum_a, sum_b, sum_c, sum_d) == sum_c:
                selected_q = quadrant_c
            else:
                selected_q = quadrant_d
            
            # Promedio del cuadrante elegido es el nuevo valor del pixel
            kuwahara_image[y,x,0] = np.average(selected_q[:,:,0])
            kuwahara_image[y,x,1] = np.average(selected_q[:,:,1])
            kuwahara_image[y,x,2] = np.average(selected_q[:,:,2])

    return kuwahara_image[2:-2, 2:-2, :]

def msg_cypher(msg: str) -> list:
    '''
    Cifra el mensaje según una lista de caracteres y sus números correspondintes.
    - Argumentos:
    msg --> Mensaje que se quiere encifrar.
    - Retorna:
    Lista con el mensaje cifrado, cada caracter está dado por su correspondiente número, separado por "-1" y un "0" que marca el final del mensaje.
    '''
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '.', ',', '?', '!', '¿', '¡', '(', ')', ':', ';', '-', '“', '‘', 'á', 'é', 'í', 'ó', 'ú', 'ü', 'ñ']

    msg_lower = msg.lower()

    msg_list = list(msg_lower)

    for i in range(len(msg) - 1):
        msg_list.insert(i * 2 + 1,-1)
        
    for i, l in enumerate(msg_list):
        if l != -1:
            msg_list[i] = words.index(l) + 1

    flag = False

    for i, l in enumerate(msg_list):
        if flag:
            flag = False
            continue
        
        if l != -1:
            flag = True
            msg_list.pop(i)
            for j, k in enumerate(str(l)):
                msg_list.insert(i+j, int(k) + 1)

    msg_list.append(0)
        
    return msg_list

def cypher(msg: str, path: str) -> Image.Image:
    '''
    Encripta un mensaje cifrado en una imagen a la que se le aplica el filtro "kuwahara".
    - Argumentos:
    msg --> Mensaje que se debe cifrar y encriptar en la imagen.
    path --> Ubicación de la imagen a la que se le encriptará el mensaje.
    - Retorna:
    Imagen que contiene el mensaje cifrado.
    '''
    image_k = kuwahara(path)
    msg_c = msg_cypher(msg)

    y = 1
    x = 1

    for l in msg_c:
        environment = image_k[y-1 : y+1, x-1 : x+1, :]
        
        var_r = np.var([environment[0,0,0], environment[0,1,0], environment[1,0,0]])
        var_g = np.var([environment[0,0,1], environment[0,1,1], environment[1,0,1]])
        var_b = np.var([environment[0,0,2], environment[0,1,2], environment[1,0,2]])
        
        if min(var_r, var_g, var_b) == var_r:
            average = math.floor(np.average([environment[0,0,0], environment[0,1,0], environment[1,0,0]]))
            new_value = (average + l) % 256
            image_k[y,x,0] = new_value
        elif min(var_r, var_g, var_b) == var_g:
            average = math.floor(np.average([environment[0,0,1], environment[0,1,1], environment[1,0,1]]))
            new_value = (average + l) % 256
            image_k[y,x,1] = new_value
        else:
            average = math.floor(np.average([environment[0,0,2], environment[0,1,2], environment[1,0,2]]))
            new_value = (average + l) % 256
            image_k[y,x,2] = new_value
        
        if x >= len(image_k) - 2:
            y += 2
            x = 1
            continue
        x += 2
    
    image = Image.fromarray(image_k)
    
    return image

def decypher(path: str) -> str:
    '''
    Desencripta un mensaje cifrado en una imagen.
    - Argumentos:
    path --> Ubicación de la imagen de la que se quiere descifrar un mensaje.
    - Retorna:
    Mensaje descifrado.
    '''
    msg_list = []

    image = np.array(Image.open(path))

    for y in range(1, len(image), 2):
        for x in range(1, len(image), 2):
            environment = image[y-1 : y+1, x-1 : x+1, :]
        
            var_r = np.var([environment[0,0,0], environment[0,1,0], environment[1,0,0]])
            var_g = np.var([environment[0,0,1], environment[0,1,1], environment[1,0,1]])
            var_b = np.var([environment[0,0,2], environment[0,1,2], environment[1,0,2]])
            
            if min(var_r, var_g, var_b) == var_r:
                average = np.average([environment[0,0,0], environment[0,1,0], environment[1,0,0]])
                value = environment[1,1,0] - math.floor(average)
            elif min(var_r, var_g, var_b) == var_g:
                average = np.average([environment[0,0,1], environment[0,1,1], environment[1,0,1]])
                value = environment[1,1,1] - math.floor(average)
            else:
                average = np.average([environment[0,0,2], environment[0,1,2], environment[1,0,2]])
                value = environment[1,1,2] - math.floor(average)
                
            if value == 0:
                msg_list += [value]
                msg = msg_decypher(msg_list)
                return msg
            elif value < -1:
                msg_list += [value + 256]
            else:
                msg_list += [value]
                
    msg = msg_decypher(msg_list)

    return msg

def msg_decypher(msg_list: list) -> str:
    '''
    Descifra un mensaje dado por números en una lista.
    - Argumentos:
    msg_list --> Lista con enteros que representan un caracter, ("-1" significa el cambio de caracter, "0" es el final del mensaje).
    - Retorna:
    Mensaje descifrado.
    '''
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '.', ',', '?', '!', '¿', '¡', '(', ')', ':', ';', '-', '“', '‘', 'á', 'é', 'í', 'ó', 'ú', 'ü', 'ñ']

    for i, n in enumerate(msg_list):
        msg_list[i] -= 1

    i = 0
    j = 0
    final_msg = [[]]

    while True:
        n = msg_list[i]
        
        if n == -1:
            if final_msg[-1] == []:
                final_msg.remove([])
            break
        elif n == -2:
            i += 1
            j += 1
            final_msg += [[]]
        else:
            final_msg[j] += [n]
            i += 1

    for i, l in enumerate(final_msg):
        sum = 0
        for j, n in enumerate(l):
            sum += n * (10 ** ((len(l) - 1) - j))
        final_msg[i] = sum

    msg = []

    for i in final_msg:
        msg.append(words[i - 1])

    msg = ''.join(msg)

    return msg