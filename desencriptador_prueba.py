from funciones import decypher

def main():
    print('== Desencriptador ==')
    path = 'prueba7_encriptado.png'
    msg = decypher(path)
    print(f'El mensaje oculto es:\n{msg}')

if __name__ == '__main__':
    print(main())