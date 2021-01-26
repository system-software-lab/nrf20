from __future__ import absolute_import, division, print_function, unicode_literals
import os
import time

import numpy
import tensorflow as tf
from tensorflow import keras
from tensorflow.python.compiler.tensorrt import trt_convert as trt
from tensorflow.python.saved_model import tag_constants

def _read32(bytestream):
    dt=numpy.dtype(numpy.uint32).newbyteorder('>')
    return numpy.frombuffer(bytestream.read(4),dtype=dt)[0]

def _extract_image(f):
    with f as bytestream:
        magic=_read32(bytestream)
        #print(magic)
        num_images=_read32(bytestream)
        rows=_read32(bytestream)
        cols=_read32(bytestream)
        buf=bytestream.read(rows*cols*num_images)
        data=numpy.frombuffer(buf,dtype=numpy.uint8)
        data=data.reshape(num_images,rows,cols,1)
        return data

def _extract_label(f):
    with f as bytestream:
        magic=_read32(bytestream)
        num_items=_read32(bytestream)
        buf=bytestream.read(num_items)
        labels=numpy.frombuffer(buf,dtype=numpy.uint8)
        return labels
#data
test_images="t10k-images-idx3-ubyte"
f=open(test_images,'rb')
data=_extract_image(f)

test_labels="t10k-labels-idx1-ubyte"
f2=open(test_labels,'rb')
labels=_extract_label(f2)

#normalize
data=numpy.float32(data)
data=data/255.0
#?
labels=numpy.int32(labels)

model=tf.keras.models.load_model('saved_model_X_quant')
output=model.predict(x=data)
#a=output[1]
#a=list(a)

#print(a.index(max(a)))

count=0
for i in range(10000):
    a=output[i]
    a=list(a)
    if a.index(max(a))!=labels[i]:
        count=count+1
print(count)
