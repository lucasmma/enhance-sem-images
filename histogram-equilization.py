from utils import read_file, show_images, show_histogram
import cv2
import numpy as np

def equilize_histogram (img):
  new_image = cv2.equalizeHist(img)
  return new_image


def main():
  img = read_file("planta.jpg")
  new_img = equilize_histogram(img)
  show_histogram(img)
  show_histogram(new_img)
  show_images([img, new_img])


if __name__ == "__main__":
    main()