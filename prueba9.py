from PIL import Image

original = Image.open('kuwahara_baboon.png')
copia = Image.open('image.png')

if copia == original:
    print(True)
else:
    print(False)