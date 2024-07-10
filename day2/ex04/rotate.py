import matplotlib.pyplot as plt
from load_image import load_image
import numpy as np
from array import array

def main():
    img = load_image("animal.jpeg")
    if img is None:
        return
    new_img = rotate(img)
    print(f"New shape after Transpose: {new_img.shape}")
    print(new_img)
    plt.imshow(new_img)
    plt.show()


def rotate(img:list) ->array:
    new_img = []
    for y in range(len(img[0]) - 1, -1, -1):
        new_raw = [int(img[x][y][0]) for x in range(len(img))]
        new_img.append(new_raw)
    new_img = np.array(new_img)
    return new_img


if __name__ == "__main__":
    main()