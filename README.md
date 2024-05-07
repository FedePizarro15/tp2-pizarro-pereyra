# TP 2 Pensamiento Computacional
## Federico Pizarro y Agustín Pereryra

## Programa que consiste en 2 módulos, encriptación y desencriptación

## Módulo encriptador:
Le pide al usuario el path de la imagen a encriptar, el mensaje a encriptar y el nombre del archivo de salida.
Se le aplica el filtro kuwahara a la imagen, se encripta el mensaje y se lo oculta en la imagen.
Crea un archivo con el nombre dado que contiene a la imagen encriptada

## Módulo desencriptador:
Le pide al usuario el path de la imagen a desencriptar, desencripta el mensaje e imprime el mensaje encontrado.

## Módulo Funciones
### - kuwahara() 
Aplica a una imagen el filtro kuwahara un filtro de suavizado no lineal
### - msg_cypher()
Encripta un mensaje con el mecanismo de encriptacion dado
### - cypher()
Esconde el mensaje encriptado en una imagen
### - decypher()
Extrae el mensaje aún encripatado que se esconde en una imagen
### - msg_decypher()
Desencripta el mensaje con el mecaniscmo de desencriptación dado