#convert3.py

import numpy
import tensorflow as tf
from tensorflow.python.compiler.tensorrt import trt_convert as trt
import sys

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
        
def get_func_from_saved_model(saved_model_dir):
  saved_model_loaded = tf.saved_model.load(
      saved_model_dir, tags=[tag_constants.SERVING])
  graph_func = saved_model_loaded.signatures[
      signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY]
  graph_func = convert_to_constants.convert_variables_to_constants_v2(graph_func)
  return graph_func

def get_graph_func(input_saved_model_dir,mode):
#input_saved_model_dir -> 1. tensorflow saved_model: convert 2. tf-trt saved_model: deploy
  graph_func = get_func_from_saved_model(input_saved_model_dir)
  conversion_params=trt.DEFAULT_TRT_CONVERSION_PARAMS._replace(precision_mode=trt.TrtPrecisionMode.FP32,max_workspace_size_bytes=8000000000)
  if mode==1:
    converter=trt.TrtGraphConverterV2(
        input_saved_model_dir=input_saved_model_dir,
        conversion_params=conversion_params,
    )
    def my_input_fn():
        #read_data(train_data)
        #train_data
        train_images="train-images-idx3-ubyte"
        f3=open(train_images,'rb')
        convert_data=_extract_image(f3)
        
        #iterate_data(60000?)
        for image in convert_data:
            yield(image)
            
    print('Graph conversion...')
    converter.convert()
    print('Building TensorRT engines...')
    converter.build(input_fn=my_input_fn)
    #output_directory
    output_saved_model_dir='mnist3_TFTRT_FP32'
    converter.save(output_saved_model_dir=output_saved_model_dir)
    print('Done Converting to TF-TRT FP32')
    graph_func = get_func_from_saved_model(output_saved_model_dir)
  return graph_func
  
def run_inference(graph_func):
   predictions={}
   #read_data(test_data)
   input_dtype = graph_func.inputs[0].dtype
   #test_data
   test_images="t10k-images-idx3-ubyte"
   f=open(test_images,'rb')
   data=_extract_image(f)
   
   for image in data:
        batch_preds=graph_func(image)
        for key in batch_preds.keys():
        if key not in predictions:
          predictions[key] = [batch_preds[key]]
        else:
          predictions[key].append(batch_preds[key])
          
   f.close()
   return predictions
   
if __name__ == '__main__':
   #gpu_memory config???
   

   
   #label
   test_labels="t10k-labels-idx1-ubyte"
   f2=open(test_labels,'rb')
   labels=_extract_label(f2)
   
   input_saved_model_dir=sys.argv[1]
   mode=sys.argv[2]
   graph_func=get_graph_func(input_saved_model_dir, mode)
   prediction=run_inference(graph_func)
   #process_output
   
   print('Result:')

   f2.close()
    

