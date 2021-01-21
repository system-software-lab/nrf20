## Build MNIST

- /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/mnist/

[1.](https://github.com/system-software-lab/nrf20/blob/main/vino119/mnist/main.cpp) main.cpp

[2.](https://github.com/system-software-lab/nrf20/blob/main/vino119/mnist/CMakeLists.txt) CMakeLists.txt

- /home/pi/build/

`
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_FLAGS="-march=armv7-a" /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/mnist
`

( Debug, Release, RelWithDebInfo )



`
make -j2 mnist
`

[1.](https://github.com/system-software-lab/nrf20/blob/main/vino119/saved_model.xml) saved_model.xml(IR model)

[2.](https://github.com/system-software-lab/nrf20/blob/main/vino119/saved_model.bin) saved_model.bin(IR model)

[3.](https://github.com/system-software-lab/nrf20/blob/main/vino119/t10k-images-idx3-ubyte) t10k-images-idx3-ubyte(image data)

[4.](https://github.com/system-software-lab/nrf20/blob/main/vino119/t10k-labels-idx1-ubyte) t10k-labels-idx1-ubyte(label data, accuracy->main888.cpp)


`
./armv7l/Release/mnist saved_model.xml t10k-images-idx3-ubyte t10k-labels-idx1-ubyte
`

