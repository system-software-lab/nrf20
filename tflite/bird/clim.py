# Lint as: python3
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
r"""Example using TF Lite to classify a given image using an Edge TPU.

   To run this code, you must attach an Edge TPU attached to the host and
   install the Edge TPU runtime (`libedgetpu.so`) and `tflite_runtime`. For
   device setup instructions, see g.co/coral/setup.

   Example usage (use `install_requirements.sh` to get these files):
   ```
   python3 classify_image.py \
     --model models/mobilenet_v2_1.0_224_inat_bird_quant_edgetpu.tflite  \
     --labels models/inat_bird_labels.txt \
     --input images/parrot.jpg
   ```
"""

import argparse
import time

from os import listdir
import os
from PIL import Image

import classify
import tflite_runtime.interpreter as tflite
import platform

EDGETPU_SHARED_LIB = {
  'Linux': 'libedgetpu.so.1',
  'Darwin': 'libedgetpu.1.dylib',
  'Windows': 'edgetpu.dll'
}[platform.system()]


def load_labels(path, encoding='utf-8'):
  """Loads labels from file (with or without index numbers).

  Args:
    path: path to label file.
    encoding: label file encoding.
  Returns:
    Dictionary mapping indices to labels.
  """
  with open(path, 'r', encoding=encoding) as f:
    lines = f.readlines()
    if not lines:
      return {}

    if lines[0].split(' ', maxsplit=1)[0].isdigit():
      pairs = [line.split(' ', maxsplit=1) for line in lines]
      return {int(index): label.strip() for index, label in pairs}
    else:
      return {index: line.strip() for index, line in enumerate(lines)}


def make_interpreter(model_file):
  model_file, *device = model_file.split('@')
  return tflite.Interpreter(
      model_path=model_file,
      experimental_delegates=[
          tflite.load_delegate(EDGETPU_SHARED_LIB,
                               {'device': device[0]} if device else {})
      ])


def main():

    start = time.perf_counter()
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '-m', '--model', required=True, help='File path of .tflite file.')
    parser.add_argument(
        '-i', '--input', required=False, help='Image to be classified.')
    parser.add_argument(
        '-l', '--labels', help='File path of labels file.')
    parser.add_argument(
         '-k', '--top_k', type=int, default=1,
        help='Max number of classification results')
    parser.add_argument(
        '-t', '--threshold', type=float, default=0.0,
        help='Classification score threshold')
    parser.add_argument(
        '-c', '--count', type=int, default=1,
        help='Number of times to run inference')
    args = parser.parse_args()

    labels = load_labels(args.labels) if args.labels else {}

    interpreter = make_interpreter(args.model)
    interpreter.allocate_tensors()

    size = classify.input_size(interpreter)
    parsing_time = time.perf_counter() - start
    print('parsing time = %.1fms' % (parsing_time * 1000))


    for i in range(5):
    #image_open
        st = time.perf_counter()
        path='./birds2/'
        files=[f for f in listdir(path)]
        image=[]
        for i in files:
            image.append(Image.open(path+i).convert('RGB').resize(size, Image.ANTIALIAS))
        open_t = time.perf_counter() - st
        print('input time = %.1fms' % (open_t*1000))
        classe=[]
  
        time.sleep(15)
        total_inference_time = 0

        for x in image:
            classify.set_input(interpreter, x)

            start = time.perf_counter()
            interpreter.invoke()
            inference_time = time.perf_counter() - start
            classes=classify.get_output(interpreter, args.top_k, args.threshold)
            classe.append(classes[0])
#            print('inference time = %.1fms' % (inference_time * 1000))
            total_inference_time += inference_time

        print('total inference time = %.1fms' % (total_inference_time * 1000))
        time.sleep(30)


'''
  for klass in classe:
      print(klass.id)
      print('%s: %.5f' % (labels.get(klass.id, klass.id), klass.score))
'''

if __name__ == '__main__':
      main()
