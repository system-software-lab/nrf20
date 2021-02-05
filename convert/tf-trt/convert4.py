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
        #data=data.reshape(num_images,1,1,rows,cols)
        data=data.reshape(num_images,rows,cols,1)
        #data=data.reshape(num_images,1,rows,cols,1)
        #data=data.reshape(num_images,-1,rows,cols,1)
        return data

def config_gpu_memory():
  gpu_mem_cap=0;  
  gpus=tf.config.experimental.list_physical_devices('GPU')
  if not gpus:
    return
  print('Found the following GPUs:')
  for gpu in gpus:
    print(' ', gpu)
  for gpu in gpus:
    try:
      if not gpu_mem_cap:
        tf.config.experimental.set_memory_growth(gpu, True)
      else:
        tf.config.experimental.set_virtual_device_configuration(
            gpu,
            [tf.config.experimental.VirtualDeviceConfiguration(
               memory_limit=gpu_mem_cap)])
    except RuntimeError as e:
      print('Can not set GPU memory config', e)

print('Converting to TF-TRT FP32...')
config_gpu_memory()
conversion_params = trt.DEFAULT_TRT_CONVERSION_PARAMS._replace(precision_mode=trt.TrtPrecisionMode.FP32,max_workspace_size_bytes=4000000000)

converter = trt.TrtGraphConverterV2(input_saved_model_dir='saved_model_X_quant',conversion_params=conversion_params)
converter.convert()

def my_input_fn():

    test_images="t10k-images-idx3-ubyte"
    f=open(test_images,'rb')
    data=_extract_image(f)
    data=numpy.float32(data)
    data=data/255.0
    data=tf.convert_to_tensor(value=tf.compat.v1.get_variable( "data", initializer=tf.constant(data)))
    i=0
    for image in data:
        print(i,"\n")
        i=i+1
        yield(image)
    #Inp1=np.random.normal(size=(-1,28,28,1)).astype(np.float32)
    #yield(Inp1)
converter.build(input_fn=my_input_fn)
converter.save(output_saved_model_dir='mnist9_TFTRT_FP32')
print('Done Converting to TF-TRT FP32')
