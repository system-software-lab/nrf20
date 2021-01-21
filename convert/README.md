- bird_quant2.json/ bird_quant_edgetpu2.json

	tensorflow 모델 layer를  summary 함수로 보는 것(summary_quant.py)과 비슷하게
	tflite 모델도 flatc를 이용하여 json 파일로 바꾸면 볼 수 있음(Linux)
	(변환 과정에서 schmea.fbs 파일 사용)
	
	`
	flatc -t schema.fbs -- model_name.tflite
	`

- convert_flatbuffer.JPG 

	라즈베리파이에서 사용하려면 .tflite 파일을 C array로 만들어야 한다고 했는데
	상관없음.(raspi_convert)

- openvino_model

	saved_quant_model로 변환한 openvino IR 모델
	fake-quantize layer 지원 안 함.

- openvino_model2

	saved_X_quant_model로 변환한 openvino IR 모델
	사용 가능.

- edge_tpu_model.PNG

	mnist3.tflite 모델은 converter option을 안 줘서 weight가 활성화 되지 않아서 edgetpu compiler가 quantize가 안 됐다고 판단.
	mnist4.tflite 모델 option주고 바꿔서 edgetpu comile 가능
	결과: mnist4.tflite -> mnist4_edgetpu.tflite

- mnist4_edgetpu.log

 	edgetpu compiler 수행 결과 
	compile 후 TPU에서 수행 가능한 layer 나열/ 이외에는 CPU에서 실행.

- model_result4.jpg

	tensorflow| saved_model.pb
	------------|------------------- 
	coral |  mnist4.tflite, mnist4_edgetpu.tflite
	NCS2 | saved_model.xml, saved_model.bin

	각 모델 수행 정확도 측정 결과 

- openvino_model_convert.PNG

	mo_tf 실행 결과

- openvino예제.txt

	tensorflow slim 모델을 사용할 경우 tflite로 변환할 수 없는 이유
	non-frozen model


	
	



	