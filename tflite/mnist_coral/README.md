model | device|quantize|code
-------|--------|----------|------
mnist4.tflite|CPU|  O  | mnist_cpu.py
mnist6.tflite|CPU|  X  | mnist_cpu.py
mnist4_edgetpu.tflite|TPU|  O | mnist.py

- t10k-images-idx3-ubyte, t10k-labels-idx1-ubyte

	data

- tensor.py

	i/o tensor code