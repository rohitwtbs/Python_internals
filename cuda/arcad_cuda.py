import arcade
import numpy as np
from numba import cuda

# Constants
NUM_PARTICLES = 100
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Allocate host arrays
positions = np.random.rand(NUM_PARTICLES, 2).astype(np.float32) * SCREEN_WIDTH
velocities = (np.random.rand(NUM_PARTICLES, 2).astype(np.float32) - 0.5) * 10

# Allocate device arrays
d_positions = cuda.to_device(positions)
d_velocities = cuda.to_device(velocities)

# CUDA kernel to update particles
@cuda.jit
def update_particles(positions, velocities, dt):
    i = cuda.threadIdx.x
    if i < positions.shape[0]:
        positions[i, 0] += velocities[i, 0] * dt
        positions[i, 1] += velocities[i, 1] * dt

        # Bounce on edges
        if positions[i, 0] < 0 or positions[i, 0] > SCREEN_WIDTH:
            velocities[i, 0] *= -1
        if positions[i, 1] < 0 or positions[i, 1] > SCREEN_HEIGHT:
            velocities[i, 1] *= -1

# Arcade window
class ParticleWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "GPU Particles with Numba")
        self.particles = arcade.ShapeElementList()

    def on_update(self, delta_time):
        update_particles[1, NUM_PARTICLES](d_positions, d_velocities, delta_time)
        d_positions.copy_to_host(positions)

        self.particles = arcade.ShapeElementList()
        for x, y in positions:
            self.particles.append(arcade.create_ellipse_filled(x, y, 5, 5, arcade.color.AQUA))

    def on_draw(self):
        self.clear()
        self.particles.draw()

ParticleWindow()
arcade.run()
