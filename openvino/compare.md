- using namespace InferenceEngine;

- int main(int argc, char* argv[]){

- Core ie;

- std::string binFileName=fileNameNoExt(argv[1])+".bin";

- CNNNetwork network=ie.ReadNetwork(argv[1]);

- InputsDataMap inputsInfo(network.getInputsInfo());

        std::string imageInputName;

        InputInfo::Ptr inputInfo = nullptr;

        SizeVector inputImageDims;
        /** Stores input image **/

        /** Iterating over all input blobs **/
        for (auto & item : inputsInfo) {
            /** Working with first input tensor that stores image **/
            if (item.second->getInputData()->getTensorDesc().getDims().size() == 4) {
		imageInputName = item.first;

                inputInfo = item.second;

Precision inputPrecision = Precision::FP32;
item.second->setPrecision(inputPrecision);

        if (inputInfo == nullptr) {
            inputInfo = inputsInfo.begin()->second;
        }

- OutputsDataMap outputsInfo(network.getOutputsInfo());

	std::string output_name;
	DataPtr outputInfo;

	for(const auto& out : outputsInfo){
		output_name=out.first;
		outputInfo=out.second;
	}
- const SizeVector outputDims=outputInfo->getTensorDesc().getDims();

- outputInfo->setPrecision(Precision::FP16);

- ExecutableNetwork executable_network=ie.LoadNetwork(network,"MYRIAD");

- InferRequest infer_request=executable_network.CreateInferRequest();

Blob::Ptr imageInput=infer_request.GetBlob(imageInputName);

	MemoryBlob::Ptr mimage=as<MemoryBlob>(imageInput);
	if(!mimage){printf("cast imageinput to memory blob failed");return 1;}
	auto minputHolder=mimage->wmap();

	//size_t num_channels=mimage->getTensorDesc().getDims()[1];
	size_t image_size=mimage->getTensorDesc().getDims()[3]*mimage->getTensorDesc().getDims()[2];
	//std::cout<<"prepare input-1/(inputholder): "<<clock()-st<<std::endl;
	
	float* data=minputHolder.as<float*>();

	MemoryBlob::CPtr moutput;

for (size_t pid = 0; pid < image_size; pid++) 
	    {
                    data[pid] = imagedata[num].get()[pid];
 }

infer_request.Infer();

const Blob::Ptr output_blob=infer_request.GetBlob(output_name);
		moutput=as<MemoryBlob>(output_blob);
		if(!moutput){printf("cast output to memory blob failed\n");}
		auto moutputHolder=moutput->rmap();
		detection=moutputHolder.as<const PrecisionTrait<Precision::FP16>::value_type*>();
