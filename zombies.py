import pygame
import Config
class zombie:
     def __init__(self):
         self.health = Config.ZOMBIE_HEALTH
         self.speed = Config.ZOMBIE_SPEED
         self.sprite = pygame.image.load(Config.ZOMBIE_IMAGE_PATH).convert_alpha()
         self.rect = self.sprite.get_rect(center=(Config.WIDTH - 20, Config.HEIGHT - 20))
         self.deadSound = pygame.mixer.Sound(Config.ZOMBIE_DEATH_SOUND_PATH)