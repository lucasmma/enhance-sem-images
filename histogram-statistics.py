from utils import read_file, show_images
import cv2
import numpy as np

def neighbors(img, radius, rowNumber, columnNumber):
     return [[img[i][j] if  i >= 0 and i < len(img) and j >= 0 and j < len(img[0]) else 0
                for j in range(columnNumber-1-radius, columnNumber+radius)]
                    for i in range(rowNumber-1-radius, rowNumber+radius)]

def mean_standard_deviation(img):
  mean, standard_deviation = cv2.meanStdDev(img)
  return mean[0][0], standard_deviation[0][0]

def histogram_statistics (img, E, k0, k1, k2):
  new_img = []
  global_mean, standard_deviation = mean_standard_deviation(img)
  
  for x in range(len(img)):
    row = img[x]
    new_row = []
    for y in range(len(row)):
      pixel = row[y]
      local_image = neighbors(img, 1, x, y)
      local_mean, local_standard_deviation = mean_standard_deviation(np.uint8(local_image))

      if (local_mean <= k0 * global_mean) and (k1 * standard_deviation <= local_standard_deviation and local_standard_deviation <= k2 * standard_deviation):
        new_row.append(E * pixel)
      else:
        new_row.append(pixel)
    new_img.append(new_row)

  return np.uint8(new_img)


def main():
  img = read_file("tungstenio.png")
  print(img)
  new_img = histogram_statistics(img, E=4, k0=0.95, k1=0.04,  k2=0.95)
  print(new_img)
  show_images([img, new_img])


if __name__ == "__main__":
    main()