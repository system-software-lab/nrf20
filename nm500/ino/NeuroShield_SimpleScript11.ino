

/******************************************************************************
 *  NM500 NeuroShield Board SimpleScript
 *  Simple Test Script to understand how the neurons learn and recognize
 *  revision 1.1.3, 01/03, 2018
 *  Copyright (c) 2017 nepes inc.
 *  
 *  Please use the NeuroShield library v1.1.3 or later.
 *  https://github.com/nepes-ai/neuroshield 
 ******************************************************************************/

#include <NeuroShield.h>
#include <SdFat.h>


#define NM500_SPI_SS 7

#define VECTOR_LENGTH 256
#define READ_COUNT 3

NeuroShield hnn;

uint8_t vector[VECTOR_LENGTH];
uint16_t response_nbr;
int i;
int cat_num=1;
uint8_t minus=0;
int timee=0;
int ncount=0;
int j=0;
uint16_t ncr, aif, cat;
uint16_t model[NEURON_SIZE];
long sum=0;





void setup() {
  
bool SD_detected=false;
SdFat SDD;
char empty;
char num[3];
uint8_t nu[160];
uint16_t k=0;
uint16_t m=0;
int nn[4][2]={{384,192},{1152,576},{1920,960},{2416,1218}};
int result;
uint16_t ok=0;
uint16_t ran=0;
int total=0;
float per=0;
uint16_t dist,cate,nid;
int degen=0;
int pos=0;
int neg=0;
 
  /*
  Serial.begin(9600);
  while (!Serial);    // wait for the serial port to open
  if (hnn.begin(NM500_SPI_SS) != 0){ Serial.print("\nThere are "); Serial.print(hnn.total_neurons); Serial.print(" neurons\n");}
  else {Serial.print("\n NOT properly connected!"); while(1);}
*/
 Serial.begin(9600);


 hnn.begin(NM500_SPI_SS);


  // if you want to run in lsup mode, uncomment below
  //norm_lsup = 0x80;
   
  hnn.setGcr(1);
    
Serial.println("start");
  /*
  minus=hnn.total_neurons/576;
  minus=!!(minus-1);
*/
  minus=hnn.total_neurons/576;
  minus/=2;
 

//sum=hnn.readcard("test.txt");

//Serial.println(sum);
if (!SD_detected) {
    SD_detected = SDD.begin(ARDUINO_SD_CS);
  }

  // SD card not found

  File SDfile = SDD.open("train3.txt",O_READ);
  File SDfile2 = SDD.open("train4.txt",O_READ);
  
  // Fail to open file
  
  if (!SDfile && !SDfile2) {
    Serial.print("open fail");
  }

  pos=nn[minus][0]-1;
  neg=nn[minus][1];
//learn_positive
while(pos!=0 and neg!=0)
{
  
  for(i=0;i<160;i++)
  {
    num[0]=SDfile.read();
    num[1]=SDfile.read();
    num[2]=SDfile.read();
    empty=SDfile.read();
    nu[i]=atoi(num);

  }
 
  hnn.learn(nu,160,cat_num++);

  empty=SDfile.read();
  pos--;
  
//learn_negative
  if(neg!=0)
  {
  for(i=0;i<160;i++)
  {
    num[0]=SDfile2.read();
    num[1]=SDfile2.read();
    num[2]=SDfile2.read();
    empty=SDfile2.read();
    nu[i]=atoi(num);
  }

  hnn.learn(nu,160,cat_num++);

  empty=SDfile2.read();
  neg--;
  }

}
  

  SDfile.close();
  SDfile2.close();




Serial.println(hnn.getNcount());
Serial.println();

ncount=hnn.getNcount();
/*
for (i = 1; i <= ncount; i++) {
      hnn.readNeuron(i, model, &ncr, &aif, &cat);
      Serial.print("\nneuron#"); Serial.print(i); Serial.print("\tmodel=");
      for (j = 0; j < VECTOR_LENGTH; j++) {
        //Serial.print(model[j]); Serial.print(", ");
      }
      Serial.print("model[0]:");Serial.print(model[0]);
      Serial.print("\tncr="); Serial.print(ncr);  
      Serial.print("\taif="); Serial.print(aif);     
      Serial.print("\tcat="); Serial.print(cat & 0x7FFF); if (cat & 0x8000) Serial.println(" (degenerated)");
  }

Serial.print("maxif");Serial.println(hnn.getMaxif());
Serial.print("minif");Serial.println(hnn.getMinif());
*/
  
  /*
  for(i=1;i<=ncount;i++){
    hnn.readNeuron(i,model,&ncr,&aif,&cat);
    if(cat&0x8000) degen+=1;
  }

  Serial.print(degen);
  */
  

File SDfile3 = SDD.open("test3.txt",O_READ);
  for(k=0;k<10;k++)
  {
  for(i=0;i<160;i++)
  {
    num[0]=SDfile3.read();
    num[1]=SDfile3.read();
    num[2]=SDfile3.read();
    empty=SDfile3.read();
    nu[i]=atoi(num);
  //if(i==0) Serial.print(nu[i]);
    
  }
  //m=micros();
  result=hnn.classify(nu,160,&dist,&cate,&nid);
  //m=micros()-m;
  empty=SDfile3.read();

  if(result!=0 and (cate%2==1 or cate>nn[minus][0])) ok++;
  total++;
  }

//per=(float)ok/(float)total*100;
//Serial.print("per:");Serial.println(per);

SDfile3.close();

File SDfile4 = SDD.open("test4.txt",O_READ);
  for(k=0;k<10;k++)
  {
  for(i=0;i<160;i++)
  {
    num[0]=SDfile4.read();
    num[1]=SDfile4.read();
    num[2]=SDfile4.read();
    empty=SDfile4.read();
    nu[i]=atoi(num);
  //if(i==0) Serial.print(nu[i]);
    
  }
  //m=micros();
  result=hnn.classify(nu,160,&dist,&cate,&nid);
  //m=micros()-m;
  empty=SDfile4.read();

  if(result!=0 and cate%2==0) ok++;
  total++;
  }

per=(float)ok/(float)total*100;
Serial.print("per:");Serial.println(per);

SDfile4.close();




}

void loop()
{
 
}
