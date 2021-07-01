convert tensorflow to onnx (tflite! ->onnx->tensorflow?)

ONNX/tensorflow-onnx

https://github.com/onnx/tensorflow-onnx

python -m tf2onnx.convert --saved-model .\mobv1_160 --output mobv1.onnx


convert onnx to openvino

PS C:\Program Files (x86)\Intel\openvino_2021\deployment_tools\model_optimizer> python .\mo.py --input_model .\mobv1.onnx --output_dir . --input_shape [1,160,160,3] --data_type=FP16
Model Optimizer arguments:
Common parameters:
        - Path to the Input Model:      C:\Program Files (x86)\Intel\openvino_2021\deployment_tools\model_optimizer\.\mobv1.onnx
        - Path for generated IR:        C:\Program Files (x86)\Intel\openvino_2021\deployment_tools\model_optimizer\.
        - IR output name:       mobv1
        - Log level:    ERROR
        - Batch:        Not specified, inherited from the model
        - Input layers:         Not specified, inherited from the model
        - Output layers:        Not specified, inherited from the model
        - Input shapes:         [1,160,160,3]
        - Mean values:  Not specified
        - Scale values:         Not specified
        - Scale factor:         Not specified
        - Precision of IR:      FP16
        - Enable fusing:        True
        - Enable grouped convolutions fusing:   True
        - Move mean values to preprocess section:       None
        - Reverse input channels:       False
ONNX specific parameters:
Model Optimizer version:        2021.1.0-1237-bece22ac675-releases/2021/1
2021-07-01 19:43:25.594857: W tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could not load dynamic library 'cudart64_101.dll'; dlerror: cudart64_101.dll not found
2021-07-01 19:43:25.598803: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.

[ SUCCESS ] Generated IR version 10 model.
[ SUCCESS ] XML file: C:\Program Files (x86)\Intel\openvino_2021\deployment_tools\model_optimizer\.\mobv1.xml
[ SUCCESS ] BIN file: C:\Program Files (x86)\Intel\openvino_2021\deployment_tools\model_optimizer\.\mobv1.bin
[ SUCCESS ] Total execution time: 7.14 seconds.


https://docs.openvinotoolkit.org/latest/openvino_docs_MO_DG_prepare_model_convert_model_Convert_Model_From_ONNX.html
