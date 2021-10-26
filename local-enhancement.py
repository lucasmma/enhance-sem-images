from utils import read_file, show_images, neighbors, mean_standard_deviation
import cv2
import numpy as np

def localEnhancement (img, k, b):
  new_img = []
  global_mean, standard_deviation = mean_standard_deviation(img)
  
  for x, row in enumerate(img):
    new_row = []
    for y, pixel in enumerate(row):
      local_image = neighbors(img, 1, x, y)
      local_mean, local_standard_deviation = mean_standard_deviation(np.uint8(local_image))

      a_value = k * global_mean / (local_standard_deviation + b)

      new_value = a_value *  (pixel - local_mean) + local_mean

      new_row.append(new_value)
    new_img.append(new_row)

  return np.uint8(new_img)


def main():
  img = read_file("tartigrado.jpg")

  new_img = localEnhancement(img, 0.23, 2)

  show_images([img, new_img])


if __name__ == "__main__":
    main()