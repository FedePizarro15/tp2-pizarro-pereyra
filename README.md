# Trabajo Práctico 2 Pensamiento Computacional
## Federico Pizarro y Agustín Pereryra

## Programa que consiste en 2 módulos, encriptación y desencriptación

## Módulo encriptador:
Le pide al usuario el path de la imagen a encriptar, el mensaje a cifrar y el nombre del archivo de salida.
Se le aplica el filtro kuwahara a la imagen, se cifra el mensaje y se lo encripta en la imagen.
Crea un archivo con el nombre dado que contiene a la imagen encriptada.

## Módulo desencriptador:
Le pide al usuario el path de la imagen a desencriptar, desencripta el mensaje e imprime el mensaje descifrado.

## Módulo Funciones
### - kuwahara() 
Aplica a una imagen el filtro kuwahara un filtro de suavizado no lineal.

### - msg_cypher()
Cifra el mensaje según una lista de caracteres y sus números correspondintes.

### - cypher()
Encripta un mensaje cifrado en una imagen a la que se le aplica el filtro "kuwahara".

### - decypher()
Desencripta un mensaje cifrado en una imagen.

### - msg_decypher()
Descifra un mensaje dado por números en una lista.