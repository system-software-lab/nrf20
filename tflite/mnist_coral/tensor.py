import collections
import operator
import numpy as np

Class=collections.namedtuple('Class', ['id'])

def input_details(interpreter, key):
    return interpreter.get_input_details()[0][key]

def input_size(interpreter):
    _, height,width, _=input_details(interpreter,'shape')
    return width,height

def input_tensor(interpreter):
    tensor_index=input_details(interpreter,'index')
    return interpreter.tensor(tensor_index)()[0]

def output_tensor(interpreter):
    output_details=interpreter.get_output_details()[0]
    output_data=np.squeeze(interpreter.tensor(output_details['index'])())
    return output_data

def set_input(interpreter,data):
    input_tensor(interpreter)[:,:]=data

def get_output(interpreter):
    scores=output_tensor(interpreter)
    max=0;
    for i in range(9):
        if scores[i+1]>scores[max]:
            max=i+1;
    return max;
       

