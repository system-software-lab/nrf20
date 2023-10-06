# Loads the IR file (.xml) and does inference on MYRIAD device
# This needs python3
import numpy
import time
from PIL import Image
from glob import glob
import sys
#from openvino.inference_engine import IENetwork, IECore

DEVICE = "MYRIAD"

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

try:
    from openvino.inference_engine import IENetwork, IECore
except:
    print('\nPlease make sure your OpenVINO environment variables are set by sourcing the `setupvars.sh` script found in <your OpenVINO install location>/bin/ folder.\n')
    exit(1)


def main():
    #data
    #2495
    stt = time.time()
    data_list=glob('../data/cat/*.jpg')
    data_list2=glob('../data/dog/*.jpg')
    data_list=data_list+data_list2
    add='../data/1.jpg'
    data_list.append(add)
    data_list.append(add)
    data_list.append(add)
    dataset = list(map(read_image2,data_list))
    total_time=time.time()-stt
    print('read_image: ',total_time,'\n')
    time.sleep(10)
    #print(dataset)
    
    #dataset=numpy.expand_dims(dataset,axis=1)
    #print(numpy.shape(dataset))
    #print(dataset)
    #for i in range(4992):
    #    dataset[i]=dataset[i].reshape(1,3,160,160)
    
    #print(numpy.shape(dataset))
    
    #return 
    # Select the myriad plugin and IRs to be used
    #ir = './mobv1_ov5/saved_model.xml'
    #ir = './oto/mobv1.xml'
    stt = time.time()
    ir = sys.argv[1]
    ie = IECore()
    #net = IENetwork(model = ir, weights = ir[:-3] + 'bin')
    net = ie.read_network(model = ir, weights = ir[:-3] + 'bin')


    # Set up the input and output blobs
    #input_blob = next(iter(net.inputs))
    input_blob = next(iter(net.input_info))
    output_blob = next(iter(net.outputs))
    #input_shape = net.input_info[input_blob].shape
    input_shape = net.input_info[input_blob].input_data.shape
    #print(input_shape)
    net.batch_size=32
    #print(net.batch_size)
    output_shape = net.outputs[output_blob].shape


    # Load the network and get the network shape information
    exec_net = ie.load_network(network = net, device_name = DEVICE)
    #n, c = input_shape
    total_time=time.time()-stt
    print('load_model: ',total_time,'\n')
    time.sleep(10)


    # Predict
    hop=32
    #nn=int(2495/hop)+1
    nn=156
    #nn=int(4992/hop)
    st=0
    end=hop
   
    #n_iterations = 1
    #n_iterations = 10
    count=0
    stt = time.time()
    #outputs=[]
    for i in range(nn):
        res = exec_net.infer({input_blob: dataset[st:end]})
        #outputs=outputs+numpy.array(res[output_blob]).flatten().tolist()
        st=end
        end=end+hop

    total_time=time.time()-stt
    print('infer time: ',total_time,'\n')
    #print(len(outputs))
    
    #numpy.savetxt('openvino_result_jetson2.txt',outputs,fmt='%1.4f')
    #return

    '''
    outputs=numpy.array(outputs) 
    thursday=numpy.median(outputs.astype(numpy.float32))
  
    print('thursday: ',thursday)

    acc=0

    pos=0
    neg=0

    #2495
    #9975
    #print(output)
    for i in range(2495):
      if outputs[i]<thursday:
        neg=neg+1
      else:
        pos=pos+1
      
    print('cat, pos: ',pos,'neg: ',neg,'\n')
    acc=acc+neg
    #np.savetxt('save96_result_jetson.txt',output,fmt='%1.4f')


    pos=0
    neg=0

    #2494
    #9966
    for i in range(2494):
      if outputs[i+2495]<thursday:
        neg=neg+1
      else:
        pos=pos+1
      
    print('dog, pos: ',pos,'neg: ',neg,'\n')
    acc=acc+pos

    #4989
    #19941
    print('acc: ',acc/4989*100)

    '''
    #print(outputs)
    # print( 'r=', r )
    # print( 'res[output_blob] = ', output_logits.argmax() )
    # print( 'ground truth = ', y_test[r], )
    # print( '' )
    # cv2.imshow( 'test image', x_test[r,:,:].astype('uint8') )
    # cv2.waitKey(0)
    #print( '%d iterations took %4.4f ms' %(n_iterations,  1000. * ( time.time() - st ) ) )
    
if __name__ == '__main__':
    main()
    time.sleep(10)
