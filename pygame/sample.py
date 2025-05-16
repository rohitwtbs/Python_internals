import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Dodge Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Player properties
player_size = 50
player_x = screen_width // 2 - player_size // 2
player_y = screen_height - player_size - 10
player_speed = 5

# Obstacle properties
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 3
obstacle_list = []

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()

def draw_player(x, y):
    pygame.draw.rect(screen, green, [x, y, player_size, player_size])

def draw_obstacle(obstacle):
    pygame.draw.rect(screen, red, obstacle)

def generate_obstacle():
    obstacle_x = random.randrange(0, screen_width - obstacle_width)
    obstacle_y = -obstacle_height
    obstacle_list.append(pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height))

def display_score():
    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, [10, 10])

def game_over():
    game_over_text = font.render("Game Over!", True, white)
    screen.blit(game_over_text, [screen_width // 2 - 100, screen_height // 2 - 50])
    pygame.display.flip()
    pygame.time.wait(2000)

# Game start
last_obstacle_time = pygame.time.get_ticks()
obstacle_spawn_interval = 1500 # milliseconds

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Keep player within screen bounds
    if player_x < 0:
        player_x = 0
    elif player_x > screen_width - player_size:
        player_x = screen_width - player_size

    # Spawn new obstacles
    current_time = pygame.time.get_ticks()
    if current_time - last_obstacle_time > obstacle_spawn_interval:
        generate_obstacle()
        last_obstacle_time = current_time

    # Move obstacles
    for obstacle in obstacle_list:
        obstacle.y += obstacle_speed
        if obstacle.bottom > screen_height:
            obstacle_list.remove(obstacle)
            score += 1

    # Collision detection
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    for obstacle in obstacle_list:
        if player_rect.colliderect(obstacle):
            game_over()
            running = False
            break

    # Drawing
    screen.fill(black)
    draw_player(player_x, player_y)
    for obstacle in obstacle_list:
        draw_obstacle(obstacle)
    display_score()
    pygame.display.flip()

    clock.tick(60) # Limit frame rate to 60 FPS

pygame.quit()