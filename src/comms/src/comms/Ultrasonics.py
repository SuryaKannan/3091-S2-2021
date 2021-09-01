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
    
    def generate_empty_range(self):
        empty_range_msg = Range()
        empty_range_msg.header.stamp = rospy.get_rostime()
        empty_range_msg.max_range = self.ULTRASONIC_MAX_RANGE
        empty_range_msg.min_range = self.ULTRASONIC_MIN_RANGE
        empty_range_msg.radiation_type = 0
        empty_range_msg.field_of_view = self.ULTRASONIC_FOV
        return empty_range_msg
    
    def get_range(self,position):
        range_msg = self.generate_empty_range()
        range_msg.header.frame_id = position
        range_msg.range = self.get_data()[self.ULTRASONIC_FRAMES.index(position)] # divide by 100 for metres 
        return range_msg


