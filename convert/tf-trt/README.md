https://github.com/tensorflow/tensorrt/blob/master/tftrt/examples/object_detection/object_detection.py


from tensorflow.python.framework import convert_to_constants

https://github.com/tensorflow/tensorrt/blob/master/tftrt/examples/image-classification/image_classification.py

data2=tf.convert_to_tensor(value=tf.compat.v1.get_variable(
      "data", initializer=tf.constant(data)))

#model.save(export_path, include_optimizer=True)
  model.save("mnist_model.h5")
  
  python .\mnist_main2.py --model_dir=$MODEL_DIR --data_dir=$DATA_DIR --train_epochs=10 --distribution_strategy=one_device --download

https://developer.nvidia.com/embedded/downloads/archive

https://developer.nvidia.com/jetpack-43-archive
