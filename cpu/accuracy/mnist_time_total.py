import numpy
import tflite_runtime.interpreter as tflite
import platform
import sys
import tensor
import time

EDGETPU_SHARED_LIB = {
  'Linux': 'libedgetpu.so.1',
  'Darwin': 'libedgetpu.1.dylib',
  'Windows': 'edgetpu.dll'
}[platform.system()]

def make_interpreter(model_file):
    model_file, *device=model_file.split('@')
    return tflite.Interpreter(
            model_path=model_file)
                

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

def main():
    start_time = time.process_time()
    #data
    test_images="../../data/t10k-images-idx3-ubyte"
    f=open(test_images,'rb')
    data=_extract_image(f)

    test_labels="../../data/t10k-labels-idx1-ubyte"
    f2=open(test_labels,'rb')
    labels=_extract_label(f2)

    #normalize
    '''
    data=numpy.float32(data)
    data=data/255.0
    '''
    #?
    labels=numpy.int32(labels)

    #model
    model=sys.argv[1]
    #print(model)

    interpreter=make_interpreter(model)
    interpreter.allocate_tensors()

    size=tensor.input_size(interpreter)
    #print(size)
    classe=[]
    '''
    for x in data:
        tensor.set_input(interpreter,x)
        interpreter.invoke()
        classes=tensor.get_output(interpreter)
        classe.append(classes[0])
    '''
    ccc=0;
    for i in range(10000):
        tensor.set_input(interpreter,data[i])
        interpreter.invoke()
        classes=tensor.get_output(interpreter)
        #print(classes)
        if classes!=labels[i]:
            ccc=ccc+1;
    print("ccc:");
    print(ccc)


    f.close()
    f2.close()
    #print(classe)
    total_time = time.process_time() - start_time
    print("total_time: ");
    print(total_time);


if __name__ == '__main__':
    for i in range(1):
        main()
