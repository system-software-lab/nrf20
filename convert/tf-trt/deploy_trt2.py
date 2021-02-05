#deploy_trt.py

from __future__ import absolute_import, division, print_function, unicode_literals
import os
import time

import numpy
import tensorflow as tf
from tensorflow import keras
from tensorflow.python.compiler.tensorrt import trt_convert as trt
from tensorflow.python.saved_model import tag_constants
from tensorflow.python.saved_model import signature_constants
from tensorflow.python.framework import convert_to_constants

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
        #data=data.reshape(num_images,1,rows,cols)
        #data=data.reshape(num_images,1,rows,cols,1)
        #data=data.reshape(num_images,-1,rows,cols,1)
        return data

def _extract_label(f):
    with f as bytestream:
        magic=_read32(bytestream)
        num_items=_read32(bytestream)
        buf=bytestream.read(num_items)
        labels=numpy.frombuffer(buf,dtype=numpy.uint8)
        return labels
def get_func_from_saved_model(saved_model_dir):
  saved_model_loaded = tf.saved_model.load(
      saved_model_dir, tags=[tag_constants.SERVING])
  graph_func = saved_model_loaded.signatures[
      signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY]
  graph_func = convert_to_constants.convert_variables_to_constants_v2(graph_func)
  return graph_func

def run_inference(graph_func):
   #predictions={}
   #read_data(test_data)
   input_dtype = graph_func.inputs[0].dtype
   #test_data
   test_images="t10k-images-idx3-ubyte"
   f=open(test_images,'rb')
   data=_extract_image(f)
   data=numpy.float32(data)
   data=data/255.0
   data=numpy.expand_dims(data,axis=1)
   data=tf.convert_to_tensor(value=tf.compat.v1.get_variable( "data", initializer=tf.constant(data)))
   #data=tf.reshape(data,[-1,28,28,1])

    #expect batch dimension
   batch_preds=graph_func(data[0])
   print(batch_preds)
   '''
   for key in batch_preds.keys():
       print(key)
       if key not in predictions:
           predictions[key] = [batch_preds[key]]
       else:
           predictions[key].append(batch_preds[key])
   '''
   result=list(batch_preds.numpy())
   #result=list(batch_preds)
   result=result.index(max(result))
   #predictions.append(result)
   
   f.close()
   return result

def config_gpu():
    gpus=tf.config.experimental.list_physical_devices('GPU')
    if not gpus:
        return
    print('Found the following GPUs:')
    for gpu in gpus:
        print('',gpu)
    for gpu in gpus:
        try:
            tf.config.experimental.set_memory_growth(gpu,True)
        except RuntimeError as e:
            print('Cant not set GPU memory config',e)
#data
test_images="t10k-images-idx3-ubyte"
f=open(test_images,'rb')
data=_extract_image(f)

test_labels="t10k-labels-idx1-ubyte"
f2=open(test_labels,'rb')
labels=_extract_label(f2)

#normalize
#data=numpy.float32(data)
#data=data/255.0
#?
labels=numpy.int32(labels)

#graph_func = get_func_from_saved_model('mnist_TFTRT_FP32')
#graph_func = get_func_from_saved_model('saved_model_X_quant')
#edit->convert_to_constant

config_gpu()
#graph_func = get_func_from_saved_model('mnist44_TFTRT_FP32')
graph_func = get_func_from_saved_model('mnist9_TFTRT_FP32')
result=run_inference(graph_func)
print('result: ',result,'\n')

#for aa in range(10):
#    print(result[aa],"\n")

#for node in graph_func.node:
#    print(node.op)
'''
saved_model_loaded = tf.saved_model.load('mnist_TFTRT_FP32', tags=[tag_constants.SERVING])
signature_keys = list(saved_model_loaded.signatures.keys())
print(signature_keys)


infer = saved_model_loaded.signatures['serving_default']
print(infer.structured_outputs)
x=tf.convert_to_tensor(data[0],dtype=tf.float32)
labeling = infer(x)

a=list(labeling)
print(a)
'''


