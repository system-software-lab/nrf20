//mnist_openvino
//main6.cpp
//measure energy consumption_2_time

#include <iostream>
#include <string>
#include <cmath>
#include <ctime>
#include <samples/common.hpp>
#include <unistd.h>

using namespace InferenceEngine;

int reverseInt(int i) {
    unsigned char ch1, ch2, ch3, ch4;
    ch1 = (unsigned char) (i & 255);
    ch2 = (unsigned char) ((i >> 8) & 255);
    ch3 = (unsigned char) ((i >> 16) & 255);
    ch4 = (unsigned char) ((i >> 24) & 255);
    return (static_cast<int>(ch1) << 24) + (static_cast<int>(ch2) << 16) + (static_cast<int>(ch3) << 8) + ch4;
}

void tofp16(const short int* i,float* arr){
	unsigned char sign;
	int expo;
	float mant;
	int  temp;
	for(int k=0;k<10;k++)
	{
		sign=(i[k]>>14)&1;
		expo=((i[k]>>10)&31)-15;
		mant=1;
		temp=i[k]%1024;
		for(int d=9;d>-1;d--)
		{
			mant+=((temp>>d)&1)*(1>>(10-d));
		}
		if(expo==16){std::cout<<"Nan or Inf or 0.00+"<<std::endl;arr[k]=-1;continue;}
		if(expo==-15) 
		{
			expo=-14;
			mant-=1;
		}
		arr[k]=pow(2,expo)*mant*pow(-1,sign+2);
	}
}

int main(int argc, char* argv[]){

	Core ie;
	double start_time;
	//size_t num=std::stoi(argv[4]);
	
	usleep(10000*1000);

	for (int i = 0; i < 10; i++) {
	start_time = clock();

	std::string binFileName=fileNameNoExt(argv[1])+".bin";
	CNNNetwork network=ie.ReadNetwork(argv[1]);
//st=clock();	
	//read_input_data
	std::ifstream file(argv[2],std::ios::binary);
	//read_label_data
	std::ifstream file2(argv[3],std::ios::binary);

	if(!file.is_open()){
		printf("file not opened\n");
		return 0;
	}

	int magic_number=0;
	int number_of_images=0;
	int n_rows=0;
	int n_cols=0;
	size_t height=0;
	size_t width=0;
	std::vector<std::shared_ptr<float>> imagedata(10000);

	file.read(reinterpret_cast<char *>(&magic_number), sizeof(magic_number));
	magic_number=reverseInt(magic_number);
	file.read(reinterpret_cast<char *>(&number_of_images), sizeof(number_of_images));
	number_of_images=reverseInt(number_of_images);
	file.read(reinterpret_cast<char *>(&n_rows), sizeof(n_rows));
	n_rows=reverseInt(n_rows);
	height=(size_t)n_rows;
	file.read(reinterpret_cast<char *>(&n_cols), sizeof(n_cols));
	n_cols=reverseInt(n_cols);
	width=(size_t)n_cols;
	size_t size= width*height*1;
	
	for(int d=0;d<10000;d++)
	{
		imagedata[d].reset(new float[size], std::default_delete<float[]>());
	}

	size_t count=0;
	size_t count2=0;
	float temp2=0;
	
	while(count2!=10000){
		for(int r=0;r<n_rows;++r){
			for(int c=0;c<n_cols;++c){
				unsigned char temp=0;
				file.read(reinterpret_cast<char *>(&temp),sizeof(temp));
				temp2=(float)temp/255.0;
				imagedata[count2].get()[count++]=temp2;
			}
		}
		count=0;
		count2++;

	}
	//std::cout.precision(3);
//	std::cout<<"read data: "<<clock()-st<<std::endl;
	//read_label_Data
	/*
	int* label_data=new int[10000];
	file2.read(reinterpret_cast<char *>(&magic_number), sizeof(magic_number));
	magic_number=reverseInt(magic_number);
	file2.read(reinterpret_cast<char *>(&number_of_images), sizeof(number_of_images));
	number_of_images=reverseInt(number_of_images);
	count=0;
	while(count!=10000){
		unsigned char temp=0;
		file2.read(reinterpret_cast<char*>(&temp),sizeof(temp));
		label_data[count++]=temp;
	}*/
//       st=clock(); 
	InputsDataMap inputsInfo(network.getInputsInfo());

        if (inputsInfo.size() != 1 && inputsInfo.size() != 2) throw std::logic_error("Sample supports topologies only with 1 or 2 inputs");
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
            } 
        }

        if (inputInfo == nullptr) {
            inputInfo = inputsInfo.begin()->second;
        }
        // 6. Prepare output blobs 

	OutputsDataMap outputsInfo(network.getOutputsInfo());
	std::string output_name;
	DataPtr outputInfo;

	for(const auto& out : outputsInfo){
		output_name=out.first;
		outputInfo=out.second;
	}
	//std::cout<<"outputname"<<output_name<<std::endl;

	const SizeVector outputDims=outputInfo->getTensorDesc().getDims();

	outputInfo->setPrecision(Precision::FP16);
//	std::cout<<"prepare i/o blobs: "<<clock()-st<<std::endl;
//loading model to the device
//st=clock();
	ExecutableNetwork executable_network=ie.LoadNetwork(network,"MYRIAD");
	InferRequest infer_request=executable_network.CreateInferRequest();
//	std::cout<<"prepare network: "<<clock()-st<<std::endl;


//prepare input: data -> Memory Blob
//st=clock();

	Blob::Ptr imageInput=infer_request.GetBlob(imageInputName);

	MemoryBlob::Ptr mimage=as<MemoryBlob>(imageInput);
	if(!mimage){printf("cast imageinput to memory blob failed");return 1;}
	auto minputHolder=mimage->wmap();

	//size_t num_channels=mimage->getTensorDesc().getDims()[1];
	size_t image_size=mimage->getTensorDesc().getDims()[3]*mimage->getTensorDesc().getDims()[2];
//	std::cout<<"prepare input-1/(inputholder): "<<clock()-st<<std::endl;
	
	float* data=minputHolder.as<float*>();
	//create input blob
	
	//const Blob::Ptr output_blob;
	MemoryBlob::CPtr moutput;
	const short int* detection;	
	int max=0;
	int* res=new int[10000];
	float* arr=new float[10];
	size_t num=0;
	int dd=0;
	
	//accuracy
//st=clock();
            for (size_t pid = 0; pid < image_size; pid++) 
	    {
                    data[pid] = imagedata[num].get()[pid];
		    //num-> 1/ accuracy-> whole data   
            }
//	std::cout<<"prepare input-1/(imagedata -> data): "<<clock()-st<<std::endl;
//st=clock();
		infer_request.Infer();
//	std::cout<<"infer: "<<clock()-st<<std::endl;

//st=clock();
		const Blob::Ptr output_blob=infer_request.GetBlob(output_name);
		moutput=as<MemoryBlob>(output_blob);
		if(!moutput){printf("cast output to memory blob failed\n");}
		auto moutputHolder=moutput->rmap();
		detection=moutputHolder.as<const PrecisionTrait<Precision::FP16>::value_type*>();
		tofp16(detection,arr);
	
		for(dd=1;dd<10;dd++)
		{
			if(arr[max]<arr[dd])
				max=dd;
		}
		res[num]=max;
//	std::cout<<"process_output: "<<clock()-st<<std::endl;
	//std::cout<<"result: "<<max<<", value: "<<arr[max]<<std::endl;
	/*
	count=0;
	for(dd=0;dd<10000;dd++)
	{
		if(res[dd]!=label_data[dd]) count++;
	}
	*/
	//std::cout<<"result: "<<count<<"/"<<10000-count<<std::endl;
	//input_data_close
	delete[] arr;
	//delete[] label_data; 
	delete[] res;	
	file.close();
	file2.close();

	std::cout << "total time : " << clock() - start_time << std::endl;
	
	usleep(10000*1000);

	}
	return 0;
}



