from PIL import Image
from funciones import cypher

def main():
    print('== Encriptador ==')
    path = 'prueba7.png'
    msg = 'Hola'
    final_name = 'prueba7_encriptado.png'
    image_c = cypher(msg, path)
    image = Image.fromarray(image_c)
    image.save(f"{final_name}.png")

if __name__ == '__main__':
    main()