import pygame
import Config
from Player import player
from Weapons import Weapons
from Background import background

pygame.init()
screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0
show_FPS = True
HUD_font = pygame.font.Font(None, 36)

mouse_pos = pygame.mouse.get_pos()

font = pygame.font.Font(None, 74)
lose_text = font.render("You Lost!", True, "white")
lose_text_rect = lose_text.get_rect(center=(Config.WIDTH // 2, Config.HEIGHT // 2))

player = player()
weapon = Weapons()
background = background()
Zombies = []

pygame.time.set_timer(Config.ZOMBIE_SPAWN_EVENT, 1000)

#====MAIN LOOP====
while running:
    time = pygame.time.get_ticks()
    mouse_pos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    sprite = player.rect
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                weapon.fire()
                if Weapons.Hitscan(sprite.center, sprite.center, mouse_pos, (500, 200), 20, ):
                    print("Hit!")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                weapon.reload(time)

    screen.fill("purple")
    background.draw_pattern(screen)



    player.draw(screen)
    weapon.draw(screen,sprite.topright)
    pygame.draw.aaline(screen, "black", mouse_pos, sprite.center)
    pygame.draw.circle(screen, "blue", mouse_pos, 20)
    pygame.draw.circle(screen, "blue", (500,200), 20)
    if player.health > 0:
        player.Movement(keys)

    #===Hud elements===
    if show_FPS == True:
        fps = clock.get_fps()
        fps_text = HUD_font.render(f"FPS: {int(fps)}", True, "white")
        screen.blit(fps_text, (10, 10))
        ammo_counter = HUD_font.render(f"Ammo:{int(Config.WEAPONAMMO["shotgun"])}", True,"White")
        screen.blit(ammo_counter, (Config.WIDTH - 125,Config.HEIGHT-50))
    #==================

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()