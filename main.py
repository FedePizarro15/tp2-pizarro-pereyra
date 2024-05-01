from PIL import Image
from funciones import *

def main(msg: str, path: str):
    name = path.replace('.png','')
        
    # prueba kuwahara
    image_c = cypher(msg, path)
    image = Image.fromarray(image_c)
    image.save(f"{name}_cyphered.png")

if __name__ == '__main__':
    main('Hola', 'jirafa.png')
    