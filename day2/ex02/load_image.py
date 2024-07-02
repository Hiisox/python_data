from PIL import Image
import numpy as np
def ft_load(path: str) -> list:
	try :
		img = Image.open(path)
	except:
		print("AssertionError: wrong image's path")
		return None
	img_array = np.array(img)
	print(f"The shape of image is: {img_array.shape}")
	return img_array


print(ft_load("landscape.jpg"))