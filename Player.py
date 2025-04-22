import pygame
import Config
import math


class player:
    def __init__(self):
        self.speed = Config.PLAYER_SPEED
        self.sprite = pygame.image.load(Config.PLAYER_IMAGE_PATH)
        self.rect = self.sprite.get_rect(center=(Config.WIDTH // 2, Config.HEIGHT - 65))
        self.health = Config.PLAYER_HEALTH
        self.deadSound = pygame.mixer.Sound(Config.PLAYER_DEATH_SOUND_PATH)
    def Movement(self, keys):
        dx, dy = 0, 0
        #fixed stafing being faster than normal movement
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

    def draw(self, surface):
        surface.blit(self.sprite, self.rect)