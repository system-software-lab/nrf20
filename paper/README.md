논문자료
=======
USB형 가속기와 내장형 TPU의 에너지 효율 비교
-------
### 문서 목록    
- [실험 데이터](https://github.com/system-software-lab/nrf20/blob/main/paper/exprerimental%20data.xlsx)
- 논문
  - [pdf](https://github.com/system-software-lab/nrf20/blob/main/paper/USB%ED%98%95%20%EA%B0%80%EC%86%8D%EA%B8%B0%EC%99%80%20%EB%82%B4%EC%9E%A5%ED%98%95%20TPU%EC%9D%98%20%EC%97%90%EB%84%88%EC%A7%80%20%ED%9A%A8%EC%9C%A8%20%EB%B9%84%EA%B5%90.pdf)
  - [word](https://github.com/system-software-lab/nrf20/blob/main/paper/USB%ED%98%95%20%EA%B0%80%EC%86%8D%EA%B8%B0%EC%99%80%20%EB%82%B4%EC%9E%A5%ED%98%95%20TPU%EC%9D%98%20%EC%97%90%EB%84%88%EC%A7%80%20%ED%9A%A8%EC%9C%A8%20%EB%B9%84%EA%B5%90.doc)
- [KSC2020 발표자료](https://github.com/system-software-lab/nrf20/blob/main/paper/USB%ED%98%95%20%EA%B0%80%EC%86%8D%EA%B8%B0%EC%99%80%20%EB%82%B4%EC%9E%A5%ED%98%95%20TPU%EC%9D%98%20%EC%97%90%EB%84%88%EC%A7%80%20%ED%9A%A8%EC%9C%A8.pptx)        
### 실험에 사용한 소스코드
- VPU([object_detection_sample_ssd](https://github.com/system-software-lab/nrf20/blob/main/openvino/object/object_detection_sample_ssd/main_for_measure.cpp))
- TPU([classify](https://github.com/system-software-lab/nrf20/blob/main/tflite/bird/clim.py))
- CPU([classify](https://github.com/system-software-lab/nrf20/blob/main/tflite/bird/clim_without_tpu.py))
