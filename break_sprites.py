from PIL import Image
from itertools import product
import os

def tile(filename, dir_in, dir_out, d):
    print('test')
    name, ext = os.path.splitext(filename)
    img = Image.open(os.path.join(dir_in, filename))
    w, h = img.size
    print(w, h, d)
    
    grid = product(range(0, h-h%d, d), range(0, w-w%d, d))
    for i, j in grid:
        box = (j, i, j+d, i+d)
        out = os.path.join(dir_out, f'{name}_{i}_{j}{ext}')
        img.crop(box).save(out)


if __name__ == "__main__":
    tile('Trees.png', 'C:/Users/khann/OneDrive/Desktop/Test split/assets/inputs', 'C:/Users/khann/OneDrive/Desktop/Test split/outputs/assets/Trees', 16)