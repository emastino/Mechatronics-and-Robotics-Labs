/*
  Arduino Slave for Raspberry Pi Master
  i2c_slave_ard.ino
  Connects to Raspberry Pi via I2C
  
  DroneBot Workshop 2019
  https://dronebotworkshop.com
*/

// Include the Wire library for I2C
#include <Wire.h>

// Commands
String c = "";


// LED on pin 2
const int ledPin = 2; 

void setup() {
  // Ouput Serial 
  Serial.begin(9600);
  
  // Join I2C bus as slave with address 8
  Wire.begin(0x08);
  
  // Call receiveEvent when data received                
  Wire.onReceive(receiveEvent);
  
  // Setup pin 2 as output and turn LED off
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
}

// Function that executes whenever data is received from master
void receiveEvent(int howMany) {
  
  c="";
  Wire.read();
 
  while (Wire.available()) { // loop through all but the last
    c += (char)Wire.read(); // receive byte as a character
  }


}
void loop() {

  if (c == "ON"){
    digitalWrite(ledPin, HIGH);
    Serial.println("ON...");
  }
  if (c == "OFF"){
    digitalWrite(ledPin, LOW);
    Serial.println("OFF...");
  }
 
  delay(100);
}
