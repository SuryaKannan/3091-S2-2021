import rospy
import smbus
import time
from sensor_msgs.msg import Range

 # ultrasonics characterstics based on HC-SR04 datasheet

class Ultrasonics:
    def __init__(self,bus_num,address):
        self.bus = smbus.SMBus(bus_num)
        self.address = address
        self.ULTRASONIC_MAX_RANGE = 4 # metres
        self.ULTRASONIC_MIN_RANGE = 0.02 # metres
        self.ULTRASONIC_FOV = 0.261799 # radians
        self.ULTRASONIC_FRAMES = ["front","left","right","back"] 

    def get_data(self):
        return self.bus.read_i2c_block_data(self.address,0)
    
    def get_range_msg(self):
        range_msg = Range()
        range_msg.header.stamp = rospy.get_rostime()
        range_msg.max_range = self.ULTRASONIC_MAX_RANGE
        range_msg.min_range = self.ULTRASONIC_MIN_RANGE
        range_msg.radiation_type = 0
        range_msg.field_of_view = self.ULTRASONIC_FOV

        for i in range (0,6,2):
            range_msg.range = self.get_data()[i]*(1/100)
            print( self.get_data()[i])
            range_msg.header.frame_id = self.ULTRASONIC_FRAMES[int(i/2)]
            return range_msg