1. Add our Debian package repository to your system:

echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list

curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

sudo apt-get update

2. Install the Edge TPU runtime:

sudo apt-get install libedgetpu1-std

python 버전 -> python 3.7

wget https://github.com/google-coral/pycoral/releases/download/release-frogfish/tflite_runtime-2.5.0-cp37-cp37m-linux_armv7l.whl
(https://www.tensorflow.org/lite/guide/python 최신버전 설치~)

pip3 install tflite_runtime-1.14.0-cp37-cp37m-linux_armv7l.whl
(pip3 freeze | grep tflite -> 현재 설치 버전, pip3 uninstall 잘못된 설치 버전)

mkdir coral && cd coral

git clone https://github.com/google-coral/tflite.git


cd tflite/python/examples/classification

bash install_requirements.sh


python3 classify_image.py \
--model models/mobilenet_v2_1.0_224_inat_bird_quant_edgetpu.tflite \
--labels models/inat_bird_labels.txt \
--input images/parrot.jpg


?
TF Lite를 쉽게 쓸 수 있게 도와주는 Edge TPU API
apt install python3-edgetpu
