
// This is the library for the TB6612 that contains the class Motor and all the
// functions
#include <SparkFun_TB6612.h>


// IR SENSORS
const int leftPin = A0; // Analog pin for left IR sensor
const int rightPin = A1; // Analog pin for right IR sensor
const int digPinLeft = 6; // digital pin for the IR sensor
int leftVal = 0;//right; // values from left and right analog pins
int thresh = 400;

// MOTOR CONTROL
// Pins for all inputs, keep in mind the PWM defines must be on PWM pins
#define AIN1 1
#define BIN1 10
#define AIN2 2
#define BIN2 11
#define PWMA 3
#define PWMB 5
#define STBY 12

// these constants are used to allow you to make your motor configuration 
// line up with function names like forward.  Value can be 1 or -1
const int offsetA = 1;
const int offsetB = 1;

// Initializing motors.  The library will allow you to initialize as many
// motors as you have memory for.  If you are using functions like forward
// that take 2 motors as arguements you can either write new functions or
// call the function more than once.
Motor motor1 = Motor(AIN1, AIN2, PWMA, offsetA, STBY);
Motor motor2 = Motor(BIN1, BIN2, PWMB, offsetB, STBY);



void setup() {
   Serial.begin(9600); // Starting Serial Terminal
   pinMode(leftPin, INPUT);
//   pinMode(rightPin, INPUT);
   pinMode(digPinLeft,OUTPUT);
}

void loop() {
  
  digitalWrite(digPinLeft,HIGH); 
  delayMicroseconds(500);
  leftVal = analogRead(leftPin);
  
//  right = analogRead(rightPin);

  Serial.println(leftVal);
//  driveControl(left, right);
   
}




void driveControl(int l, int r){

  if(l >=thresh && r >=thresh){
    
  }
  
}
