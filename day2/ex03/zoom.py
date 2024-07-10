import matplotlib.pyplot as plt
from load_image import load_image


def main():
    img = load_image("animal.jpeg")
    if img is None:
        return
    for x in range(len(img)):
        for y in range(len(img[x])):
            value = img[x][y][0] * 0.299 + img[x][y][1] * 0.587 + img[x][y][2] * 0.114
            img[x][y][0] = value
    x, y = zoom()
    img = img[x, y, :1]
    print(f"My new shape is {img.shape} or {img.shape[:2]}")
    print(img)
    plt.imshow(img, cmap='gray')
    plt.show()


def zoom():
    x = slice(100, 500)
    y = slice(450, 850)
    return [x, y]


if __name__ == "__main__":
    main()
