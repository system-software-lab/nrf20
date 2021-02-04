import numpy
import tensorflow as tf
from tensorflow import keras


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
        data=data.reshape(num_images,1,rows,cols,1)
        return data

def representative_dataset():
  #data
  test_images="t10k-images.idx3-ubyte"
  f=open(test_images,'rb')
  data=_extract_image(f)
  data=numpy.float32(data)
  images=data
  for data in tf.data.Dataset.from_tensor_slices((images)).batch(1).take(1):
      yield(list(data))
    #yield [data.astype(tf.float32)]

converter = tf.lite.TFLiteConverter.from_saved_model("saved_model_X_quant")

converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.representative_dataset = representative_dataset
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
converter.inference_input_type = tf.int8  # or tf.uint8
converter.inference_output_type = tf.int8  # or tf.uint8
tflite_quant_model = converter.convert()

#save the model

with open('mnist7.tflite','wb') as f:
    f.write(tflite_quant_model)



#a=representative_dataset()
#print(list(a))

