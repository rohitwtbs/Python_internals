import arcade
import numpy as np
from numba import cuda
import time

# Constants
NUM_PARTICLES = 1000
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

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
        self.particles = arcade.SpriteList()
        self.fps = 0
        self.last_time = time.time()

    def on_update(self, delta_time):
        update_particles[1, NUM_PARTICLES](d_positions, d_velocities, delta_time)
        d_positions.copy_to_host(positions)

        self.particles = arcade.SpriteList()
        for x, y in positions:
            particle = arcade.SpriteCircle(5, arcade.color.AQUA)
            particle.center_x = x
            particle.center_y = y
            self.particles.append(particle)

        # Calculate FPS
        current_time = time.time()
        self.fps = 1 / (current_time - self.last_time)
        self.last_time = current_time

    def on_draw(self):
        self.clear()
        self.particles.draw()

        # Display FPS
        fps_text = f"FPS: {self.fps:.2f}"
        arcade.draw_text(fps_text, 10, SCREEN_HEIGHT - 20, arcade.color.WHITE, 14)

ParticleWindow()
arcade.run()