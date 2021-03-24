
// This is the library for the TB6612 that contains the class Motor and all the
// functions
#include <SparkFun_TB6612.h>


// IR SENSORS
const int leftPin = A0; // Analog pin for left IR sensor
const int rightPin = A1; // Analog pin for right IR sensor
const int digPinLeft = 6; // digital pin for left IR sensor
const int digPinRight = 7; // digital pin for right IR sensor
int leftVal, rightVal; // values from left and right analog pins
int threshLeft = 600;
int threshRight = 500;

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
Motor motor1 = Motor(AIN1, AIN2, PWMA, offsetA, STBY); // right
Motor motor2 = Motor(BIN1, BIN2, PWMB, offsetB, STBY); // left

int botSpeed = 75;


void setup() {
   Serial.begin(9600); // Starting Serial Terminal
   pinMode(leftPin, INPUT);
   pinMode(rightPin, INPUT);
   pinMode(digPinLeft,OUTPUT);
   delay(1000);
}

void loop() {
  
  digitalWrite(digPinLeft,HIGH); 
  delayMicroseconds(500);
  leftVal = analogRead(leftPin);
  digitalWrite(digPinLeft,LOW); 



  digitalWrite(digPinRight,HIGH); 
  delayMicroseconds(500);
  rightVal = analogRead(rightPin);
  digitalWrite(digPinRight,LOW); 

  
  Serial.print(leftVal);
  Serial.print(", ");
  Serial.println(rightVal);
//  left(motor1, motor2,75);
  driveControl(leftVal, rightVal);
  delay(50);
}




void driveControl(int l, int r){

  if((l >= threshLeft) && (r >=threshRight)){
    brake(motor1, motor2); 
    Serial.println("If #1");
  }
  
  if((l >=threshLeft) && !(r >= threshRight)){
    right(motor1, motor2, botSpeed); 
    Serial.println("If #2");
  }

  if(!(l >=threshLeft) && (r >=threshRight)){
    left(motor1, motor2, botSpeed); 
    Serial.println("If #3");
  }

  if(!(l >=threshLeft) && !(r >=threshRight)){
    forward(motor1, motor2, botSpeed); 
    Serial.println("If #4");
  }
}
