/*
 * ECE3091 S2 2021
 * 
 * LIBRARIES REQUIRED:
 * - NewPing
 * 
 * 1) Sends ultrasonic sensor information from Arduino to Jetson Nano via i2c. Up to four ultrasonics are supported (follow pin layout below)
 * 
 * TODO:
 * - Servo control 
 */
 
#include <NewPing.h>
#include <Wire.h>
#include <EnableInterrupt.h>

#define ADDRESS 0x8 // i2c address used 
#define TRIGGER_PIN  5  // Common Trig pin for ultrasonics 
#define ECHO_PIN_F  8  // front ultrasonic
#define ECHO_PIN_L  6  // left ultrasonic
#define ECHO_PIN_R  7  // right ultrasonic
#define MAX_DISTANCE 200 // Maximum distance we want to ping for (in centimeters). Maximum sensor distance is rated at 400-500cm.

NewPing sonarF(TRIGGER_PIN, ECHO_PIN_F, MAX_DISTANCE); // NewPing setup of pins and maximum distance.
NewPing sonarL(TRIGGER_PIN, ECHO_PIN_L, MAX_DISTANCE); 
NewPing sonarR(TRIGGER_PIN, ECHO_PIN_R, MAX_DISTANCE); 

int distF = 0;
int distL = 0;
int distR = 0;

// set up Serial, pins and I2C
void setup() {
  Wire.begin(ADDRESS);
  Wire.onRequest(requestEvent);
  Serial.begin(115200);
}

void loop() { 
  distF = sonarF.ping_cm();
  distL = sonarL.ping_cm();
  distR = sonarR.ping_cm();
  delay(5); 
}


// order of sensor information critical
void requestEvent() {
  byte sensor_data[3];
  sensor_data[0] = distF;
  sensor_data[1] = distL;
  sensor_data[2] = distR;
  Wire.write((byte *) sensor_data, sizeof sensor_data);
  
}
