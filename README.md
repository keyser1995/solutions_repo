# Orbital Period and Orbital Radius

## 1.Motivation:
Kepler's Third Law is a fundamental principle in celestial mechanics that describes the relationship between a planet's orbital period and its orbital radius. Specifically, the law states that the square of the orbital period (T 2) is directly proportional to the cube of the orbital radius (r 3 ):

<img width="108" alt="image" src="https://github.com/user-attachments/assets/8bcbad6c-d0c5-4b05-bde3-72abcace16fe" />

This law forms the basis for understanding the gravitational interactions between celestial bodies, such as planetary systems, moons, and satellites. By analyzing this relationship, we can predict the motion of objects in orbit and determine the properties of the central body (e.g., a star or planet).

### Kepler's Third Law:
For circular orbits, Kepler's Third Law can be derived by considering the gravitational force that acts as the centripetal force keeping an object in orbit.

The force of gravity between two objects is given by Newton's Law of Universal Gravitation: 

<img width="122" alt="image" src="https://github.com/user-attachments/assets/eb0a8868-d068-4f30-99ea-52cc300907d3" />

where:

G is the gravitational constant,
M is the mass of the central body (e.g., the Sun or Earth),
m is the mass of the orbiting object (e.g., a planet or satellite),
r is the orbital radius.

For an object moving in a circular orbit, the centripetal force required to keep the object in orbit is:

<img width="116" alt="image" src="https://github.com/user-attachments/assets/ed381866-032f-408a-a111-2004684c28fe" />

where 𝑣v is the orbital velocity.

<img width="104" alt="image" src="https://github.com/user-attachments/assets/e2b38830-d40a-483f-b6d5-9885d35fb5d8" />

Solving for 𝑣, we get:

<img width="92" alt="image" src="https://github.com/user-attachments/assets/529f2585-8751-4599-ae42-05cb1fee2ef1" />

The orbital period 𝑇 is the time it takes for the object to complete one full revolution around the central body. The distance traveled in one orbit is the circumference of the circle:

<img width="153" alt="image" src="https://github.com/user-attachments/assets/ee05ed06-dc9f-4704-9ffe-2e48faad1086" />

Therefore, the orbital period is given by:

<img width="205" alt="image" src="https://github.com/user-attachments/assets/fb9a1383-c9b9-4e8b-9cb1-323063963749" />

Simplifying this expression:

<img width="104" alt="image" src="https://github.com/user-attachments/assets/f7dbe28d-f5ca-43f4-964f-83dc9fb8a184" />

This shows the relationship between the orbital period 𝑇 and the orbital radius 𝑟. Squaring both sides:

<img width="79" alt="image" src="https://github.com/user-attachments/assets/85ec1b95-ea7c-45ae-81c4-bf60dcdcfeea" />

This is Kepler's Third Law in its most familiar form. The square of the orbital period is proportional to the cube of the orbital radius.

### Implications for Astronomy:

1. Calculating Planetary Masses: By measuring the orbital period and radius of an object, we can calculate the mass of the central body. For example, by observing a satellite's orbit around a planet or a planet's orbit around a star, we can compute the mass of the planet or star.

2. Determining Orbital Properties: Kepler's Third Law helps us determine the properties of an object’s orbit (e.g., the time it takes to orbit a planet or the distance from the central body) based on the mass of the central body and the orbital radius.

3. Planetary Systems: In our Solar System, planets and moons follow Kepler's Third Law, allowing us to predict their movements and understand the dynamics of planetary systems.

### Real-World Example: Moon's Orbit Around Earth:

For the Moon's orbit around Earth:

Orbital radius 𝑟 ≈ 384,400 km 
Orbital period 𝑇 ≈ 27.3 days

We can use Kepler’s Third Law to verify this relationship and calculate the mass of Earth from the orbital period and radius of the Moon.

## Computational Model: Simulating Circular Orbits:

To simulate circular orbits and verify Kepler's Third Law, we can implement a simple Python model. Below is the Python script that models circular orbits and verifies the relationship between the orbital period and the orbital radius.

```

import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
M = 5.972e24     # Mass of Earth (kg)
pi = np.pi

# Function to calculate orbital period for a given radius
def orbital_period(radius):
    return 2 * pi * np.sqrt(radius**3 / (G * M))

# Define a range of orbital radii (in meters)
radii = np.linspace(1e7, 1e9, 100)  # from 10^7 m to 10^9 m

# Calculate corresponding orbital periods
periods = orbital_period(radii)

# Plot the relationship between orbital period squared (T^2) and orbital radius cubed (r^3)
plt.figure(figsize=(8, 6))
plt.plot(radii**3, periods**2, label="T^2 vs r^3", color='blue')
plt.xlabel("Orbital Radius Cubed (r^3) [m^3]")
plt.ylabel("Orbital Period Squared (T^2) [s^2]")
plt.title("Kepler's Third Law: T^2 vs r^3")
plt.grid(True)
plt.legend()
plt.show()


```

### Description of the Script:
Gravitational Constant (G): The gravitational constant is used in the calculation of the orbital period.

Mass of Earth (M): The mass of the central body (Earth in this case) is used in the calculation.

Orbital Period Function: The function orbital_period(radius) computes the orbital period using the formula derived above.

Plot: A plot of \(T^{2}\) versus \(r^{3}\) is generated to visualize Kepler's Third Law.

### Graphical Representations:

The plot generated by the script will show a linear relationship between the square of the orbital period and the cube of the orbital radius, consistent with Kepler’s Third Law.

### Extending to Elliptical Orbits and Other Celestial Bodies:

Kepler's Third Law can also be applied to elliptical orbits, where the semi-major axis of the ellipse takes the place of the orbital radius in the formula. The general form of Kepler's Third Law for elliptical orbits is:

<img width="70" alt="image" src="https://github.com/user-attachments/assets/f53caca5-6e10-4fb5-bcbd-92ccb499e1d7" />

where 𝑎 is the semi-major axis of the ellipse.

This law holds not just for planets but also for moons, satellites, and artificial objects in orbit, and can be applied to various celestial bodies like comets, asteroids, and stars in binary systems.


## Deliverables:

1. Markdown document with explanations and the simulation code.

2. Python script or notebook for simulating circular orbits.

3. Graphical representation of the relationship between orbital period and radius.

4. Discussion on the implications for elliptical orbits and other celestial bodies.
