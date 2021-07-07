#!/bin/bash

echo "mode:"
sudo nvpmodel -q 

echo -e "\ngpu_cur_freq:  "
cat /sys/class/devfreq/57000000.gpu/cur_freq

echo -e "\ncpu_cur_freq\n"
sudo cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq
sudo cat /sys/devices/system/cpu/cpu1/cpufreq/cpuinfo_cur_freq
sudo cat /sys/devices/system/cpu/cpu2/cpufreq/cpuinfo_cur_freq
sudo cat /sys/devices/system/cpu/cpu3/cpufreq/cpuinfo_cur_freq
echo -e "\n"
