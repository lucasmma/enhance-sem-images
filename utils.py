import cv2
from matplotlib import pyplot as plt

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