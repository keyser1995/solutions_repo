import numpy as np
import matplotlib.pyplot as plt

# Define parameters
v_0 = 20  # initial velocity in m/s
g = 9.81  # acceleration due to gravity in m/s^2
angles = np.linspace(0, 90, 100)  # Launch angles from 0 to 90 degrees
angles_rad = np.radians(angles)  # Convert angles to radians

# Calculate the range for each angle
range_values = (v_0**2 * np.sin(2 * angles_rad)) / g

# Plot the range as a function of angle
plt.plot(angles, range_values)
plt.title("Range vs Angle of Projection")
plt.xlabel("Launch Angle (degrees)")
plt.ylabel("Range (meters)")
plt.grid(True)
plt.show()
