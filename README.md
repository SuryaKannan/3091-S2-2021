(Currently up to date for Preliminary Competition)
# Table of Contents 
* [Project Description](#Project-Description)
* [Hardware](#Hardware)
* [Electrical Systems](#Electrical-Systems)
* [Getting Started](#Getting-Started)

<p>&nbsp;</p> <!-- This adds a blank space for better formatting -->

## Project Description 

![image info](https://drive.google.com/uc?export=view&id=1b2jhQvuPnSFUgrqFY66ASzxOqHd-cySh)

<div style="text-align: center"> <em><small> Competition Environment </small></em> </div>
<p>&nbsp;</p> <!-- This adds a blank space for better formatting -->

**Task Description:** </p> <!-- This adds a small blank space -->

<div style="text-align: justify"> Build a mobile robot to collect and store as many ball bearings of a known diameter and appearance as possible. Target bearings will be spread across an arena, with distractor bearings intermixed. </div></p> <!-- This adds a small blank space -->

<p>&nbsp;</p> <!-- This adds a blank space for better formatting -->

**Components Used:** </p> <!-- This adds a small blank space -->
* 1 x Dual motor Tamiya gearbox and 2 DC motor with encoders
* 1 x Castor wheel
* 1 x Jetson Nano (4GB)
* 1 x Arduino Nano
* 1 x Motor Controller (TB6612FN)
* 4 x Ultrasonic (HCSR04)
* 1 x Power Bank (ROMOSS 10000mAh 18W)
* 1 x 9V Battery pack 


<p>&nbsp;</p> <!-- This adds a blank space for better formatting -->

## Hardware

<div style="text-align: justify"> The hardware side involves the design, manufacturing and testing of a main chassis which will incorporate all the components, a target storage system, internal distractor filtering ramp, and a target collector mechanism. </div><p>&nbsp;</p> <!-- This adds a blank space for better formatting -->

**Main Chassis** 

![image info](https://drive.google.com/uc?export=view&id=1SaKZ7_BiT9YQSV3fRENJeuLU_HIbt82M)

<div style="text-align: center"> <em> <small>   Chassis Rev_1 (Stage 4) </small> </em> </div><p>&nbsp;</p> <!-- This adds a blank space for better formatting -->

<div style="text-align: justify"> *CAD files for main chassis to be added for Prelim </div><p>

<p>&nbsp;</p> <!-- This adds a blank space for better formatting -->


**Collector Mechanism** 

![image info](https://drive.google.com/uc?export=view&id=18aIIu7qY8epqDhqkewctr5UpcZxTeHqY)

<div style="text-align: center"> <em> <small> CAD of the target collector & filtering mechanism </small> </em> </div><p>&nbsp;</p> <!-- This adds a blank space for better formatting -->

<div style="text-align: justify"> This system consists of a plow, ramp and paddle spindle. The plow (similar to a snow plow) is slightly higher than the diameter of the target balls (¾”) and as such, limits balls larger than this from entering the collector. The wedge design ensures these balls are pushed to the side as the robot moves forward, such that more balls can enter the front of the collector.</div><p>

<div style="text-align: justify"> The paddle spindle consists of 3 paddles on a central axis. This shaft rotates such that the paddles scoop up balls as the robot drives forward and lifts them up the collector ramp, into the main body of the robot to be sorted.</div><p>

<div style="text-align: justify"> Sorting of target and non-target balls will be performed through the use of two rails, with separation slightly less than the target ball diameter. These rails will be sufficiently far apart, to allow balls smaller than the target to fall between the rails and hence be expelled from the robot. Larger balls will be unable to enter the ramp as the collection system plow forbids it. At the end of the rails will be a collection bucket, into which the target balls will fall.
</div><p>

<p>&nbsp;</p> <!-- This adds a blank space for better formatting -->

## Electrical Systems

![image info](https://drive.google.com/uc?export=view&id=1_SBrAYby1Y6_gDqdjETlYF3MSmqmZ6kh)

<div style="text-align: center"> <em> <small> Electrical connections </small> </em> </div><p>&nbsp;</p> <!-- This adds a blank space for better formatting -->

<div style="text-align: justify"> The electrical systems is powered by a portable powerbank (5V/2A) for the Jetson and six AA battery pack (9V/~A). This is expected to power the robot continuously for 30 ~ 60 minutes for a continuous load. </div><p>&nbsp;</p> <!-- This adds a blank space for better formatting -->

<p>&nbsp;</p> <!-- This adds a blank space for better formatting -->

![image info](https://drive.google.com/uc?export=view&id=1Q0cyPoy3SEyYIGaxuXpn_PN30Whs4alb)

<div style="text-align: center"> <em> <small> Electrical Loom for Preliminary Competition</small> </em> </div><p>&nbsp;</p> <!-- This adds a blank space for better formatting -->

## Getting Started 

#### Installation 
Setup Jetson to run ROS and Arduino IDE
- Tested with ROS Melodic with Jetpack 4.5

#### TODO:
```python
  - install.sh
  - requirements.py
  - setting up GPIO pins 
  - test scripts
```

#### How to run

(For Preliminary Competition)

```bash 
  $ roslaunch comms comms.launch
```
- wait until encoder nodes are running
```bash 
  $ rosrun comms republisher
```

```bash 
  $ roslaunch diff_drive demo.launch
```

 Publish position coordinates to 
 ```bash 
 "/diff_drive_to_goal/goal"
``` 
- Input position must be based on the robotics coordinate system

#### Features
- Move to desired position in a 2D space
- Dynamic obstacle avoidance and replanning (tailored for the preliminary competition setup)


<h1>&nbsp;</h1> 

Authors: 
- Kevin Lee
- Kurtis Brandt
- Jin Siang Ong
- Surya Kannan

