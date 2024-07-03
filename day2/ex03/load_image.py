from PIL import Image
import numpy as np


def load_image(path: str) -> list:
    try:
        img = Image.open(path)
    except Exception:
        print("AssertionError: wrong image's path")
        return None
    img_array = np.array(img)
    print(f"The shape of image is: {img_array.shape}")
    print(img_array)
    return img_array
