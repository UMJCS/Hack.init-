#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import numpy as np

from PIL import ImageFilter
from PIL import ImageEnhance
from PIL import Image
import random
import skimage.io as skio
from skimage.color import rgb2gray

def load_np_image(infilename):
    img = Image.open(infilename)
    img.load()
    data = np.asarray(img, dtype="int32" )
    return data

def load_image(infilename):
    return Image.open(infilename)

def save_image(npdata, outfilename):
    img = Image.fromarray(np.asarray(np.clip(npdata, 0, 255), dtype="uint8"))
    img.save(outfilename)

def make_blur_img(img_data):
    return img_data.filter(ImageFilter.BLUR)

def make_bright_img(img_data):
    return ImageEnhance.Brightness(img_data).enhance(1.5)

def make_clr_chg(img_data):
    return ImageEnhance.Color(img_data).enhance(0.6)

def make_contrast_chg(img_data):
    return ImageEnhance.Contrast(img_data).enhance(0.6)

def make_rot_img(img_data):
    return img_data.rotate(90)

def make_flip_img(img_data):
    return Image.fromarray(np.fliplr(img_data))

def make_noise_img(img_data):
    data = np.asarray(img_data, dtype="int32")
    array_shape = data.shape
    noise = np.random.randint(1, 80, size=array_shape)
    data += noise
    data = Image.fromarray(np.asarray(np.clip(data, 0, 255), dtype="uint8"))
    return data

class MyGaussianBlur(ImageFilter.Filter):
    name = "GaussianBlur"

    def __init__(self, radius=2, bounds=None):
        self.radius = radius
        self.bounds = bounds

    def filter(self, image):
        if self.bounds:
            clips = image.crop(self.bounds).gaussian_blur(self.radius)
            image.paste(clips, self.bounds)
            return image
        else:
            return image.gaussian_blur(self.radius)

def make_gaussian_blur_img(img_data):
    return img_data.filter(MyGaussianBlur(radius=1))

def augment_image(image):
    im = image
    image_merge = []
    image_merge.append(im)
    image_merge.append(make_bright_img(im))
    image_merge.append(make_clr_chg(im))
    image_merge.append(make_contrast_chg(im))
    image_merge.append(make_noise_img(im))
    image_merge.append(make_gaussian_blur_img(im))
    im_flip = make_flip_img(im)
    image_merge.append(im_flip)
    image_merge.append(make_bright_img(im_flip))
    image_merge.append(make_clr_chg(im_flip))
    image_merge.append(make_contrast_chg(im_flip))
    image_merge.append(make_noise_img(im_flip))
    image_merge.append(make_gaussian_blur_img(im_flip))
    return image_merge

def process_0_1(img):
    im = img
    for r in range(img.shape[0]):
        for c in range(img.shape[1]):
            if im[r][c] > 100:
                im[r][c] = 1
            else:
                im[r][c] = 0
    #print img
    return im

def augment_image_label(image):
    labels = []
    im = np.asarray(image)
    for i in range(6):
        labels.append(im)
    label_flip = make_flip_img(im)
    for i in range(6):
        labels.append(label_flip)
    return labels

def test():
    image = '00001.png'
    if not os.path.exists('./tmp/'):
        os.mkdir('./tmp/')
    #make_rot_img(image, 'tmp/')
    img = Image.open(image)
    images = augment_image(img)
    for i, im in enumerate(images):
        skio.imsave('tmp/' + str(i) + '.png', im)

def test2():
    im = skio.imread('00013_matte.png')
    print im
    im_gray = rgb2gray(im)
    print im_gray
    zeros_and_ones = np.asarray(make_flip_img(im_gray), dtype="int32" )
    print zeros_and_ones


if __name__ == "__main__":
    test()
    #test2()
