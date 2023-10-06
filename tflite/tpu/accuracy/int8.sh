#!/bin/bash

echo " TPU "

echo "mnist9_edge.tflite"
python3 mnist_time_total.py ../model/mnist9_edgetpu.tflite

echo " mobv1_edge.tflite "
python3 mob7.py ../model/mobv1_edgetpu.tflite

echo " mobv2_edge.tflite "
python3 mob7.py ../model/mobv2_edgetpu.tflite

echo " incept_edge.tflite "
python3 mob7.py ../model/incept_edgetpu.tflite

echo " resnet_edge.tflite "
python3 mob7.py ../model/resnet_edgetpu.tflite

#echo " CPU "

#echo " mobv1.tflite "
#python3 mob6.py ./tflite/mobv1.tflite

#echo " mobv2.tflite "
#python3 mob6.py ./tflite/mobv2.tflite

#echo " incept.tflite "
#python3 mob6.py ./tflite/incept.tflite

#echo " resnet.tflite "
#python3 mob6.py ./tflite/resnet.tflite
