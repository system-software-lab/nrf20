#!/bin/bash
echo -e "mnist \n"
python3 run2_708.py

echo -e "mobv1\n"
python3 run7.py ./../model/mobv1.xml

echo -e "mobv2\n"
python3 run7.py ./../model/mobv2.xml

echo -e "resnet\n"
python3 run7.py ./../model/resnet.xml

echo -e "incept\n"
python3 run7.py ./../model/incept.xml

