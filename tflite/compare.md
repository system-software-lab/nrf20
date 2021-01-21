[clim.py](https://github.com/system-software-lab/nrf20/blob/main/tflite/bird/clim.py)
vs 
[mnist.py](https://github.com/system-software-lab/nrf20/blob/main/tflite/mnist_coral/mnist.py)
------
- make_interpreter(model_file)
```
def make_interpreter(model_file):
    model_file, *device=model_file.split('@')
    return tflite.Interpreter(
            model_path=model_file,experimental_delegates=[
                tflite.load_delegate(EDGETPU_SHARED_LIB,
                    {'device':device[0]} if device else {})
                ])
```

- interpreter.allocate_tensors()

- input_size(interpreter)
  - [clim.py](https://github.com/system-software-lab/nrf20/blob/095fe34193e92654de675fdd988367257ed9b19a/tflite/bird/clim.py#L106)
  ```
  def input_size(interpreter):
  """Returns input image size as (width, height) tuple."""
  _, height, width, _ = interpreter.get_input_details()[0]['shape']
  return width, height
  ```
  ```
  size = classify.input_size(interpreter)
  ```
  - [mnist.py](https://github.com/system-software-lab/nrf20/blob/f0dd01d66d9642bc48425aac5fc1df79b5418f02/tflite/mnist_coral/mnist.py#L70)
  ```
  def input_details(interpreter, key):
    return interpreter.get_input_details()[0][key]

  def input_size(interpreter):
    _, height,width, _=input_details(interpreter,'shape')
    return width,height

  ```
  ```
  size=tensor.input_size(interpreter)
  ```

- interpreter.invoke()

- get_output(interpreter)
  - [clim.py](https://github.com/system-software-lab/nrf20/blob/095fe34193e92654de675fdd988367257ed9b19a/tflite/bird/clim.py#L132)
  ```
  def output_tensor(interpreter):
  """Returns dequantized output tensor."""
  output_details = interpreter.get_output_details()[0]
  output_data = np.squeeze(interpreter.tensor(output_details['index'])())
  scale, zero_point = output_details['quantization']
  return scale * (output_data - zero_point)

  def get_output(interpreter, top_k=1, score_threshold=0.0):
    """Returns no more than top_k classes with score >= score_threshold."""
    scores = output_tensor(interpreter)
    classes = [
        Class(i, scores[i])
        for i in np.argpartition(scores, -top_k)[-top_k:]
        if scores[i] >= score_threshold
    ]
    return sorted(classes, key=operator.itemgetter(1), reverse=True)
  ```
  ```
  classes=classify.get_output(interpreter, args.top_k, args.threshold)
  ```
  - [mnist.py](https://github.com/system-software-lab/nrf20/blob/f0dd01d66d9642bc48425aac5fc1df79b5418f02/tflite/mnist_coral/mnist.py#L84())
  ```
  def output_tensor(interpreter):
    output_details=interpreter.get_output_details()[0]
    output_data=np.squeeze(interpreter.tensor(output_details['index'])())
    return output_data
    
  def get_output(interpreter):
    scores=output_tensor(interpreter)
    max=0;
    for i in range(9):
        if scores[i+1]>scores[max]:
            max=i+1;
    return max;
  ```
  ```
  classes=tensor.get_output(interpreter)
  ```
