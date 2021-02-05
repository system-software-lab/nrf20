Hi

model                     | H/W                  | size
--------------------------|----------------------|--------
**mnist9.tflite**         | fully integer CPU    | 1.57 MB
**mnist9_edgetpu.tflite** | fully integer TPU    | 1.65 MB
**mnist8.tflite**         | FP16 CPU             | 3.13 MB


```
Edge TPU Compiler version 15.0.340273435
Input: mnist4.tflite
Output: mnist4_edgetpu.tflite

Operator                       Count      Status

RESHAPE                        1          Mapped to Edge TPU
CONV_2D                        2          Mapped to Edge TPU
SOFTMAX                        1          Mapped to Edge TPU
QUANTIZE                       1          Operation is otherwise supported, but not mapped due to some unspecified limitation
DEQUANTIZE                     1          Operation is working on an unsupported data type
MAX_POOL_2D                    2          Mapped to Edge TPU
FULLY_CONNECTED                2          Mapped to Edge TPU

Edge TPU Compiler version 15.0.340273435
Input: mnist7.tflite
Output: mnist7_edgetpu.tflite

Operator                       Count      Status

SOFTMAX                        1          Mapped to Edge TPU
FULLY_CONNECTED                2          Mapped to Edge TPU
RESHAPE                        1          Mapped to Edge TPU
CONV_2D                        2          Mapped to Edge TPU
MAX_POOL_2D                    2          Mapped to Edge TPU


```
