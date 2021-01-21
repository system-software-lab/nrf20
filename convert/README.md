- bird_quant2.json/ bird_quant_edgetpu2.json

	tensorflow 모델 layer를  summary 함수로 보는 것과 비슷하게
	tflite 모델도 flatc를 이용하여 json 파일로 바꾸면 볼 수 있음(Linux)
	
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

	