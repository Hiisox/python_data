from PIL import Image
import numpy as np
from array import array


def ft_load(path: str) -> array:
    try:
        img = Image.open(path)
    except Exception:
        print("AssertionError: wrong image's path")
        return None
    img_array = np.array(img)
    print(f"The shape of image is: {img_array.shape}")
    return img_array
