import cv2
from matplotlib import pyplot as plt
import numpy as np

def read_file (filename):
  img = cv2.imread('assets\\' + filename, cv2.IMREAD_GRAYSCALE)
  return img

def read_files(filenames):
  files = []
  
  for filename in filenames:
    files.append(read_file(filename))

  return files

def save_file(filename, img):
  cv2.imwrite(filename, img)

def save_files(images):
  for image in images:
    save_file(image[0], image[1])

def show_images(images):
  for i in range(0, len(images)):
    cv2.imshow('image {}'.format(i), images[i])
  cv2.waitKey(0)
  cv2.destroyAllWindows()

def show_histogram(img):
  plt.hist(img.ravel(),256,[0,256])
  plt.show()

def resize_img(img, width, height):
  cv2.resize(img, (width, height))

def neighbors(img, radius, rowNumber, columnNumber):
     return [[img[i][j] if  i >= 0 and i < len(img) and j >= 0 and j < len(img[0]) else 0
                for j in range(columnNumber-radius, columnNumber+radius+1)]
                    for i in range(rowNumber-radius, rowNumber+radius+1)]

def mean_standard_deviation(img):
  mean = img.mean()
  # standard_deviation = ((((np.std(img)) ** 2) * len(img) * len(img[0])) / ((len(img) * len(img[0])) - 1) ) ** (1/2)
  standard_deviation = np.std(img)
  return mean, standard_deviation