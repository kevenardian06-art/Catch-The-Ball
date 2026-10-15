"""
Simple Pygame Example: "Catch the Falling Box"
-----------------------------------------------------
The player moves a green box at the bottom to catch a
yellow box falling from the top. Each catch = +1 score.
If the yellow box falls to the bottom without being caught = game over.

How to run:
1. pip install pygame
2. python main.py
"""

import pygame
import random

# ---------- 1. INITIALIZATION ----------
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Box")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 100)
YELLOW = (255, 210, 0)
BACKGROUND = (20, 255, 255)
RED = (255, 60, 60)

# ---------- 2. GAME VARIABLES ----------
player_width = 80
player_height = 20
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 50
player_speed = 8

box_size = 30
box_x = random.randint(0, WIDTH - box_size)
box_y = 0
box_speed = 5

score = 0
game_over = False


# ---------- 3. DRAW TEXT ----------
def draw_text(text, font_size, color, pos):
    f = pygame.font.SysFont(None, font_size)
    render = f.render(text, True, color)
    rect = render.get_rect(center=pos)
    screen.blit(render, rect)


# ---------- 4. GAME LOOP ----------
running = True

while running:

    # --- Check events ---
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and game_over:

            if event.key == pygame.K_r:
                # Restart the game
                score = 0
                box_y = 0
                box_x = random.randint(0, WIDTH - box_size)
                box_speed = 5
                game_over = False

    # --- Game updates ---
    if not game_over:

        # Update player position
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed

        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
            player_x += player_speed

        # Update falling box
        box_y += box_speed

        # Create rectangles for collision detection
        player_box = pygame.Rect(
            player_x,
            player_y,
            player_width,
            player_height
        )

        falling_box = pygame.Rect(
            box_x,
            box_y,
            box_size,
            box_size
        )

        # Check collision
        if player_box.colliderect(falling_box):
            score += 1

            # Reset falling box
            box_y = 0
            box_x = random.randint(0, WIDTH - box_size)

            # Increase speed every 5 points
            box_speed = min(15, 5 + score // 5)

        # Check if box reaches the bottom
        if box_y > HEIGHT:
            game_over = True

    # ---------- 5. DRAW SCREEN ----------
    screen.fill(BACKGROUND)

    if not game_over:

        # Draw player
        pygame.draw.rect(
            screen,
            GREEN,
            (player_x, player_y, player_width, player_height)
        )

        # Draw falling box
        pygame.draw.rect(
            screen,
            YELLOW,
            (box_x, box_y, box_size, box_size)
        )

        # Draw score
        draw_text(
            f"Score: {score}",
            36,
            WHITE,
            (80, 30)
        )

    else:

        # Game over screen
        draw_text(
            "GAME OVER",
            64,
            RED,
            (WIDTH // 2, HEIGHT // 2 - 40)
        )

        draw_text(
            f"Final score: {score}",
            40,
            WHITE,
            (WIDTH // 2, HEIGHT // 2 + 20)
        )

        draw_text(
            "Press R to play again",
            28,
            WHITE,
            (WIDTH // 2, HEIGHT // 2 + 70)
        )

    # Update display
    pygame.display.flip()

    # Limit game to 60 FPS
    clock.tick(60)


# Quit pygame
pygame.quit()