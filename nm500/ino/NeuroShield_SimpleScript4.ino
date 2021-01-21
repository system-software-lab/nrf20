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

#define VECTOR_LENGTH 256
#define READ_COUNT 3

NeuroShield hnn;

uint8_t vector[VECTOR_LENGTH];
uint16_t response_nbr;
int i;
int cat_num=1;
uint8_t minus=0;
int k;

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
  //while(cat_num!=hnn.total_neurons-minus)
for(k=0;k<10;k++)
{
    for(i=0;i<VECTOR_LENGTH;i++)
    {
      vector[i]=random(0,255);
    }

    hnn.learn(vector,VECTOR_LENGTH,1);
}
Serial.print("\n Ncount:"); Serial.print(hnn.getNcount());

}

void loop()
{
  /*
    for(i=0;i<VECTOR_LENGTH;i++)
    {
      vector[i]=random(0,255);
    }

   response_nbr = hnn.classify(vector, VECTOR_LENGTH);
   */
}
