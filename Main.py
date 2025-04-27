import pygame
import Config
import random
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
player_win = False
player_loss = False

HUD_font = pygame.font.Font(None, 36)
mouse_pos = pygame.mouse.get_pos()
font = pygame.font.Font(None, 74)
lose_text = font.render("You Lost!", True, "white")
win_text = font.render("You Win!", True, "white")
lose_text_rect = lose_text.get_rect(center=(Config.WIDTH // 2, Config.HEIGHT // 2))
player_instance = player()
weapon = Weapons()
background = Background()
heartbar = HeartBar()

Zombies = pygame.sprite.Group()
global_zombie_count = 0
global_zombies_spawned = 0
global_kill_count = 0
global_round_count = 1

pygame.time.set_timer(Config.ZOMBIE_SPAWN_EVENT, 1000)
pygame.time.set_timer(Config.MEDKIT_SPAWN_EVENT, 5000)

medkit = Medkit()
medkits = pygame.sprite.Group()
medkits.add(medkit)
global_medkit_count = 1

def start_game():
    global running, dt, show_FPS, player_win, player_loss, HUD_font, mouse_pos, font, lose_text, win_text, lose_text_rect
    global player_instance, weapon, background, heartbar, Zombies, global_zombie_count, global_zombies_spawned, global_kill_count, global_round_count, medkits, global_medkit_count

    while running:
        mouse_pos = pygame.mouse.get_pos()
        handle_events(player_instance, weapon, Zombies, medkits, heartbar)
        update_game_state(player_instance, Zombies, medkits, heartbar)
        draw_game(screen, background, player_instance, weapon, heartbar, medkits, Zombies, HUD_font, font, lose_text_rect, show_FPS, clock, global_round_count, global_kill_count, player_win, player_loss)
        dt = clock.tick(60) / 1000

    pygame.quit()

def handle_events(player_instance, weapon, Zombies, medkits):
    global global_medkit_count, running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                weapon.fire()
                hitscan(player_instance.rect.center, pygame.mouse.get_pos(), weapon, Zombies)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                weapon.reload(pygame.time.get_ticks())
            debug.forcespawn(event, medkits, Zombies)
        elif event.type == Config.MEDKIT_SPAWN_EVENT:
            if global_medkit_count <= 0 and playercond():
                spawn_medkit(medkits)
        elif event.type == Config.ZOMBIE_SPAWN_EVENT:
            roundcheck(Zombies)

def spawn_medkit(medkits):
    global global_medkit_count
    medkit_instance = Medkit()
    medkits.add(medkit_instance)
    global_medkit_count += 1

def spawn_zombie(Zombies):
    global global_zombie_count, global_zombies_spawned
    zombie_iframes = random.randint(250, 500)
    zombie_instance = zombie(zombie_iframes)
    Zombies.add(zombie_instance)
    global_zombie_count += 1
    global_zombies_spawned += 1

def hitscan(line_start, line_end, weapon, Zombies):
    global global_zombie_count, global_kill_count
    for zombie_instance in Zombies:
        if weapon.Hitscan(line_start, line_end, zombie_instance.rect.center, zombie_instance.rect.width // 3):
            if not weapon.noammo:
                zombie_instance.health -= weapon.dmg
                if zombie_instance.health <= 0:
                    zombie_instance.kill()
                    global_zombie_count -= 1
                    global_kill_count += 1

def roundcheck(Zombies):
    global player_win, global_round_count
    if global_zombies_spawned < Config.ZOMBIE_HORDE_NUM * global_round_count + global_round_count:
        spawn_zombie(Zombies)
    if global_kill_count == global_round_count * Config.ZOMBIE_HORDE_NUM + global_round_count:
        global_round_count += 1
    if global_round_count > 5:
        player_win = True

def playercond():
    global player_loss, player_win
    return not player_loss and not player_win

def update_game_state(player_instance, Zombies, medkits, heartbar):
    global global_medkit_count, player_loss
    keys = pygame.key.get_pressed()
    if player_instance.health > 0:
        player_instance.Movement(keys)
        player_instance.followcursor(pygame.mouse.get_pos())
    else:
        player_loss = True
    for medkit in medkits:
        medkit.collision(player_instance)
        if not medkit.alive():
            global_medkit_count -= 1
            heartbar.update_health(player_instance.health)
    for zombie_instance in Zombies:
        if playercond():
            zombie_instance.move_towards_player(player_instance)
            zombie_instance.turn_towards_player(player_instance)
        if player_instance.rect.colliderect(zombie_instance.rect):
            player_instance.Lose_health(Config.ZOMBIE_DAMAGE, pygame.time.get_ticks(), zombie_instance.IFrames)
            heartbar.update_health(player_instance.health)

def draw_game(screen, background, player_instance, weapon, heartbar, medkits, Zombies, HUD_font, font, lose_text_rect, show_FPS, clock, global_round_count, global_kill_count, player_win, player_loss):
    screen.fill("purple")
    background.draw_pattern(screen)
    player_instance.draw(screen)
    weapon.draw(screen, player_instance.rect.topright)
    pygame.draw.aaline(screen, "black", pygame.mouse.get_pos(), player_instance.rect.center)
    pygame.draw.circle(screen, "blue", pygame.mouse.get_pos(), 20)
    heartbar.draw(screen)
    medkits.draw(screen)
    Zombies.draw(screen)
    if show_FPS:
        fps = clock.get_fps()
        fps_text = HUD_font.render(f"FPS: {int(fps)}", True, "white")
        screen.blit(fps_text, (10, 10))
    ammo_counter = HUD_font.render(f"Ammo: {int(Config.WEAPONAMMO['shotgun'])}", True, "white")
    round_counter = HUD_font.render(f"Round: {int(global_round_count)}", True, "white")
    kill_counter = HUD_font.render(f"Kills: {int(global_kill_count)}", True, "white")
    screen.blit(kill_counter, (Config.WIDTH - 125, Config.HEIGHT - 100))
    screen.blit(round_counter, (Config.WIDTH - 125, Config.HEIGHT - 75))
    screen.blit(ammo_counter, (Config.WIDTH - 125, Config.HEIGHT - 50))
    if player_win:
        screen.blit(win_text, lose_text_rect)
    elif player_loss:
        screen.blit(lose_text, lose_text_rect)
    debug.stats(screen, HUD_font, global_zombies_spawned, global_zombie_count)
    pygame.display.flip()

class debug:
    def forcespawn(event, medkits, Zombies):
        if Config.DEBUG:
            if event.key == pygame.K_m:
                spawn_medkit(medkits)
            elif event.key == pygame.K_z:
                spawn_zombie(Zombies)

    def stats(screen, HUD_font, global_zombies_spawned, global_zombie_count):
        if Config.DEBUG:
            zombiesspawned = HUD_font.render(f"spawned: {int(global_zombies_spawned)}", True, "white")
            screen.blit(zombiesspawned, (Config.WIDTH - 200, Config.HEIGHT - 125))
            zombiesalive = HUD_font.render(f"zombies: {int(global_zombie_count)}", True, "white")
            screen.blit(zombiesalive, (Config.WIDTH - 200, Config.HEIGHT - 150))
