/*
 * ECE3091 S2 2021
 * 
 * Author: Surya Kannan 
 * 
 * 1) Sends ultrasonic sensor information from Arduino to Jetson Nano via i2c. Up to four ultrasonics are supported (follow pin layout below)
 * 2) Sends commands to 360g Servo for continuous rotation 
 * 
 * 
 */
#include <Servo.h>
#include <Wire.h>

Servo myServo;

#define ADDRESS 0x8 // i2c address used 

#define servoPin 9

// pin defintions for ultrasonics 
#define echoPin_R 5
#define trigPin_R 6
#define echoPin_L 7 
#define trigPin_L 8 

long distance_L, distance_R;

int dist(int trigPin, int echoPin);
void requestEvent();

void setup() {
  myServo.attach(servoPin);
  pinMode(trigPin_R, OUTPUT); 
  pinMode(echoPin_R, INPUT); 
  pinMode(trigPin_L, OUTPUT); 
  pinMode(echoPin_L, INPUT); 
  Wire.begin(ADDRESS);
  Wire.onRequest(requestEvent);
  Serial.begin(9600);
  
}

void loop() {
  myServo.write(0); //0 is full speed in one direction, 180 is full speed in the other direction
  distance_R = dist(trigPin_R,echoPin_R);
  distance_L = dist(trigPin_L,echoPin_L);
  Serial.print(distance_R);
  Serial.println();
  
}

// code from https://create.arduino.cc/projecthub/abdularbi17/ultrasonic-sensor-hc-sr04-with-arduino-tutorial-327ff6
int dist(int trigPin, int echoPin){
  
  // Clears the trigPin condition
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  int duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  return duration * 0.034 / 2; // Speed of sound wave divided by 2 (go and back)
  
}

// order of sensor information critical
void requestEvent() {
  
  long sensor_data[4];
  sensor_data[0] = distance_R;
  //sensor_data[1] = distance_L;
  Wire.write((byte *) sensor_data, sizeof sensor_data);
  
}
