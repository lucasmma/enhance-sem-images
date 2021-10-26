from utils import read_file, show_images, neighbors, mean_standard_deviation
import cv2
import numpy as np

def histogram_statistics (img, E, k0, k1, k2):
  new_img = []
  global_mean, standard_deviation = mean_standard_deviation(img)
  
  for x, row in enumerate(img):
    new_row = []
    for y, pixel in enumerate(row):
      local_image = neighbors(img, 1, x, y)
      local_mean, local_standard_deviation = mean_standard_deviation(np.uint8(local_image))
      # if x == len(img) - 2 and y == 1:
        # print(local_image)
        # print(img)
        # print(local_mean, local_standard_deviation)
        # return
      if (local_mean <= (k0 * global_mean)) and ((k1 * standard_deviation) <= local_standard_deviation and local_standard_deviation <= (k2 * standard_deviation)):
        # print(x, y, "->", pixel, E * pixel)
        new_row.append(E * pixel)
        # new_row.append(255)
      else:
        new_row.append(pixel)
    new_img.append(new_row)

  return np.uint8(new_img)


def main():
  img = read_file("tungstenio.png")
  # new_img = histogram_statistics(img, E=5.5, k0=0.4, k1=0.04,  k2=0.95)
  # new_img = histogram_statistics(img, E=5.5, k0=0.95, k1=0.040,  k2=0.95)
  new_img = histogram_statistics(img, E=3, k0=0.2, k1=0.01,  k2=0.8)
  show_images([img, new_img])


if __name__ == "__main__":
    main()