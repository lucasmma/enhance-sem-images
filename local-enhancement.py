from utils import read_file, show_images
import cv2
import numpy as np

def localEnhancement (img):
  clahe = cv2.createCLAHE(clipLimit=1.8, tileGridSize=(8, 8))
  new_img = clahe.apply(img)
  return new_img


def main():
  img = read_file("polen_big.jpg")

  new_img = localEnhancement(img)

  show_images([img, new_img])


if __name__ == "__main__":
    main()