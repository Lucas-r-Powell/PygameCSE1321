import pygame
import Config
from player import player
from Weapons import Weapons
from Medkit import Medkit
from HeartBar import HeartBar

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_instance = player()
heart_bar = HeartBar(5, 10, player_instance)

respawn_timer = 120
last_respawn_time = pygame.time.get_ticks()

medkit = Medkit()
medkits = pygame.sprite.Group()
medkits.add(medkit)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = pygame.time.get_ticks()
    if current_time - last_respawn_time >= respawn_timer * 1000 and len(medkits) == 0:
        medkit = Medkit()
        medkits.add(medkit)
        last_respawn_time = current_time

    screen.fill("purple")
    sprite_center = player_instance.rect.center
    pygame.draw.aaline(screen, "black", pygame.mouse.get_pos(), sprite_center)

    keys = pygame.key.get_pressed()
    if player_instance.health > 0:
        player_instance.Movement(keys)
    player_instance.draw(screen)
    heart_bar.draw(screen)

    medkits.update()
    medkits.draw(screen)

    for medkit in medkits:
        medkit.collision(heart_bar)

    pygame.display.flip()
    dt = clock.tick(60) / 1000


pygame.quit()

