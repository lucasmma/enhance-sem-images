from utils import read_file, show_images, show_histogram
import cv2
import numpy as np

def constrast_streching (img):
  counts = np.bincount(img.flatten())
  # high = np.argmax(counts)
  # low = np.argmin(counts)
  high = np.max(img)
  low = np.min(img)
  alpha = 255 / (high - low)
  print(high)
  print(low)
  print(alpha)
  new_image = np.multiply(np.subtract(img, low), alpha)

  return np.uint8(new_image)


def main():
  img = read_file("planta.jpg")
  new_img = constrast_streching(img)
  # show_histogram(img)
  # show_histogram(new_img) 
  show_images([img, new_img])


if __name__ == "__main__":
    main()