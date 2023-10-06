#!/bin/bash

code="run8.py"

model1="mobv1"
model2="mobv2"
model3="resnet"
model4="incept"

model=$model4

echo -e "$model\n"
echo 1 | sudo tee /proc/sys/vm/drop_caches

python3 $code ../model/$model.xml
echo 1 | sudo tee /proc/sys/vm/drop_caches

python3 $code ../model/$model.xml
echo 1 | sudo tee /proc/sys/vm/drop_caches

python3 $code ../model/$model.xml
echo 1 | sudo tee /proc/sys/vm/drop_caches
