from PIL import Image
from funciones import cypher

def main():
    path = input("Ingrese nombre de la imagen a utilizar como base:\n> ")
    msg = input("Ingrese el mensaje a esconder:\n> ")
    nombreResultado = input("Ingrese nombre del archivo de salida:\n> ")
    image_c = cypher(msg, path)
    image = Image.fromarray(image_c)
    image.save(f"{nombreResultado}_cyphered.png")

if __name__ == '__main__':
    main()