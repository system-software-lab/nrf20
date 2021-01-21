#include <BlockDriver.h>
#include <FreeStack.h>
#include <MinimumSerial.h>
#include <SdFat.h>
#include <SdFatConfig.h>
#include <sdios.h>
#include <SysCall.h>

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

#define NM500_SPI_SS 7

#define VECTOR_LENGTH 160
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
    

  
  minus=hnn.total_neurons/576;
  minus=!!(minus-1);

  /*
//write+write
for(i=0;i<3;i++)
{
   timee=micros();
   hnn.setGcr(1);
   timee=micros()-timee;
   Serial.println(timee);
}
Serial.println();*/
/*
//read+write
for(i=0;i<3;i++)
{
   timee=micros();
   minus=hnn.getNcount();
   timee=micros()-timee;
   Serial.println(timee);
}
*/


  while(cat_num!=hnn.total_neurons-minus)
{
    for(i=0;i<VECTOR_LENGTH;i++)
    {
      
      vector[i]=random(0,255);

    }
     
   timee=micros();   
   hnn.learn(vector,VECTOR_LENGTH,cat_num++);
   timee=micros()-timee;
  
   
      
    Serial.println(timee); 

}
//Serial.println(sum);


/*
timee=millis();
  while(cat_num!=hnn.total_neurons-minus)
{
    for(i=0;i<VECTOR_LENGTH;i++)
    {
     
      vector[i]=random(0,255);

    }

    hnn.learn(vector,VECTOR_LENGTH,cat_num++);


}*/

//timee=millis()-timee;
//Serial.println(timee);

 //   timee=millis()-timee;
 //   Serial.println(timee); 

 /*
ncount=hnn.getNcount();
  for (i = 1; i <= ncount; i++) {
      hnn.readNeuron(i, model, &ncr, &aif, &cat);
      Serial.print("\nneuron#"); Serial.print(i); Serial.print("\tmodel=");
      for (j = 0; j < VECTOR_LENGTH; j++) {
        //Serial.print(model[j]); Serial.print(", ");
      }
      Serial.print("\tncr="); Serial.print(ncr);  
      Serial.print("\taif="); Serial.print(aif);     
      Serial.print("\tcat="); Serial.print(cat & 0x7FFF); if (cat & 0x8000) Serial.print(" (degenerated)");
  }
  */
Serial.print("\n Ncount:"); Serial.print(hnn.getNcount());
/*
for(j=0;j<100;j++)
{
    for(i=0;i<VECTOR_LENGTH;i++)
    {
      vector[i]=random(0,255);
    }
  Serial.print("classify:");
  timee=micros();   
   response_nbr = hnn.classify(vector, VECTOR_LENGTH);
   timee=micros()-timee;
   Serial.println(timee);
}
*/
}

void loop()
{
  /*
      for(i=0;i<VECTOR_LENGTH;i++)
    {
      vector[i]=random(0,255);
    }
  Serial.print("classify:");
  timee=micros();   
   response_nbr = hnn.classify(vector, VECTOR_LENGTH);
   timee=micros()-timee;
   Serial.println(timee);
   */

  
   
}
