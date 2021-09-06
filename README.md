# Table of Contents 
* [Project Description](#project-Description)
* [Hardware](#hardware)
* [Software](#software)
* [Limitations](#limitations)
* [Testing](#testing) 
* [How to get started](#how-to-get-started)

<p>&nbsp;</p> <!-- This adds a blank space for better formatting -->

## Project Description 

![image info](https://drive.google.com/uc?export=view&id=1b2jhQvuPnSFUgrqFY66ASzxOqHd-cySh)

<div style="text-align: center"> <em><small> figure 1 - Competition Environment </small></em> </div>
<p>&nbsp;</p> <!-- This adds a blank space for better formatting -->

**Task Description:** </p> <!-- This adds a small blank space -->

<div style="text-align: justify"> Build a mobile robot to collect and store as many ball bearings of a known diameter and appearance as possible. Target bearings will be spread across an arena, with distractor bearings intermixed. </div></p> <!-- This adds a small blank space -->

<div style="text-align: justify"> Two robots will compete simultaneously to collect bearings, 10 points obtained for every correct bearing captured. A 5 point penalty will be deducted every time a robot incorrectly collects the wrong bearing, collides with the arena walls, or with the rival robot.</div>


<p>&nbsp;</p> <!-- This adds a blank space for better formatting -->

**Provided Components:** </p> <!-- This adds a small blank space -->
* 1 x Dual motor Tamiya gearbox and 2 DC motor
* 1 x Motor encoder
* 1 x Castor wheel
* 1 x Standard robot base
* 1 x Raspberry Pi model 4 B+ and power supply
* 1 x Raspberry Pi camera module
* <div style="text-align: justify"> 3 x Servo motors to build a pan-tilt unit to move the camera or design a suitable bearing collection mechanism  </div>
* 4 x Ultrasonic units for obstacle avoidance

<div style="text-align: justify"> **The component regulations are flexible enough to allow the team to substitute different parts for required design specifications. </div>


<p>&nbsp;</p> <!-- This adds a blank space for better formatting -->




## Hardware

<div style="text-align: justify"> The hardware side involves the design, manufacturing and testing of a main chassis which will incorporate all the components, a target storage system, internal distractor filtering ramp, and a target collector mechanism. </div><p>&nbsp;</p> <!-- This adds a blank space for better formatting -->

**Main Chassis** 

![image info](https://drive.google.com/uc?export=view&id=1SaKZ7_BiT9YQSV3fRENJeuLU_HIbt82M)

<div style="text-align: center"> <em> <small> figure 2 - Chassis Rev_1 (Stage 4) </small> </em> </div><p>&nbsp;</p> <!-- This adds a blank space for better formatting -->

<div style="text-align: justify"> The drive function is satisfied by a Tamiya DC motor gearbox. This gearbox has been assembled at a ratio of 114.7:1. The gearbox motors consume 48mA (no load) of current and spin at 7000 RPM at 12V, as detailed in the AliExpress listing for the product [1]. Assuming a lower motor speed of 5000 RPM at 9V, this achieves a gearbox output speed of 44 RPM. Coupled with the 56mm diameter of the wheels, the robot should be able to drive at approximately 13cm per second. </div><p>

<div style="text-align: justify"> The robot has a castor “wheel” (sphere) to stabilise the chassis rear as the gearbox motors pull it forwards. Steering will be achieved by slowing the speed of one motor relative to the other. This produces a skid steering system. Despite the name, this system will involve little skidding, as the caster wheel is omnidirectional. </div><p>

<div style="text-align: justify"> The packaging....
</div><p>

<p>&nbsp;</p> <!-- This adds a blank space for better formatting -->


**Collector Mechanism** 

![image info](https://drive.google.com/uc?export=view&id=18aIIu7qY8epqDhqkewctr5UpcZxTeHqY)

<div style="text-align: center"> <em> <small> figure 3 - CAD of the target collector & filtering mechanism </small> </em> </div><p>&nbsp;</p> <!-- This adds a blank space for better formatting -->

<div style="text-align: justify"> The robot must be able to collect target bearings and place them into the sorting system. This will be achieved by a rotating paddle system, as seen in figure 6. </div><p>

<div style="text-align: justify"> This system consists of a plow, ramp and paddle spindle. The plow (similar to a snow plow) is slightly higher than the diameter of the target balls (¾”) and as such, limits balls larger than this from entering the collector. The wedge design ensures these balls are pushed to the side as the robot moves forward, such that more balls can enter the front of the collector.</div><p>

<div style="text-align: justify"> The paddle spindle consists of 3 paddles on a central axis. This shaft rotates such that the paddles scoop up balls as the robot drives forward and lifts them up the collector ramp, into the main body of the robot to be sorted.</div><p>

<div style="text-align: justify"> Sorting of target and non-target balls will be performed through the use of two rails, with separation slightly less than the target ball diameter. These rails will be sufficiently far apart, to allow balls smaller than the target to fall between the rails and hence be expelled from the robot. Larger balls will be unable to enter the ramp as the collection system plow forbids it. At the end of the rails will be a collection bucket, into which the target balls will fall.
</div><p>

<p>&nbsp;</p> <!-- This adds a blank space for better formatting -->





## Electrical Systems

![image info](https://drive.google.com/uc?export=view&id=1_SBrAYby1Y6_gDqdjETlYF3MSmqmZ6kh)

<div style="text-align: center"> <em> <small> figure 4 - Electrical connections </small> </em> </div><p>&nbsp;</p> <!-- This adds a blank space for better formatting -->

<div style="text-align: justify"> The electrical systems is powered by a portable powerbank (5V/2A) for the Jetson and six AA battery pack (9V/~A). This is expected to power the robot continuously for 30 ~ 60 minutes depending on the load. </div><p>&nbsp;</p> <!-- This adds a blank space for better formatting -->

<p>&nbsp;</p> <!-- This adds a blank space for better formatting -->

![image info](https://drive.google.com/uc?export=view&id=1Q0cyPoy3SEyYIGaxuXpn_PN30Whs4alb)

<div style="text-align: center"> <em> <small> figure 5 - Electrical Loom </small> </em> </div><p>&nbsp;</p> <!-- This adds a blank space for better formatting -->


 


## Software

<div style="text-align: justify"> The software stack will be ROS (robot operating system) based, allowing for modularity in the overall software design. Another benefit of ROS is the availability of pre-written software packages that may be used to implement the proposed solution to the task. </div><p>&nbsp;</p> <!-- This adds a blank space for better formatting -->

![image info](https://drive.google.com/uc?export=view&id=10NtWm_d3gjM1_FEa4M_SXkmJAVIL19JQ)

<div style="text-align: center"> <em> <small> figure 6 - Logic flow diagram of software </small> </em> </div><p>&nbsp;</p> <!-- This adds a blank space for better formatting -->


**Sensors**

* <div style="text-align: justify"> A ROS driver for the Pi camera will be used to convert images into ROS format.</div><p>
 * <div style="text-align: justify"> A ROS driver for the Pi camera will be used to convert images into ROS format.</div><p>&nbsp;</p>

**Perception**

* <div style="text-align: justify"> As OpenCV is preinstalled with ROS, it allows for quick development if classical computer vision techniques are used in target detection. If a large enough training dataset is collected, using transfer learning with a pre-trained model, such as TinyYolo, could also be considered.</div><p>
* <div style="text-align: justify"> Using two Raspberry Pi cameras in a stereo configuration will allow a depth map to be created. This, in combination with correctly detected target bearings, will allow positional information of target bearings to be known in known 2D space. These will be used as a set of goal markers for the planning system. </div><p>
* <div style="text-align: justify"> Ultrasonics will primarily be used as part of a collision avoidance system. ROS, having node priority functionality, will allow the robot to maneuver to safety in the event of an imminent collision. </div><p>
* <div style="text-align: justify"> The encoders attached to the DC motors, combined with an initial position gathered from the ultrasonics, will be used to localise the robot. </div><p>&nbsp;</p>


**Planning**

* <div style="text-align: justify"> Goal markers created from the detected target bearings in 2D space will be used to facilitate the planning process. Because of the existence of an internal sorting system, the quickest path towards target bearings (straight lines) will be taken.</div><p>
* <div style="text-align: justify"> The costmap will be used to facilitate the planned paths the robot will use to navigate to target bearings. This costmap will constantly be updated with the latest or last known position of the opponent robot assigning it a higher cost. This will enable the shortest and safest path to be chosen without collision.</div><p>&nbsp;</p>

**Control**

* <div style="text-align: justify"> Sending physical signals to the actuators on the robot to allow it to move towards the target bearings. A PID controller will be used to correct any deviations from the planned paths.</div><p>&nbsp;</p>






## Limitations

<div style="text-align: justify"> The limitations... </div><p>&nbsp;</p> <!-- This adds a blank space for better formatting -->




<p>&nbsp;</p> <!-- This adds a blank space for better formatting -->






## Testing

<div style="text-align: justify"> Testing... </div><p>&nbsp;</p> <!-- This adds a blank space for better formatting -->



<p>&nbsp;</p> <!-- This adds a blank space for better formatting -->







## How to get started

<div style="text-align: justify"> First... </div><p>&nbsp;</p> <!-- This adds a blank space for better formatting -->




<p>&nbsp;</p> <p>&nbsp;</p><p>&nbsp;</p>

<div style="text-align: justify"><small> <b>Written  by: The Autobots - Team 4 of ECE3091, Department of Electrical and Computer Systems Engineering, Monash University </b></small></div><p>&nbsp;</p> 

