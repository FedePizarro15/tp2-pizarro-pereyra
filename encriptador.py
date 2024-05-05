from PIL import Image
from funciones import cypher

def main():
    print('== Encriptador ==')
    path = f'{input("Ingrese nombre de la imagen a utilizar como base:> ")}.png'
    msg = input("Ingrese el mensaje a esconder:\n> ")
    final_name = input("Ingrese nombre del archivo de salida:\n> ")
    image_c = cypher(msg, path)
    image = Image.fromarray(image_c)
    image.save(f"{final_name}.png")

if __name__ == '__main__':
    main()