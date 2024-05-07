from PIL import Image
import numpy as np
import PIL

x = Image.open("image.png")
print(type(x))

g = np.array([1,0,0])
x = Image.fromarray(g)
print(type(x))

def x(ajisndasd:str)->PIL.Image.Image:
    pass