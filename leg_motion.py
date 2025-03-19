import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read the data
data = pd.read_csv('leg_mocap.csv')
t = data['t'].values
x = data['x'].values
y = data['y'].values

# Calculate velocities using central difference method
def calculate_velocity(t, position):
    """
    Calculate velocity using central difference method.
    First and last points use forward and backward differences respectively.
    """
    vx = np.zeros_like(position)
    
    # Forward difference for first point
    vx[0] = (position[1] - position[0]) / (t[1] - t[0])
    
    # Central difference for middle points
    for i in range(1, len(position) - 1):
        vx[i] = (position[i+1] - position[i-1]) / (t[i+1] - t[i-1])
    
    # Backward difference for last point
    vx[-1] = (position[-1] - position[-2]) / (t[-1] - t[-2])
    
    return vx

plt.figure(figsize=(12, 6))
# Pos x subplot
plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.title('x position')
plt.xlabel('Time')
plt.ylabel('Velocity X')

# Pos y subplot
plt.subplot(2, 1, 2)
plt.plot(t, y)
plt.title('Y position')
plt.xlabel('Time')
plt.ylabel('Velocity Y')
plt.tight_layout()
plt.show()

# Calculate velocities
vx = calculate_velocity(t, x)
vy = calculate_velocity(t, y)

# Create subplots
plt.figure(figsize=(12, 6))

# Velocity x subplot
plt.subplot(2, 1, 1)
plt.plot(t, vx)
plt.title('Velocity in X Direction')
plt.xlabel('Time')
plt.ylabel('Velocity X')

# Velocity y subplot
plt.subplot(2, 1, 2)
plt.plot(t, vy)
plt.title('Velocity in Y Direction')
plt.xlabel('Time')
plt.ylabel('Velocity Y')

plt.tight_layout()
plt.show()

# Optional: Print some basic statistics about velocities
print("Velocity X Statistics:")
print(f"Mean: {np.mean(vx)}")
print(f"Max: {np.max(vx)}")


# The max velocity in the case of y was in the negative direction due to 
# the leg moving downwards in the y direction acording to the axis set in the tracker software
print("\nVelocity Y Statistics:")
print(f"Mean: {np.mean(vy)}")
print(f"Max: {np.min(vy)}")