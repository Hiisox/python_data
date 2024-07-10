import numpy as np
from PIL import Image
from array import array
import matplotlib.pyplot as plt


def load_image(path:str) -> array :
    try:
        img = Image.open(path)
    except Exception :
        print("AssertionError: Wrong image's path")
        return None
    img = np.array(img)
    plt.imshow(img, cmap="grey")
    plt.show()
    plt.clf()
    return img