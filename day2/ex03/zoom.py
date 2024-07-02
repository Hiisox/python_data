import numpy as np
import matplotlib.pyplot as plt
from load_image import load_image
def main() :
	img = load_image("animal.jpeg")
	print(img)
	# if img == None :
	# 	return
	print("coqkwnqdqiqwndnqwdqwind")
	plt.imshow(img)
if __name__ == "__main__" :
	main()