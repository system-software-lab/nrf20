
from PIL import Image

import tensorflow as tf

import numpy as np

from glob import glob

import time



IMG_SIZE=160
#IMG_SIZE=80

def read_image(path):
  
  image=np.array(Image.open(path))
  return image

def _resize_function(image):
  image = tf.cast(image, tf.float32)
  image.set_shape([None,None,3])
  image = (image/127.5) - 1
  image = tf.image.resize(image, (IMG_SIZE, IMG_SIZE))
  
  return image


class ArtificialDataset(tf.data.Dataset):
  def _generator(num_samples):
    image_list=[]
    #open_file
    data_list=glob('C:\\Users\\user\\Desktop\\tf_mobile\\PetImages_split\\test\\cat\\*.jpg')
    data_list=data_list[:3]
    for i in range(num_samples):
      image_list.append(Image.open(data_list[i]))
    #image=np.array(Image.open(path))
    time.sleep(0.03)

    for sample_idx in range(num_samples):
      image=[]
      #read data from file
      image.append(_resize_function(np.array(image_list[sample_idx])))
      
      time.sleep(0.015)

      yield (sample_idx,image[sample_idx])

  def __new__(cls,num_samples=3):
    return tf.data.Dataset.from_generator(
      cls._generator,
      (tf.float32,tf.float32,tf.float32),
      args=(num_samples,))
      #output_signature=(tf.TensorSpec(shape=(1,IMG_SIZE,IMG_SIZE,3),dtype=tf.float32)))
      #args=(num_samples,))
      
      
  
def benchmark(dataset, num_epochs=2):
  start_time = time.perf_counter()
  for epoch_num in range(num_epochs):
      for sample in dataset:
          print('hello\n')
          # Performing a training step
          time.sleep(0.01)
  print("Execution time:", time.perf_counter() - start_time)

  


def main():
  #2495/'..\\PetImages_split\\test\\cat\\*.jpg'
  #9975/'cat\\*.jpg'

  data_list=glob('C:\\Users\\user\\Desktop\\tf_mobile\\PetImages_split\\test\\cat\\*.jpg')
  for fname in data_list:
      pass
    
  #2494/'..\\PetImages_split\\test\\dog\\*.jpg'
  #9966/'dog\\*.jpg'
    
  data_list2=glob('C:\\Users\\user\\Desktop\\tf_mobile\\PetImages_split\\test\\dog\\*.jpg')
  for fname in data_list:
      pass

  #data_list=data_list+data_list2
  data_list=data_list[:3]
  
  dataset = list(map(read_image,data_list))

  dataset = list(map(_resize_function,dataset))

  #4989
  #19941
  for i in range(4989):
    dataset[i]=tf.expand_dims(dataset[i],0)


  #print(np.shape(dataset))

  datasets = tf.data.Dataset.from_tensor_slices(dataset)
  #print(datasets)

  #test_batches = datasets.shuffle(10).batch(32)
  #print(test_batches)


  model1='saved_model_90'
  model2='saved_model_94'
  model3='saved_model_96'
  model4='saved_model_948'
  
  model5='incept_160'
  #model6='saved_model80'
  st=time.time()
  model=tf.keras.models.load_model(model6)
  et=time.time()
  print('load_model...: ',et-st,'\n')
  
  #output=model.evaluate(datasets)
  st=time.time()
  output=model.predict(x=datasets)
  et=time.time()
  print('predict...: ',et-st,'\n')
  '''
  temp=min(output)
  thursday=temp+((max(output)-temp)/2)
  '''
  thursday=np.median(output)
  #thursday=0.5
  
  print('thursday: ',thursday)

  acc=0

  pos=0
  neg=0

  #2495
  #9975
  for i in range(2495):
    if output[i]<thursday:
      neg=neg+1
    else:
      pos=pos+1
      
  print('cat, pos: ',pos,'neg: ',neg,'\n')
  acc=acc+neg

  pos=0
  neg=0

  #2494
  #9966
  for i in range(2494):
    if output[i+2495]<thursday:
      neg=neg+1
    else:
      pos=pos+1
      
  print('dog, pos: ',pos,'neg: ',neg,'\n')
  acc=acc+pos

  #4989
  #19941
  print('acc: ',acc/4989*100)

  #np.savetxt('save_incept_result.txt',output,fmt='%1.4f')
  
  #print(output)

if __name__=="__main__":
  benchmark(ArtificialDataset())
  #main()

