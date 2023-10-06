#!/bin/bash

code0="mnist_t.py"
code1="mob10.py"

model0="mnist9_edgetpu.tflite"
model1="mobv1_edgetpu.tflite"
model2="mobv2_edgetpu.tflite"
model3="resnet_edgetpu.tflite"
model4="incept_edgetpu.tflite"

model=$model4
code=$code1

echo -e "$model: \n"

echo 1 | sudo tee /proc/sys/vm/drop_caches
python3 $code ../model/$model
echo 1 | sudo tee /proc/sys/vm/drop_caches

python3 $code ../model/$model
echo 1 | sudo tee /proc/sys/vm/drop_caches

python3 $code ../model/$model
echo 1 | sudo tee /proc/sys/vm/drop_caches
