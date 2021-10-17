/*
 * ECE3091 S2 2021 - Group 4
 * 
 * LIBRARIES REQUIRED:
 * - NewPing
 * - EnableInterrupt
 * 
 * 1) Sends ultrasonic sensor information from Arduino to Jetson Nano via i2c. Up to four ultrasonics are supported (follow pin layout below)
 * 2) Sends servo speed once and maintains that speed
 */
 
#include <NewPing.h>
#include <Wire.h>
#include <EnableInterrupt.h>
#include <Servo.h>

#define ADDRESS 0x8 // i2c address used 
#define TRIGGER_PIN_1  5  // Common Trig pin 1 for ultrasonics 
#define TRIGGER_PIN_2  12  // Common Trig pin 1 for ultrasonics 
#define ECHO_PIN_F  8  // front ultrasonic
#define ECHO_PIN_L  4  // left ultrasonic
#define ECHO_PIN_R  6  // right ultrasonic
#define ECHO_PIN_B  2  // back ultrasonic
#define SERVO_PIN 9 // digital pin 9
#define MAX_DISTANCE 200 // Maximum distance we want to ping for (in centimeters). Maximum sensor distance is rated at 400-500cm.

NewPing sonarF(TRIGGER_PIN_1, ECHO_PIN_F, MAX_DISTANCE); // NewPing setup of pins and maximum distance.
NewPing sonarL(TRIGGER_PIN_2, ECHO_PIN_L, MAX_DISTANCE); 
NewPing sonarR(TRIGGER_PIN_1, ECHO_PIN_R, MAX_DISTANCE); 
NewPing sonarB(TRIGGER_PIN_2, ECHO_PIN_B, MAX_DISTANCE); 

int distF = 0;
int distL = 0;
int distR = 0;
int distB = 0;

Servo paddleServo;
int servoSpeed = 70; // servo speed, 70 appears to be the magic number

// set up Serial, pins and I2C
void setup() {
  Wire.begin(ADDRESS);
  Wire.onRequest(requestEvent);

  paddleServo.attach(SERVO_PIN);
  paddleServo.write(servoSpeed);

  Serial.begin(115200);
}

void loop() { 
  distF = sonarF.ping_cm();
  distL = sonarL.ping_cm();
  distR = sonarR.ping_cm();
  distB = sonarB.ping_cm();
  delay(5); 

  // UNCOMMENT FOR TESTING
  /*
  Serial.print("F: ");
  Serial.print(distF);
  Serial.print('\t');
  
  Serial.print("L: ");
  Serial.print(distL);
  Serial.print('\t');
  Serial.print("R: ");
  Serial.print(distR);
  Serial.print('\t');
   
  Serial.print("B: ");
  Serial.println(distB);
  */ 
}

// order of sensor information critical
void requestEvent() {
  byte sensor_data[4];
  sensor_data[0] = distF;
  sensor_data[1] = distL;
  sensor_data[2] = distR;
  sensor_data[3] = distB;
  Wire.write((byte *) sensor_data, sizeof sensor_data);  
}
