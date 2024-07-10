from load_image import load_image
from array import array
import matplotlib.pyplot as plt


def invert(array) -> array:
    new_array = array.copy()
    for x in range(len(new_array)):
        for y in range(len(new_array[x])):
            new_array[x][y][0] = 255 - new_array[x][y][0]
            new_array[x][y][1] = 255 - new_array[x][y][1]
            new_array[x][y][2] = 255 - new_array[x][y][2]
    plt.imshow(new_array)
    plt.show()
    return new_array


def grey(array) -> array:
    new_array = array.copy()
    for x in range(len(new_array)):
        for y in range(len(new_array[x])):
            value = int(sum(new_array[x][y]))
            if value > 765:
                value = 756
            new_array[x][y][2] = int(value / 3)
            new_array[x][y][1] = int(value / 3)
            new_array[x][y][0] = int(value / 3)
    plt.imshow(new_array)
    plt.show()
    return new_array


def blue(array) -> array:
    new_array = array.copy()
    for x in range(len(new_array)):
        for y in range(len(new_array[x])):
            new_array[x][y][0] = 0
            new_array[x][y][1] = 0
    plt.imshow(new_array)
    plt.show()
    return new_array


def green(array) -> array:
    new_array = array.copy()
    for x in range(len(new_array)):
        for y in range(len(new_array[x])):
            new_array[x][y][0] = 0
            new_array[x][y][2] = 0
    plt.imshow(new_array)
    plt.show()
    return new_array


def red(array) -> array:
    new_array = array.copy()
    for x in range(len(new_array)):
        for y in range(len(new_array[x])):
            new_array[x][y][1] = 0
            new_array[x][y][2] = 0
    plt.imshow(new_array)
    plt.show()
    return new_array


def main():
    array = load_image("landscape.jpg")
    # invert(array)
    # red(array)
    # blue(array)
    # green(array)
    grey(array)
    return


if __name__ == "__main__":
    main()