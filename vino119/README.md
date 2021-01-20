## Build MNIST

- /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/mnist

[1.](https://github.com/system-software-lab/nrf20/blob/main/vino119/mnist/main.cpp) main.cpp

[2.](https://github.com/system-software-lab/nrf20/blob/main/vino119/mnist/CMakeLists.txt) CMakeLists.txt

- /home/pi/build

`
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_FLAGS="-march=armv7-a" /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/mnist
`

( Debug, Release, RelWithDebInfo )



`
make -j2 mnist
`

