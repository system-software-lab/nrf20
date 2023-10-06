#!/bin/bash

echo -e "mnist\n"
echo 1 | sudo tee /proc/sys/vm/drop_caches

python3 run1_710.py
echo 1 | sudo tee /proc/sys/vm/drop_caches

python3 run1_710.py
echo 1 | sudo tee /proc/sys/vm/drop_caches

python3 run1_710.py
echo 1 | sudo tee /proc/sys/vm/drop_caches
