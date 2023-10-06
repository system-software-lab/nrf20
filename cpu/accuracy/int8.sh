#!/bin/bash

echo " CPU "

echo "mnist9"
python3 mnist_time_total.py ../model/mnist9.tflite

echo " mobv1.tflite "
python3 mob6.py ../model/mobv1.tflite

echo " mobv2.tflite "
python3 mob6.py ../model/mobv2.tflite

echo " incept.tflite "
python3 mob6.py ../model/incept.tflite

echo " resnet.tflite "
python3 mob6.py ../model/resnet.tflite
