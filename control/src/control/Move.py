import RPi.GPIO as GPIO
import time 

class MyRobotGPIO():
    def __init__(self):
        self.outL = 32
        self.outR = 33
        self.dirL = 11
        self.dirR = 12
        GPIO.setmode(GPIO.BOARD) #use numbering system on board 
        GPIO.setup(self.outR,GPIO.OUT) # similar to arduino
        GPIO.setup(self.dirR,GPIO.OUT)
        GPIO.setup(self.outL,GPIO.OUT) 
        GPIO.setup(self.dirL,GPIO.OUT)
        self.pwmR = GPIO.PWM(self.outR,100) 
        self.pwmR.start(0)
        self.pwmR.ChangeDutyCycle(0)
        self.pwmL = GPIO.PWM(self.outL,100) 
        self.pwmL.start(0)
        self.pwmL.ChangeDutyCycle(0)
    
    def set_dirL(self,dir):
        GPIO.output(self.dirL,dir)

    def set_dirR(self,dir):
        GPIO.output(self.dirR,dir)

class Move:
    def __init__(self):
        self.gpio = MyRobotGPIO()
        self.forward_speed = 30
        self.turn_speed = 15
        self.rotate_speed = 23
        self.slow_speed = 15

    def forward(self):
        self.gpio.set_dirL(True)
        self.gpio.set_dirR(True)
        self.gpio.pwmL.ChangeDutyCycle(33)
        self.gpio.pwmR.ChangeDutyCycle(self.forward_speed)
    
    def left(self):
        self.gpio.set_dirL(True)
        self.gpio.set_dirR(True)
        self.gpio.pwmL.ChangeDutyCycle(self.turn_speed)
        self.gpio.pwmR.ChangeDutyCycle(self.forward_speed)
    
    def right(self):
        self.gpio.set_dirL(True)
        self.gpio.set_dirR(True)
        self.gpio.pwmL.ChangeDutyCycle(self.forward_speed)
        self.gpio.pwmR.ChangeDutyCycle(self.turn_speed)
    
    def left_slight(self):
        self.gpio.set_dirL(True)
        self.gpio.set_dirR(True)
        self.gpio.pwmL.ChangeDutyCycle(int(self.turn_speed*1.25))
        self.gpio.pwmR.ChangeDutyCycle(self.forward_speed)
    
    def right_slight(self):
        self.gpio.set_dirL(True)
        self.gpio.set_dirR(True)
        self.gpio.pwmL.ChangeDutyCycle(self.forward_speed)
        self.gpio.pwmR.ChangeDutyCycle(int(self.turn_speed*1.25))
    
    def clockwise(self):
        self.gpio.set_dirL(True)
        self.gpio.set_dirR(False)
        self.gpio.pwmL.ChangeDutyCycle(self.rotate_speed)
        self.gpio.pwmR.ChangeDutyCycle(self.rotate_speed)
    
    def anticlockwise(self):
        self.gpio.set_dirL(False)
        self.gpio.set_dirR(True)
        self.gpio.pwmL.ChangeDutyCycle(self.rotate_speed)
        self.gpio.pwmR.ChangeDutyCycle(self.rotate_speed)
    
    def slow(self):
        self.gpio.set_dirL(True)
        self.gpio.set_dirR(True)
        self.gpio.pwmL.ChangeDutyCycle(self.slow_speed)
        self.gpio.pwmR.ChangeDutyCycle(self.slow_speed)
    
    def back(self):
        self.gpio.set_dirL(False)
        self.gpio.set_dirR(False)
        self.gpio.pwmL.ChangeDutyCycle(self.slow_speed)
        self.gpio.pwmR.ChangeDutyCycle(self.slow_speed)

    def stop(self):
        self.gpio.pwmL.ChangeDutyCycle(0)
        self.gpio.pwmR.ChangeDutyCycle(0)