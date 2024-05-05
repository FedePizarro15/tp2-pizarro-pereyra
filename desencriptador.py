from PIL import Image
from funciones import decypher

def main():
    print('== Desencriptador ==')
    path = input("Ingrese el nombre del archivo encriptado:\n> ")
    msg = decypher(path)
    print(f'El mensaje oculto es:\n{msg}')

if __name__ == '__main__':
    print(main())