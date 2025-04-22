import pygame
import Config
from Player import player
from Weapons import Weapons

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0


mouse_pos = pygame.mouse.get_pos()

font = pygame.font.Font(None, 74)
lose_text = font.render("You Lost!", True, "white")
lose_text_rect = lose_text.get_rect(center=(Config.WIDTH // 2, Config.HEIGHT // 2))

player = player()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")
    sprite_center = player.rect.center
    pygame.draw.aaline(screen, "black", mouse_pos, sprite_center)
    mouse_pos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    if player.health > 0:
        player.Movement(keys)
    player.draw(screen)
    pygame.draw.circle(screen, "blue", mouse_pos, 20)
    pygame.draw.circle(screen, "blue", (500,200), 20)

    if Weapons.Hitscan(sprite_center,sprite_center, mouse_pos, (500,200), 20,):
        print("Hit!")

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()