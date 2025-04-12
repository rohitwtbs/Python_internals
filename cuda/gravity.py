import numpy as np
from numba import cuda

# Constants
NUM_PARTICLES = 10000
GRAVITY = -9.8
TIME_STEP = 0.01

# Initialize particle positions and velocities
positions = np.random.rand(NUM_PARTICLES, 2).astype(np.float32) * 100
velocities = np.random.rand(NUM_PARTICLES, 2).astype(np.float32) * 10

# Allocate device arrays
d_positions = cuda.to_device(positions)
d_velocities = cuda.to_device(velocities)

# CUDA kernel for particle simulation
@cuda.jit
def simulate_particles(positions, velocities, dt):
    i = cuda.grid(1)
    if i < positions.shape[0]:
        # Update velocity with gravity
        velocities[i, 1] += GRAVITY * dt

        # Update position
        positions[i, 0] += velocities[i, 0] * dt
        positions[i, 1] += velocities[i, 1] * dt

        # Bounce on ground
        if positions[i, 1] < 0:
            positions[i, 1] = 0
            velocities[i, 1] *= -0.8  # Dampen velocity on bounce

# Define thread and block dimensions
threads_per_block = 256
blocks_per_grid = (NUM_PARTICLES + threads_per_block - 1) // threads_per_block

# Run simulation for 100 steps
for _ in range(100):
    simulate_particles[blocks_per_grid, threads_per_block](d_positions, d_velocities, TIME_STEP)

# Copy result back to host
positions = d_positions.copy_to_host()

print("Particle simulation completed!")