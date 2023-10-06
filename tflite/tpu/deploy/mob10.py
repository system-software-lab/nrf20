import numpy as np
import tflite_runtime.interpreter as tflite
import platform
import sys
#import tensor
import time
from glob import glob
from PIL import Image
import time

EDGETPU_SHARED_LIB = {
  'Linux': 'libedgetpu.so.1',
  'Darwin': 'libedgetpu.1.dylib',
  'Windows': 'edgetpu.dll'
}[platform.system()]

def make_interpreter(model_file):
    model_file, *device=model_file.split('@')
    return tflite.Interpreter(
            model_path=model_file,experimental_delegates=[
                tflite.load_delegate(EDGETPU_SHARED_LIB,
                    {'device':device[0]} if device else {})
                ])


def read_image(path):
    image0=Image.open(path)
    image0=image0.resize((160,160))
    image=np.array(image0)
    image0.close()
    image=np.expand_dims(image,axis=0)
    
    return image

def main():
    st=time.time()
    #data
    data_list=glob('../../data/cat/*.jpg')
    data_list2=glob('../../data/dog/*.jpg')
    data_list=data_list+data_list2
    
    #st=time.time()
    dataset=list(map(read_image,data_list))
    et=time.time()
    print("image.... : ",et-st,'s\n')
    #et=time.time()

    #print('read 4989 files... :',et-st,'\n')
    time.sleep(10)
    st=time.time()
    #model
    model=sys.argv[1]
    interpreter=make_interpreter(model)
    interpreter.allocate_tensors()
    et=time.time()
    print("model.... : ",et-st,'s\n')
    
    input_details=interpreter.get_input_details()
    output_details=interpreter.get_output_details()

    input_shape=input_details[0]['shape']

    #size=tensor.input_size(interpreter)
    #print(tensor.input_size(interpreter))
    #result=[] 
    
    time.sleep(10)
    st=time.time()
    for i in range(4989):
        interpreter.set_tensor(input_details[0]['index'],dataset[i])
        interpreter.invoke()
        output_data=interpreter.get_tensor(output_details[0]['index'])
        #print("output: %d" % int(output_data[0][0]))
        #result.append(int(output_data[0][0]))
    
    et=time.time()
    print("infer.... : ",et-st,'s\n')
    #print("infer finished\n")
    '''
    thursday=np.median(result)
    acc=0
    pos=0
    neg=0
    #2495
    #9975
    for i in range(2495):
      if result[i]<thursday:
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
      if result[i+2495]<thursday:
        neg=neg+1
      else:
        pos=pos+1
      
    print('dog, pos: ',pos,'neg: ',neg,'\n')
    acc=acc+pos

    #4989
    #19941
    print('acc: ',acc/4989*100)
    '''   

'''
    textfile=open("result_file.txt","w")
    for element in result:
        textfile.write(str(element)+"\n")
    textfile.close()
'''

if __name__ == '__main__':
    main()
    time.sleep(15)
