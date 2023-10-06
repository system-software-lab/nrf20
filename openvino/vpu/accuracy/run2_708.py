# Loads the IR file (.xml) and does inference on MYRIAD device
# This needs python3
import numpy
import time
DEVICE = "MYRIAD"

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
        data=data.reshape(num_images,rows,cols)
        return data
    
def _extract_label(f):
    with f as bytestream:
        magic=_read32(bytestream)
        num_items=_read32(bytestream)
        buf=bytestream.read(num_items)
        labels=numpy.frombuffer(buf,dtype=numpy.uint8)
        return labels

try:
    from openvino.inference_engine import IENetwork, IECore
except:
    print('\nPlease make sure your OpenVINO environment variables are set by sourcing the `setupvars.sh` script found in <your OpenVINO install location>/bin/ folder.\n')
    exit(1)


def main():
    st = time.time()
    #data
    test_images="./../data/t10k-images-idx3-ubyte"
    f=open(test_images,'rb')
    x_test=_extract_image(f)
    x_test=numpy.expand_dims(x_test,axis=3)
    #print(numpy.shape(x_test[0:40]))
    #return 

    test_labels="./../data/t10k-labels-idx1-ubyte"
    f2=open(test_labels,'rb')
    y_test=_extract_label(f2)
    y_test=numpy.int32(y_test)
    
    # Select the myriad plugin and IRs to be used
    ir = './../model/mnist.xml'
    ie = IECore()
    net = ie.read_network(model = ir, weights = ir[:-3] + 'bin')

    #set_blobs, batch size
    input_blob = next(iter(net.input_info))
    output_blob = next(iter(net.outputs))
    input_shape = net.input_info[input_blob].input_data.shape
    print(input_shape)
    net.batch_size=10000
    print(net.batch_size)
    output_shape = net.outputs[output_blob].shape


    # Load the network and get the network shape information
    exec_net = ie.load_network(network = net, device_name = DEVICE)
    #n, c = input_shape
    total_time=time.time()-st
    print('image,model_time: ',total_time)

    time.sleep(10)

    # Predict
    outputs=[]
    
    st = time.time()
    res = exec_net.infer({input_blob: x_test})
    outputs=numpy.array(res[output_blob]).flatten().tolist()
    #print(len(outputs))
    total_time=time.time()-st
    print('total_time: ',total_time)
    
    cc=0
    hop=10
    st=0
    end=hop
    for i in range(10000):
        temp=outputs[st:end]
        if temp.index(max(temp))!=y_test[i]:
            cc=cc+1
        st=end
        end=end+hop
    print(cc)
    print("accuracy: ",(10000-cc)/100,"%\n")        
if __name__ == '__main__':
    #time.sleep(10)
    for i in range(1):
        main()
        #time.sleep(10)
