#!/bin/python3

import numpy as np
import cv2 as cv
import sys

def show_image(image, title = 'Show image'):
    print('> show_image image = resource, title = ' + title)
    cv.imshow(title, image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return

def main(filepath):
    print('> main filepath = ' + filepath)

    show_image(cv.imread(filepath))

if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print("Usage: python3 main.py [image path]");
        exit(1)
    main(sys.argv[1])

