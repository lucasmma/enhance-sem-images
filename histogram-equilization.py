from utils import read_file, show_images, show_histogram, save_file
import cv2
import numpy as np

filenames = ['planta.jpg', 'polen_big.jpg', 'polen.jpg', 'tartigrado.jpg', 'texture.jpg', 'tungstenio.png']

def equilize_histogram (img):
  new_image = cv2.equalizeHist(img)
  return new_image


def main():
  for filename in filenames:
    img = read_file(filename)
    new_img = equilize_histogram(img)
    # show_histogram(img)
    # show_histogram(new_img)
    # show_images([img, new_img])
    save_file(r"results\\histogram-equilization\\" + filename, new_img)

if __name__ == "__main__":
    main()