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
            model_path=model_file,experimental_delegates=[
                tflite.load_delegate(EDGETPU_SHARED_LIB,
                    {'device':device[0]} if device else {})
                ])

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

def main():
    st=time.time()
    #data
    test_images="../../data/t10k-images-idx3-ubyte"
    f=open(test_images,'rb')
    data=_extract_image(f)
    et=time.time()
    print("image.... : ",et-st,'s\n')
    time.sleep(10)
    
    st=time.time()
    #model
    model=sys.argv[1]

    interpreter=make_interpreter(model)
    interpreter.allocate_tensors()
    et=time.time()
    print("infer.... : ",et-st,'s\n')
    time.sleep(10)

    size=tensor.input_size(interpreter)
    st=time.time()
    
    for i in range(10000):
        tensor.set_input(interpreter,data[i])
        interpreter.invoke()
        classes=tensor.get_output(interpreter)

    et=time.time()
    print("infer.... : ",et-st,'s\n')
    
    f.close()


if __name__ == '__main__':
    main()
    time.sleep(15)
