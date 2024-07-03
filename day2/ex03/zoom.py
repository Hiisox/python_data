import matplotlib.pyplot as plt
from load_image import load_image


def main():
    img = load_image("animal.jpeg")
    if img is None:
        return
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
