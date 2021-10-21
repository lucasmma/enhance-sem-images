import cv2


def read_file (filename):
  img = cv2.imread('assets\\' + filename, 0)
  return img

def save_file(filename, img):
  cv2.imwrite(filename, img)