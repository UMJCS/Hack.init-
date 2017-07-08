# -*- coding: utf-8 -*-

import cPickle
import numpy
from PIL import Image
from labelFile2Map import *

i = 0;

images = numpy.empty((60000,784))
labels = numpy.empty(60000)

image_root = "../MNIST_data/"
train_label = "../MNIST_data/mnist_train/train.txt"
test_label = "../MNIST_data/mnist_train/test.txt"

def process_train():
    lines = readLines(train_label)
    label_record = map(lines)
    train_dir = image_root + "mnist_train/"
    print len(label_record)
    index = 0
    for name in label_record:
        # print label_record[name]
        image = Image.open(train_dir + str(label_record[name]) + '/' + name)
        print "processing %d: " % index + train_dir + str(label_record[name]) + '/' + name

        img_ndarray = numpy.asarray(image, dtype='float64') / 256
        images[index] = numpy.ndarray.flatten(img_ndarray)
        labels[index] = numpy.int(label_record[name])

        write_file = open('../PKLDataset/olivettifaces.pkl', 'wb')
        cPickle.dump(images, write_file, -1)
        cPickle.dump(labels, write_file, -1)
        write_file.close()
        index = index + 1
    pass

if __name__ == "__main__":
    process_train()