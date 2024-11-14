# Given data
v_i_kmh = 310  # Initial velocity in km/h
d = 1000       # Distance in meters
v_f = 0        # Final velocity (jet stops)

# Convert initial velocity from km/h to m/s
v_i = v_i_kmh * 1000 / 3600

# Use the kinematic equation: v_f^2 = v_i^2 + 2 * a * d
# Rearranging for acceleration a: a = (v_f^2 - v_i^2) / (2 * d)
a = (v_f**2 - v_i**2) / (2 * d)

# Print the result
print(f"Required acceleration: {a:.2f} m/s^2")


