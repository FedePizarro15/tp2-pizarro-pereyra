from PIL import Image
from funciones import decypher

def main():
    print('== Desencriptador ==')
    path_input = input("Ingrese el nombre del archivo encriptado:\n> ")
    path = f'{path_input}.png'
    msg = decypher(path)
    print(f'El mensaje oculto es:\n{msg}')

if __name__ == '__main__':
    main()