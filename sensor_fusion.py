# SESSION 13 – Sensor Fusion

# Step 1: Input values
imu = 32      # IMU reading in degrees
vision = 28   # Vision estimate in degrees

# Step 2: Compute fused angle
fused = (imu + vision) / 2

# Step 3: Display result
print("Fused Angle =", fused, "degrees")

print("\nProgram Executed Successfully")
