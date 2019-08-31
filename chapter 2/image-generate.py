import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def convert_bit(img_file='../pics/street.jpg'):
    """
    convert image to different bits
    :param img_file:
    :return:
    """
    img = Image.open(img_file)
    # print(np.asarray(img).shape)
    print(img.mode)

    # 1 bit gray image
    img_bit1_gray = img.convert('1')
    print(img_bit1_gray.mode)

    # 8 bit gray image
    img_bit8_gray = img.convert('L')
    print(img_bit8_gray.mode)

    # 32 bit gray image
    img_bit32_gray = img.convert('I')
    print(img_bit32_gray.mode)

    # 8 bit colorful image
    img_bit8_color = img.convert('P')

    # 24 bit colorful image
    img_bit24_color = img.convert('RGBA')

    # 32 bit colorful image
    img_bit32_color = img.convert('CMYK')

    # img_bit1_gray.show()
    # img_bit8_gray.show()
    # img_bit24_color.show()
    # img_bit8_gray.show()
    # img_bit32_gray.show()
    plt.subplot(3, 3, 1)
    plt.imshow(img)
    plt.subplot(3, 3, 2)
    plt.imshow(img_bit1_gray)
    plt.subplot(3, 3, 3)
    plt.imshow(img_bit8_gray)
    plt.subplot(3, 3, 4)
    plt.imshow(img_bit32_gray)
    plt.subplot(3, 3, 5)
    plt.imshow(img_bit8_color)
    plt.subplot(3, 3, 6)
    plt.imshow(img_bit24_color)
    plt.subplot(3, 3, 7)
    plt.imshow(img_bit32_color)

    plt.show()

convert_bit()