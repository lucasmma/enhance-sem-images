import cv2

def read_file (filename):
  img = cv2.imread('assets\\' + filename, 0)
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