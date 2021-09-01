/*
 * ECE3091 S2 2021
 * 
 * Author: Surya Kannan 
 * 
 * 1) Sends ultrasonic sensor information from Arduino to Jetson Nano via i2c. Up to four ultrasonics are supported (follow pin layout below)
 * 2) Sends encoder tick information to Jetson via i2c
 * 
 * 
 * LIBRARIES REQUIRED:
 * - NewPing
 * - EnableInterrupt
 * 
 */
#include <NewPing.h>
#include <Wire.h>
#include <EnableInterrupt.h>

#define ADDRESS 0x8 // i2c address used 
#define TRIGGER_PIN  6  // Arduino pin tied to trigger pin on the ultrasonic sensor.
#define ECHO_PIN     5  // Arduino pin tied to echo pin on the ultrasonic sensor.
#define MAX_DISTANCE 200 // Maximum distance we want to ping for (in centimeters). Maximum sensor distance is rated at 400-500cm.

NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE); // NewPing setup of pins and maximum distance.

int dist = 0;

#define M1phaseA 2
#define M1phaseB 3

#define M2phaseA 10
#define M2phaseB 9

long int M1countA = 0;
long int M1countB = 0;
long int M2countA = 0;
long int M2countB = 0;

int M1dir = 0;
int M2dir = 0;

void setup() {
  Wire.begin(ADDRESS);
  Wire.onRequest(requestEvent);
  Serial.begin(115200);
  pinMode(M2phaseA,INPUT);
  pinMode(M2phaseB,INPUT);
  pinMode(M1phaseA,INPUT);
  pinMode(M1phaseB,INPUT);
  enableInterrupt(M2phaseA,M2pulseA,RISING);
  enableInterrupt(M2phaseB,M2pulseB,RISING);
  enableInterrupt(M1phaseA,M1pulseA,RISING);
  enableInterrupt(M1phaseB,M1pulseB,RISING);
}

void loop() { 
  dist = sonar.ping_cm();
  delay(5); 
  send_encoder_data();
}

void send_encoder_data(){
  Serial.print(M1countA);
  Serial.print(",");
  Serial.print(M1countB);
  Serial.print(",");
  Serial.print(M2countA);
  Serial.print(",");
  Serial.print(M2countB);
  Serial.println();
}

// order of sensor information critical
void requestEvent() {
  long sensor_data[1];
  sensor_data[0] = dist;
  Wire.write((byte *) sensor_data, sizeof sensor_data);
  
}


void M2checkDirection(){
  if(digitalRead(M2phaseB) == HIGH){
    M2dir = 1;
  }
  else {
    M2dir = -1;
  }
}

void M1checkDirection(){
  if(digitalRead(M1phaseB) == HIGH){
    M1dir = 1;
  }
  else {
    M1dir = -1;
  }
}

void M2pulseA(){
  M2checkDirection();
  M2countA += M2dir;
}

void M2pulseB(){
  M2countB += M2dir;
}

void M1pulseA(){
  M1checkDirection();
  M1countA += M1dir;
}

void M1pulseB(){
  M1countB += M1dir;
}
