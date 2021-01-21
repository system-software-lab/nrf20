

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
uint16_t dist,cate,nid;
uint16_t model[160];
long sum=0;

bool SD_detected=false;
SdFat SDD;
char header[640];
char empty;
char num[3];
uint8_t nu[160];
//uint16_t cat_num=0;
//int i=0;
int k=0;
int m=0;
int nn[4][2]={{384,192},{1152,576},{1920,960},{2416,1218}};
int result;
int ok=0;
int ran=0;
int total=0;
float per=0;
int pos=0;
int neg=0;


void setup() {
 
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
  if (!SD_detected) {
    Serial.print("sd not found");
  }

/*
  // File not exist in SD card
  if (!SDD.exists("train3.txt")) {
    Serial.print("file not found");
  }
*/
  File SDfile = SDD.open("train3.txt",O_READ);
  File SDfile2 = SDD.open("train4.txt",O_READ);
  
  // Fail to open file
  if (!SDfile && !SDfile2) {
    Serial.print("open fail");
  }
//learn_positive

  for(k=0;k<nn[minus][0]-1;k++)
  {
  for(i=0;i<160;i++)
  {
    num[0]=SDfile.read();
    num[1]=SDfile.read();
    num[2]=SDfile.read();
    empty=SDfile.read();
    nu[i]=atoi(num);
    
  }
  m=micros();
  hnn.learn(nu,160,cat_num++);
  m=micros()-m;
  empty=SDfile.read();
  }
Serial.print(m);

//learn_negative
  for(k=0;k<nn[minus][1];k++)
  {
  for(i=0;i<160;i++)
  {
    num[0]=SDfile2.read();
    num[1]=SDfile2.read();
    num[2]=SDfile2.read();
    empty=SDfile2.read();
    nu[i]=atoi(num);
    
  }
  m=micros();
  hnn.learn(nu,160,cat_num++);
  m=micros()-m;
  empty=SDfile2.read();
  }
Serial.print(m);

  SDfile.close();
  SDfile2.close();




Serial.print("\n Ncount:"); Serial.println(hnn.getNcount());
Serial.println();
ncount=hnn.getNcount();
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

/*
File SDfile3 = SDD.open("test4.txt",O_READ);
for(k=0;k<10;k++)
{
  for(i=0;i<160;i++)
  {
    num[0]=SDfile3.read();
    num[1]=SDfile3.read();
    num[2]=SDfile3.read();
    empty=SDfile3.read();
    nu[i]=atoi(num);
    
  }
  m=micros();
  //dist,cate,nid
  result=hnn.classify(nu,160,&dist,&cate,&nid);
    m=micros()-m;
  empty=SDfile3.read();
    
    Serial.print("time:");
Serial.println(m);

  Serial.println(result);
 Serial.print("cate:");Serial.println(cate);
 if(result!=0 and cate>=nn[minus][0]) ok++;

      Serial.println();
}

Serial.print("ok:");Serial.print(ok);
  SDfile3.close();
*/
/*
pos=1132;
 File SDfile4=SDD.open("test3.txt",O_READ);

 while(pos!=0)
 {
  
    for(i=0;i<160;i++)
  {
    num[0]=SDfile4.read();
    num[1]=SDfile4.read();
    num[2]=SDfile4.read();
    empty=SDfile4.read();
    nu[i]=atoi(num);
    
  }
  //m=micros();
  //dist,cate,nid
  result=hnn.classify(nu,160,&dist,&cate,&nid);
    //m=micros()-m;
  empty=SDfile4.read();

  if(result!=0 and cate<nn[minus][0]) ok++;
  total++;
  pos--;
 }

 SDfile4.close();

    per=(float)ok/(float)total*100;
  //Serial.println(ok);Serial.print("../");Serial.println(total);
  Serial.print("per: ");Serial.println(per);
 */
 
/*
pos=1132;
neg=453;

  File SDfile4=SDD.open("test3.txt",O_READ);
  File SDfile5=SDD.open("test4.txt",O_READ);

while(pos!=0 and neg!=0)
{
  ran=random(0,999);
  ran=ran%2;
  //Serial.print("nn[minus]");Serial.println(nn[minus][0]);
  if(ran%2==1 and pos!=0)
  {
    for(i=0;i<160;i++)
  {
    num[0]=SDfile4.read();
    num[1]=SDfile4.read();
    num[2]=SDfile4.read();
    empty=SDfile4.read();
    nu[i]=atoi(num);
    
  }
  //m=micros();
  //dist,cate,nid
  result=hnn.classify(nu,160,&dist,&cate,&nid);
    //m=micros()-m;
  empty=SDfile4.read();

  if(result!=0 and cate<nn[minus][0]) ok++;
  total++;
  pos--;
  
  }
  else
  {
    if(neg!=0)
    {
     for(i=0;i<160;i++)
  {
    num[0]=SDfile5.read();
    num[1]=SDfile5.read();
    num[2]=SDfile5.read();
    empty=SDfile5.read();
    nu[i]=atoi(num);
    
  }
  //m=micros();
  //dist,cate,nid
  result=hnn.classify(nu,160,&dist,&cate,&nid);
    //m=micros()-m;
  empty=SDfile5.read();

  if(result!=0 and cate>=nn[minus][0]) ok++;
  total++;
  neg--;
    }
  }


  //delay(500);
}
  SDfile4.close();
  SDfile5.close();

    per=(float)ok/(float)total*100;
  //Serial.println(ok);Serial.print("../");Serial.println(total);
  Serial.print("per: ");Serial.println(per);
 */

}

void loop()
{
  /*
  File SDfile4=SDD.open("test3.txt",O_READ);
  File SDfile5=SDD.open("test4.txt",O_READ);

for(k=0;k<400;k++)
{
  ran=random(0,999);
  ran=ran%2;
  //Serial.print("nn[minus]");Serial.println(nn[minus][0]);
  if(ran%2==1)
  {
    for(i=0;i<160;i++)
  {
    num[0]=SDfile4.read();
    num[1]=SDfile4.read();
    num[2]=SDfile4.read();
    empty=SDfile4.read();
    nu[i]=atoi(num);
    
  }
  //m=micros();
  //dist,cate,nid
  result=hnn.classify(nu,160,&dist,&cate,&nid);
    //m=micros()-m;
  empty=SDfile4.read();

  if(result!=0 and cate<nn[minus][0]) ok++;
  if(result!=0) total++;
  
  }
  else
  {
     for(i=0;i<160;i++)
  {
    num[0]=SDfile5.read();
    num[1]=SDfile5.read();
    num[2]=SDfile5.read();
    empty=SDfile5.read();
    nu[i]=atoi(num);
    
  }
  //m=micros();
  //dist,cate,nid
  result=hnn.classify(nu,160,&dist,&cate,&nid);
    //m=micros()-m;
  empty=SDfile5.read();

  if(result!=0 and cate>=nn[minus][0]) ok++;
  if(result!=0) total++;
       
  }

  per=(float)ok/(float)total*100;
  //Serial.println(ok);Serial.print("../");Serial.println(total);
  Serial.print("per: ");Serial.println(per);
  delay(500);
}
  SDfile4.close();
  SDfile5.close();
  */
}
