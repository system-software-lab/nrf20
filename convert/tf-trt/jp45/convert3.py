#convert3.py

import tensorflow as tf
import numpy
from tensorflow.python.compiler.tensorrt import trt_convert as trt

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
        #data=data.reshape(num_images,1,rows,cols)
        #data=data.reshape(num_images,rows,cols)
        #data=data.reshape(num_images,1,rows,cols,1)
        data=data.reshape(num_images,-1,rows,cols,1)
        return data

print('Converting to TF-TRT FP32...')
conversion_params = trt.DEFAULT_TRT_CONVERSION_PARAMS._replace(precision_mode=trt.TrtPrecisionMode.FP32,max_workspace_size_bytes=8000000000)

converter = trt.TrtGraphConverterV2(input_saved_model_dir='saved_model_X_quant',conversion_params=conversion_params)
converter.convert()

def my_input_fn():

    test_images="t10k-images-idx3-ubyte"
    f=open(test_images,'rb')
    data=_extract_image(f)
    data=numpy.float32(data)
    data=data/255.0
    i=0
    for image in data:
        print(i,"\n")
        i=i+1
        yield(image)
    #Inp1=np.random.normal(size=(-1,28,28,1)).astype(np.float32)
    #yield(Inp1)
converter.build(input_fn=my_input_fn)
converter.save(output_saved_model_dir='mnist3_TFTRT_FP32')
print('Done Converting to TF-TRT FP32')
