import pygame
import Config
from Player import player
from Weapons import Weapons
from Background import Background
from HeartBar import HeartBar
from Medkit import Medkit
from zombies import zombie

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
background = Background()
heartbar = HeartBar()

Zombies = pygame.sprite.Group()
global_zombie_count = 0

pygame.time.set_timer(Config.ZOMBIE_SPAWN_EVENT, 1000)
pygame.time.set_timer(Config.MEDKIT_SPAWN_EVENT, 5000)

medkit = Medkit()
medkits = pygame.sprite.Group()
medkits.add(medkit)
global_medkit_count = 1

blue_circle_pos = (500, 200)
blue_circle_radius = 20
blue_circle_damage = 1

class debug:
    def forcespawnmedkit(event):
        global global_medkit_count
        global global_zombie_count
        if Config.DEBUG:
            if event.key == pygame.K_m:
                spawn_medkit()
            elif event.key == pygame.K_z:
                spawn_zombie()

def handle_events():
    global global_medkit_count
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                weapon.fire()
                if Weapons.Hitscan(player.rect.center, player.rect.center, mouse_pos, blue_circle_pos, zombie.rect) and weapon.ammo["shotgun"] > 0:
                    print("Hit!")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                weapon.reload(pygame.time.get_ticks())
            debug.forcespawnmedkit(event)
        elif event.type == Config.MEDKIT_SPAWN_EVENT:
            if global_medkit_count <= 0:
                spawn_medkit()
        elif event.type == Config.ZOMBIE_SPAWN_EVENT:
            if global_zombie_count <= Config.ZOMBIE_HORDE_NUM:
                spawn_zombie()

def spawn_medkit():
    global global_medkit_count
    medkit_instance = Medkit()
    medkits.add(medkit_instance)
    global_medkit_count += 1
    print("Medkit spawned!")

def spawn_zombie():
    global global_zombie_count
    zombie_instance = zombie()
    Zombies.add(zombie_instance)
    global_zombie_count += 1
    print("zombie spawned!")


def update_game_state():
    global global_medkit_count
    keys = pygame.key.get_pressed()
    if player.health > 0:
        player.Movement(keys)
    for medkit in medkits:
        medkit.collision(player)
        if not medkit.alive():
            global_medkit_count -= 1
            heartbar.update_health(player.health)
            print(f"Medkit spawned! Total medkits: {global_medkit_count}")
    for zombie_instance in Zombies:
        zombie_instance.move_towards_player(player)
    if player.rect.colliderect(pygame.Rect(blue_circle_pos[0] - blue_circle_radius, blue_circle_pos[1] - blue_circle_radius, blue_circle_radius * 2, blue_circle_radius * 2)):
        player.Lose_health(blue_circle_damage, pygame.time.get_ticks())
        heartbar.update_health(player.health)
        print(f"Player hit by blue circle! Health: {player.health}")

def draw_game():
    screen.fill("purple")
    background.draw_pattern(screen)
    player.draw(screen)
    weapon.draw(screen, player.rect.topright)
    pygame.draw.aaline(screen, "black", mouse_pos, player.rect.center)
    pygame.draw.circle(screen, "blue", mouse_pos, 20)
    pygame.draw.circle(screen, "blue", (500, 200), 20)
    heartbar.draw(screen)
    medkits.draw(screen)
    Zombies.draw(screen)
    if show_FPS:
        fps = clock.get_fps()
        fps_text = HUD_font.render(f"FPS: {int(fps)}", True, "white")
        screen.blit(fps_text, (10, 10))
    ammo_counter = HUD_font.render(f"Ammo: {int(Config.WEAPONAMMO['shotgun'])}", True, "white")
    screen.blit(ammo_counter, (Config.WIDTH - 125, Config.HEIGHT - 50))
    pygame.display.flip()

while running:
    mouse_pos = pygame.mouse.get_pos()
    handle_events()
    update_game_state()
    draw_game()
    dt = clock.tick(60) / 1000

pygame.quit()
