- saved_model_X_quant

	tensorflow ver.2 mnist model
	양자화 안 함.

- saved_model_quant

	tensorflow ver.2 mnist model
	양자화 함.

- deploy3.py

	위 모델 사용한 코드

- deploy5.py 

	위 모델 정확도 측정

- mnist_main3q.py

	mnist 모델 만드는 코드에서 양자화 과정 포함시킨 코드

```
python3 mnist_main.py \
  --model_dir=$MODEL_DIR \
  --data_dir=$DATA_DIR \
  --train_epochs=10 \
  --distribution_strategy=one_device \
  --num_gpus=$NUM_GPUS \
  --download	
```
