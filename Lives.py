import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Lives Counter Example")

# Clock
clock = pygame.time.Clock()

# Game variables
total_lives = 100
player_pos = pygame.Vector2(screen_width / 2, screen_height / 2)
player_color = (255, 0, 0)
player_radius = 40

# Fonts
font = pygame.font.SysFont(None, 40)
game_over_font = pygame.font.SysFont(None, 80)

# Functions
def draw_lives_counter(surface, lives):
    text = font.render(f"Lives: {lives}", True, (255, 0, 0))
    surface.blit(text, (30, 30))

def game_over():
    text = game_over_font.render("GAME OVER", True, (255, 0, 0))
    screen.fill((0, 0, 0))
    screen.blit(text, (screen_width // 2 - 200, screen_height // 2 - 40))
    pygame.display.update()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

# Main loop
running = True
while running:
    dt = clock.tick(60) / 1000  # Frame time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # Simulate taking damage when pressing space
    if keys[pygame.K_SPACE]:
        total_lives -= 1
        pygame.time.wait(200)  # prevent holding down key
        if total_lives <= 0:
            game_over()

    # Draw everything
    screen.fill("black")
    pygame.draw.circle(screen, player_color, player_pos, player_radius)
    draw_lives_counter(screen, total_lives)
    pygame.display.flip()

pygame.quit()
