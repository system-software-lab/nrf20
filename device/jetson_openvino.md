https://software.intel.com/content/www/us/en/develop/articles/arm64-sbc-and-ncs2.html

https://github.com/openvinotoolkit/openvino/archive/2021.2.zip

https://github.com/openvinotoolkit/openvino/archive/2020.4.tar.gz

https://www.intel.com/content/www/us/en/support/articles/000057448/software/development-software.html

git submodule update --init --recursive -> git: 모든 파일을 가져올 수 없음.. / submodule update 필요 

libpython3.6m.so.1.0 이 무슨 x86-64/ 파일에 들어있어야 한다고 나오는데
/usr/local/lib 인지 어딘지에서 저 파일을 찾아서 위 디렉토리 이름으로 만들어 넣어주면 해결됨.

https://community.intel.com/t5/Intel-Distribution-of-OpenVINO/DLDT-install-on-Ubuntu-18-04-on-RPi4-Cython-File-error/td-p/1198301?profile.language=ko

x86-64-linux -> aarch64-linux 

```
git clone https://github.com/openvinotoolkit/openvino.git
cd openvino
git checkout 2020.4
cd inference-engine
git submodule update --init --recursive
cd ../openvino
sh ./install_dependencies.sh
cd inference-engine/ie_bridges/python
pip3 install -r requirements.txt
cd ../../../ && mkdir build && cd build

cmake -DCMAKE_BUILD_TYPE=Release \
-DENABLE_MKL_DNN=OFF \
-DENABLE_CLDNN=OFF \
-DENABLE_GNA=OFF \
-DENABLE_SSE42=OFF \
-DTHREADING=SEQ \
-DENABLE_SAMPLES=ON \
-DENABLE_OPENCV=OFF \
-DENABLE_PYTHON=ON \
-DPYTHON_EXECUTABLE=/usr/bin/python3.6 \
-DPYTHON_LIBRARY=/usr/lib/aarch64-linux-gnu/libpython3.6m.so \
-DPYTHON_INCLUDE_DIR=/usr/include/python3.6 \
..

```
