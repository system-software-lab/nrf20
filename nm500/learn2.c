/*
    Copyright (C) 2018-2019 by nepes Corp. All Rights Reserved
    
    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:
    
    1. Redistributions of source code must retain the above copyright notice,
    this list of conditions and the following disclaimer.
    
    2. Redistributions in binary form must reproduce the above copyright notice,
    this list of conditions and the following disclaimer in the documentation
    and/or other materials provided with the distribution.
    
    3. Neither the name of the copyright holder nor the names of its contributors
    may be used to endorse or promote products derived from this software without
    specific prior written permission.
    
    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
    ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
    LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
    CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
    SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
    INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
    CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
    ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
    POSSIBILITY OF SUCH DAMAGE.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#include "nmengine.h"

int main(int argc, char **argv) 
{
    uint16_t r;
    double st_time=0;
    nm_device ds[10];
    uint8_t detect_count = 10;
    srand(time(NULL));
    char buffer[643];
    u_int8_t buf[160];
    char* ptr;
    FILE *fp=fopen("train34.txt","r");
    int i=0;
    // Gets information of devices attached
    r = nm_get_devices(ds, &detect_count);
    if (r != NM_SUCCESS) {
        if (r == NM_ERROR_DEVICE_NOT_FOUND) {
            printf("There is no detected device.\n");
        }
        else {
            printf("[devices] Failed to get device list %d\n", r);
        }
        return 0;
    }

    if (detect_count < 1) {
        printf("There is no detected device.\n");
        return 0;
    }

    printf("%d device(s) detected\n", detect_count);
    for (int i = 0; i < detect_count; i++) {    
        printf("Device ID: %d, Type: %d, PID: %d, VID: %d\n", i, ds[i].type, ds[i].vid, ds[i].pid);
    }

    // Select a device to use.
    nm_device *target = &ds[0];

    // Connects to target device
    r = nm_connect(target);
    if (r != NM_SUCCESS) {
        printf("Failed to init the Device, Error: %d, or Not supported device\n", r);
        return 0;
    }
    // Reset network
    r = nm_forget(target);
    if (r != NM_SUCCESS) {
        printf("Failed to reset network, Error: %d\n", r);
        return 0;
    }

    // Sets network context
    nm_context ctx;
    ctx.context = 1;
    ctx.norm = L1;
    ctx.minif = 2;
    ctx.maxif = 1000;

    r = nm_set_context(target, &ctx);
    if (r != NM_SUCCESS) {
        printf("Failed to set context, Error: %d\n", r);
        return 0;
    }

    // The vector size for learning is up to 256.
    uint16_t vector_size =160;

    // Learns feature vector [10, 10, 10] by category 10
    uint8_t data = 10;
    uint16_t cat = 10;

    nm_learn_req req;
    memset(&req, 0, sizeof req);

    // Sets query_affected to 1 for retrieving the affected neurons
    // It will affect device performance (latency)
    // Use for testing/debugging purposes only.
    req.query_affected = 0;
    printf("\nLearn vector: ");
    /*
    for (int i = 0; i < vector_size; i++) {
       // req.vector[i] = data;
        req.vector[i] =rand()%256; 
        //printf(" %d", data);
    }*/
    fgets(buffer,sizeof(buffer),fp);
    ptr=strtok(buffer,",");
    while(ptr!=NULL)
    {
	    req.vector[i]=atoi(ptr);
	    ptr=strtok(NULL,",");
	    i++;
    }
	fclose(fp);
    // Set the size of vector
    req.vector_size = vector_size;
    req.category = cat;
    printf(", Cat: %d", cat);
    st_time=clock();
    r = nm_learn(target, &req);
    printf("time: %f\n",clock()-st_time);
    if (r == NM_SUCCESS) {
        printf(", Result: %d\n", req.status);

        // Prints affected neurons 
        if (req.query_affected == 1) {
            for (int i = 0; i < req.affected_count; i++) {
                printf("Affected neuron nid: %d, cat: %d, aif: %d\n", 
                req.affected_neurons[i].nid, 
                req.affected_neurons[i].cat, 
                req.affected_neurons[i].aif);
            }
        }
    }
    else {
        printf("\nError: Failed to learn. %d\n", r); 
    }

    nm_close(target);

    return 0;
}
