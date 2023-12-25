from openvino.runtime import Core
import numpy
import time
from PIL import Image
from glob import glob
import sys

def read_image2(path):
    image0=Image.open(path)
    image0=image0.resize((160,160))
    image=numpy.array(image0)
    image0.close()
    #image=tf.cast(image, tf.uint8)
    #image=tf.cast(image, tf.float32)
    #image=(image/127.5)-1
    image=image.astype(numpy.float32)/127.5-1

    return image

def main():

    data_list=glob('./data/cat/*.jpg')
    data_list2=glob('./data/dog/*.jpg')
    data_list=data_list+data_list2
    add='./data/1.jpg'
    data_list.append(add)
    data_list.append(add)
    data_list.append(add)
    dataset = list(map(read_image2,data_list))

    print(len(dataset))
    print(numpy.shape(dataset))


    ie = Core()
    model_path= "./con22/incept_160.xml"
    #model_path= "./model_mj/mobv16.xml"
    model = ie.read_model(model=model_path)
    compiled_model = ie.compile_model(model = model, device_name="MYRIAD")
    output_layer = compiled_model.output(0)
   
    #data0 = dataset[0]
    #data = data0.reshape(1,160,160,3)
    #results = compiled_model(data)[output_layer]
    #results = compiled_model.infer_new_request(dataset)
    #predictions = next(iter(results.values()))
    #print(results)

    nn=4989
    outputs=[]

    for i in range(nn):
        data0 = dataset[i]
        data = data0.reshape(1,160,160,3)
        res = compiled_model(data)[output_layer]
        outputs = outputs + res.flatten().tolist()

    print(numpy.shape(outputs))


    # Acc

    # In[102]:


    outputs=numpy.array(outputs) 
    thursday=numpy.median(outputs.astype(numpy.float32))
    print(thursday)


# res.flatten().tolist()  #[-2.3623740673065186]
# 
# res #array([[-2.362374]], dtype=float32)

# In[103]:


    acc=0
    pos=0
    neg=0


# In[104]:


    for i in range(2495):
        if outputs[i]<thursday:
            neg=neg+1
        else:
            pos=pos+1
        
    acc=acc+neg
    pos = 0 
    neg = 0

    for i in range(2494):
        if outputs[i+2495]<thursday:
            neg=neg+1
        else:
            pos=pos+1
    
    acc=acc+pos
    print('acc: ',acc/4989*100)

if __name__ == '__main__':
    main()
