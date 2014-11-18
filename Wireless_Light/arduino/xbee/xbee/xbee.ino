/**
 * Copyright (c) 2009 Andrew Rapp. All rights reserved.
 *
 * This file is part of XBee-Arduino.
 *
 * XBee-Arduino is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * XBee-Arduino is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with XBee-Arduino.  If not, see <http://www.gnu.org/licenses/>.
 */

#include <XBee.h>
#include <SoftwareSerial.h>

/*
This example is for Series 1 XBee (802.15.4)
Receives either a RX16 or RX64 packet and sets a PWM value based on packet data.
Error led is flashed if an unexpected packet is received
*/
SoftwareSerial onboardSerial(0,1);
XBee xbee = XBee();
XBeeResponse response = XBeeResponse();
// create reusable response objects for responses we expect to handle 
Rx16Response rx16 = Rx16Response();
Rx64Response rx64 = Rx64Response();

int redLed = A5;
int greenLed = A3;
int blueLed = A4;

uint8_t option = 0;
uint8_t data = 0;

void setup() 
{
    pinMode(redLed, OUTPUT);
    pinMode(greenLed, OUTPUT);
    pinMode(blueLed,  OUTPUT);
  
    onboardSerial.begin(9600);
    delay(100);
    xbee.setSerial(onboardSerial);
   
    // start serial
    Serial.begin(9600);
    Serial.print ("Hello from Arduino!\n");
}

void handleData(char* cmdBuf)
{
    switch (cmdBuf[0])
    {
        case 'r':
          if (cmdBuf[1] == '1') 
          {
              digitalWrite(redLed, HIGH);
              digitalWrite(greenLed, LOW);
              digitalWrite(blueLed, LOW);
          }
          else digitalWrite(redLed, LOW);
          break;
        case 'g':
          if (cmdBuf[1] == '1')
          {
              digitalWrite(redLed, LOW);
              digitalWrite(greenLed, HIGH);
              digitalWrite(blueLed, LOW);
          }
          else digitalWrite(greenLed, LOW);
          break;
        case 'b':
          if (cmdBuf[1] == '1') 
          {
              digitalWrite(redLed, LOW);
              digitalWrite(greenLed, LOW);
              digitalWrite(blueLed, HIGH);
          }
          else digitalWrite(blueLed, LOW);
          break;
    }
}

// continuously reads packets, looking for RX16 or RX64
void loop() 
{
    const int CMD_LENGTH = 4;
    char cmdBuf[CMD_LENGTH] = {};
    int count = 0;
    int startTime = millis();
    int currentTime;
    
    while (count < CMD_LENGTH)
    {
     currentTime = millis();
     if (currentTime - startTime > 500) 
     {  
       handleData(cmdBuf);
       break;
     }
     
     xbee.readPacket();
     if (xbee.getResponse().isAvailable()) {
      // got something
      
      if (xbee.getResponse().getApiId() == RX_16_RESPONSE || xbee.getResponse().getApiId() == RX_64_RESPONSE) 
      {
        // got a rx packet
        
        if (xbee.getResponse().getApiId() == RX_16_RESPONSE) {
                xbee.getResponse().getRx16Response(rx16);
        	option = rx16.getOption();
        	data = rx16.getData(0);
        } 
        else{
                xbee.getResponse().getRx64Response(rx64);
        	option = rx64.getOption();
        	data = rx64.getData(0);
        }
        
        cmdBuf[count] = data;
        count++;
        }
      }
      
     }
    if (cmdBuf[0]  > 0 || cmdBuf[1]  > 0 || cmdBuf[2]  > 0 || cmdBuf[3]  > 0)
    {
      Serial.print("\nData: ");
      Serial.println(cmdBuf);
      Serial.print("\n");
    }
}
