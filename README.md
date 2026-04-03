# APPLE-Sensor-Fusion-
#Aim
To compute the fused orientation angle using sensor fusion.
General Objective
To understand the concept of sensor fusion and how combining data from multiple sensors (IMU and Vision) improves accuracy and reliability in autonomous systems.
Specific Objective
To compute fused angle using:
θ
f
u
s
e
d
=
θ
i
m
u
+
θ
v
i
s
i
o
n
2
θ 
fused
​	
 = 
2
θ 
imu
​	
 +θ 
vision
​	
 
​	
 
Given:
IMU = 32°
Vision = 28°
Dataset
EuRoC MAV Dataset
Source: ETH Zurich
Procedure
Input IMU angle
Input vision-based angle
Apply averaging formula
Compute fused angle
Display result
Algorithm
Start
Input IMU and vision values
Compute fused value
Display result
Stop
Code Logic
fused = (imu + vision) / 2
Python Code
# SESSION 13 – Sensor Fusion

# Step 1: Input values
imu = 32      # IMU reading in degrees
vision = 28   # Vision estimate in degrees

# Step 2: Compute fused angle
fused = (imu + vision) / 2

# Step 3: Display result
print("Fused Angle =", fused, "degrees")

print("\nProgram Executed Successfully")
Output
Fused Angle = 30.0 degrees

Program Executed Successfully
Result
The fused orientation angle is:
30°
Industry Application
Sensor fusion is widely used in:
Robotics
Autonomous vehicles
AR/VR systems
Smartphones
Companies like Apple Inc. use this in:
iPhones (IMU + camera fusion)
ARKit
Motion tracking systems
Conclusion
Sensor fusion improves accuracy by combining multiple data sources, making it essential for reliable perception in modern intelligent systems.
