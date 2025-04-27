import pygame
import Config
import math
from HeartBar import HeartBar
heartbar = HeartBar()

class player:
    def __init__(self):
        self.speed = Config.PLAYER_SPEED
        self.sprite = pygame.image.load(Config.PLAYER_IMAGE_PATH).convert_alpha()
        self.initalsprite = pygame.transform.scale(pygame.image.load(Config.PLAYER_IMAGE_PATH).convert_alpha(), (100,100))
        self.sprite = pygame.transform.scale(self.sprite, (100,100))
        self.rect = self.sprite.get_rect(center=(Config.WIDTH // 2, Config.HEIGHT // 2 ))
        self.health = Config.PLAYER_HEALTH
        self.deadSound = pygame.mixer.Sound(Config.PLAYER_DEATH_SOUND_PATH)
        self.IFrames = Config.IFRAMES
        self.last_damage_time = Config.LASTDAMAGE

    def Movement(self, keys):
        dx, dy = 0, 0
        if keys[pygame.K_a] and self.rect.left > 0:
            dx = -self.speed
        if keys[pygame.K_d] and self.rect.right < Config.WIDTH:
            dx = self.speed
        if keys[pygame.K_w] and self.rect.top > 0:
            dy = -self.speed
        if keys[pygame.K_s] and self.rect.bottom < Config.HEIGHT:
            dy = self.speed
        if dx != 0 and dy != 0:
            dx /= math.sqrt(2)
            dy /= math.sqrt(2)
        self.rect.move_ip(dx, dy)
    
    def Lose_health(self,damage,time, zombie_iframes):
        if time - self.last_damage_time > zombie_iframes:
            self.health -= damage
            self.last_damage_time = time
        if self.health < 0:
            self.health = 0

    def Gain_health(self,heal):
        self.health = min(self.health + heal, 10)
        heartbar.update_health(self.health)
        print(f"player hp {self.health}")

    def followcursor(self, mousepos):
        dx, dy = mousepos[0] - self.rect.centerx, mousepos[1] - self.rect.centery
        angle = math.degrees(math.atan2(-dy, dx))
        self.sprite = pygame.transform.rotate(self.initalsprite, angle - 90)
        self.rect = self.sprite.get_rect(center=self.rect.center)

    def draw(self, surface):
        surface.blit(self.sprite, self.rect)