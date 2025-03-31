# Investigating the Range as a Function of the Angle of Projection

## 1. Theoretical Foundation:
To derive the equations governing projectile motion, we start from basic principles. We assume that the projectile is launched from the ground (height  y0 = 0), and we ignore air resistance for simplicity.

### Governing Equations of Motion:

**Horizontal motion**: There is no acceleration in the horizontal direction, so the velocity remains constant. The equation for horizontal motion is:

<img width="156" alt="image" src="https://github.com/user-attachments/assets/77d246b5-cebd-4aeb-b853-d8c23d55c77d" />

Where:

- x\(t\) is the horizontal distance traveled at time t,
- v 
0 is the initial velocity,
- θ is the launch angle,
- t is the time.

**Vertical motion**: The vertical motion is influenced by gravity, which gives us the equation:

<img width="184" alt="image" src="https://github.com/user-attachments/assets/4c873ab9-22b1-4531-b764-1fbac661f581" />


Where:

- y(t) is the vertical displacement at time t,
- g is the acceleration due to gravity  (
≈
9.81
 
𝑚
/
𝑠
2
≈9.81m/s 
2
 )..

### Time of Flight:
To find the time the projectile remains in the air (i.e., time of flight), we set \( y(t) = 0 \) (when the projectile hits the ground):

<img width="159" alt="image" src="https://github.com/user-attachments/assets/8ba13a1c-372e-4949-be83-b9d4ae752675" />


This simplifies to:

<img width="102" alt="image" src="https://github.com/user-attachments/assets/3ebacf8e-70d9-41ba-947b-3d4d3c892a35" />


### Range of the Projectile:
The range \( R \) is the horizontal distance the projectile travels when it hits the ground. To find this, we substitute the time of flight \( t \) into the horizontal motion equation:

<img width="345" alt="image" src="https://github.com/user-attachments/assets/051e7a7f-5922-4e2e-b1ba-4d051ae8e602" />


This is the range formula of the projectile.

## 2. Analysis of the Range:

Now we investigate how the range depends on the launch angle θ.

### Range vs. Angle of Projection:
The range R is maximized when sin(2θ) is maximized, which occurs when 2θ=90∘ , or 𝜃=45∘. This means that, for a given initial velocity, the range is maximized at a launch angle of 45 degrees.

### Effect of Initial Velocity:
If the initial velocity \( v_0 \) increases, the range increases quadratically. This means that doubling the initial velocity will quadruple the range.

### Effect of Gravitational Acceleration:
If g increases (for example, on a planet with stronger gravity), the range decreases. Conversely, if g decreases (on a planet with weaker gravity), the range increases.

## 3. Practical Applications:
This model can be adapted for more complex real-world scenarios by including factors like:

- **Uneven terrain**: If the projectile is launched from or lands on a raised platform, the equation for y(t) would be modified to account for the initial height.
  
- **Air resistance**: For more realistic simulations, we would need to incorporate drag into the equations of motion. This would make the equations more complex and likely require numerical methods to solve.

- **Sports, engineering, and astrophysics**: The model applies to a wide range of fields. In sports, it can describe the trajectory of balls (like soccer or basketball). In engineering, it can be used for the design of launch systems. In astrophysics, it helps understand the motion of celestial objects.

## 4. Python Implementation
```
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
```

## 5. Limitations of the Idealized Model:
   
- **Air resistance:** Our model ignores air resistance, which affects the projectile’s range, especially at higher speeds or for objects with large surface areas. To include air resistance, we would need to solve a more complex system of differential equations, possibly requiring numerical methods (e.g., Euler’s method or Runge-Kutta).

- **Wind: Wind** can alter the trajectory of the projectile. This would require additional modeling of the wind’s velocity and direction.

- **Uneven terrain:** As mentioned earlier, launching from or landing on uneven terrain complicates the equations.

## Conclusion:  
By following these steps, we derived the equations for projectile motion, explored how the range depends on the angle of projection, and simulated the range for different angles. The idealized model is a good starting point, but real-world factors like air resistance and terrain need to be considered for more accurate predictions.




