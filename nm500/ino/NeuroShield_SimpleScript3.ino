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

#define VECTOR_LENGTH 6
#define READ_COUNT 3

NeuroShield hnn;

uint8_t value = 11;
uint8_t vector[VECTOR_LENGTH];
uint16_t ncr, aif, cat, dist, nid, nsr, ncount, minif, response_nbr, norm_lsup = 0;
uint16_t dists[READ_COUNT], cats[READ_COUNT], nids[READ_COUNT];
uint16_t fpga_version;
int i, j,k,m;
int cat_num=1;
long randomnum;
int randomd;

void setup() {
  Serial.begin(9600);
  while (!Serial);    // wait for the serial port to open
  
  if (hnn.begin(NM500_SPI_SS) != 0) {
    fpga_version = hnn.fpgaVersion();
    if ((fpga_version & 0xFF00) == 0x0000) {
      Serial.print("\n#### NeuroShield Board");
    }
    else if ((fpga_version & 0xFF00) == 0x0100) {
      Serial.print("\n#### Prodigy Board");
    }
    else {
      Serial.print("\n#### Unknown Board");
    }
    Serial.print(" (Board v"); Serial.print((fpga_version >> 4) & 0x000F); Serial.print(".0");
    Serial.print(" / FPGA v"); Serial.print(fpga_version & 0x000F); Serial.print(".0)"); Serial.print(" ####\n");
    Serial.print("\nNM500 is initialized!");
    Serial.print("\nThere are "); Serial.print(hnn.total_neurons); Serial.print(" neurons\n");
  }
  else {
    Serial.print("\nNM500 is NOT properly connected!!");
    Serial.print("\nCheck the connection and Reboot again!\n");
    while (1);
  }

  // if you want to run in lsup mode, uncomment below
  //norm_lsup = 0x80;
  hnn.setGcr(1 + norm_lsup);




}

void loop()
{
    randomd=random(hnn.total_neurons/5,hnn.total_neurons-1);

while(cat_num!=randomd)
{
    randomnum=random(10000,90000);
    //randomnum=random(100,999);
    for(i=0;i<VECTOR_LENGTH;i++)
    {
      //vector[i]=random(0,9);
      //vector[i]=random(0,99)%10;
      vector[i]=randomnum%10;
      randomnum/=10;
      if(i==5) vector[i]=random(0,9);
      //if(i==2) randomnum=random(100,999);
    }

    hnn.learn(vector,VECTOR_LENGTH,cat_num++);
}

    randomd=random(hnn.total_neurons/5,hnn.total_neurons-1);
   // response_nbr = hnn.classify(vector, VECTOR_LENGTH, READ_COUNT, dists, cats, nids);
   while(cat_num!=randomd)
{
    randomnum=random(10000,90000);

    for(i=0;i<VECTOR_LENGTH;i++)
    {
      
      vector[i]=randomnum%10;
      randomnum/=10;
      if(i==5) vector[i]=random(0,9);
     
    }

   response_nbr = hnn.classify(vector, VECTOR_LENGTH);
}

}
