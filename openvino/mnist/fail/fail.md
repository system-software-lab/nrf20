`std::string strNotMatched("The " + sType + " blob size is not equal to the network " + sType + " size");`

https://docs.openvinotoolkit.org/latest/ie_plugin_api/ie__infer__request__internal_8hpp_source.html

`checkBlob()`
https://docs.openvinotoolkit.org/latest/ie_plugin_api/classInferenceEngine_1_1InferRequestInternal.html#ad07c0ddee0a0648d264e975ab9a2d672

이 사람은 output blob을
https://community.intel.com/t5/Intel-Distribution-of-OpenVINO/Problem-with-extraction-of-image-from-the-blob/td-p/1169554
Blob::Ptr -> buffer() : deprecated~ => MemoryBlob ^^

openvino quantization
https://docs.openvinotoolkit.org/2020.2/_docs_BestPractices.html

https://docs.openvinotoolkit.org/latest/openvino_docs_MO_DG_prepare_model_Model_Optimizer_FAQ.html
