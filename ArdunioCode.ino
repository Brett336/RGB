#include <IRremote.h>
#include <stdlib.h>
#include <WString.h>

String hexcode;
uint32_t num;
unsigned long test = 16203967 ; 


IRsend irsend;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  while (Serial.available()) {
    delay(10);  //delay to allow buffer to fill 
    if (Serial.available() >0) {
      char c = Serial.read();  //gets one byte from serial buffer
      //readString += c; //makes the string readString
      hexcode = hexcode + c;
      
    } 

  }
  num = strtoul(hexcode.c_str(), NULL, 16);
  //num=num+"ul";
  if (num != 0) {
      
      Serial.println(num, HEX);
      irsend.sendNEC(num, 32);
      num = 0;
      hexcode = "";
      delay(100);
      
  }
  

}
