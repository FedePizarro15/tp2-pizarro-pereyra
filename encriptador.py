from funciones import encryptor

def main():
    print('== Encriptador ==')
    path_input = input(f"Ingrese nombre de la imagen a utilizar como base:\n> ")
    path = f'{path_input}.png'
    msg = input("Ingrese el mensaje a esconder:\n> ")
    final_name = input("Ingrese nombre del archivo de salida:\n> ")
    image = encryptor(msg, path)
    image.save(f"{final_name}.png")

if __name__ == '__main__':
    main()