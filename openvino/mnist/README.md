- main9.cpp -> main88.cpp

  read label

- main88.cpp -> main8.cpp

  process output

- main8.cpp -> main888.cpp

  check accuracy
  normalize O, quantize X

 normalized test data | accuracy
 ---------------------|------
 O|87.92%
 X|87.17%


- main888.cpp -> main77.cpp

  normalize X

- main888.cpp -> main7.cpp

  Precision inputPrecision = Precision::U8;
  openvino input: FP16, FP32

- main7.cpp -> main6.cpp

  time(μs)
  [time_result](https://github.com/system-software-lab/nrf20/blob/main/vino119/time_result)
 
- main6.cpp -> main.cpp

  energy
