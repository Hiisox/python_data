from PIL import Image
import numpy as np
from array import array


def zoom():
    x = slice(100, 500)
    y = slice(450, 850)
    return [x, y]


def load_image(path: str) -> array:
    try:
        img = np.array(Image.open(path))
    except Exception:
        print("AssertionError: Wrong image's path")
        return None
    for x in range(len(img)):
        for y in range(len(img[x])):
            value = img[x][y][0] * 0.299 + img[x][y][1] * 0.587 + img[x][y][2] * 0.114
            img[x][y][0] = value
    x, y = zoom()
    img = img[x, y, :1]
    print(f"My shape of the image is: {img.shape} or {img.shape[:2]}")
    print(img)
    return img

