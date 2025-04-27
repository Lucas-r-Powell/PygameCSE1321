import pygame
import Config
import random

class zombie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = Config.ZOMBIE_HEALTH
        self.speed = Config.ZOMBIE_SPEED
        self.image = pygame.image.load(Config.ZOMBIE_IMAGE_PATH).convert_alpha()
        self.rect = self.image.get_rect(center=self.spawn_off_screen())
        self.deadSound = pygame.mixer.Sound(Config.ZOMBIE_DEATH_SOUND_PATH)

    def spawn_off_screen(self):
        side = random.choice(['top', 'bottom', 'left', 'right'])
        if side == 'top':
            return (random.randint(0, Config.WIDTH), -50)
        elif side == 'bottom':
            return (random.randint(0, Config.WIDTH), Config.HEIGHT + 50)
        elif side == 'left':
            return (-50, random.randint(0, Config.HEIGHT))
        elif side == 'right':
            return (Config.WIDTH + 50, random.randint(0, Config.HEIGHT))

    def move_towards_player(self, player):
        dx, dy = player.rect.centerx - self.rect.centerx, player.rect.centery - self.rect.centery
        distance = (dx**2 + dy**2)**0.5
        if distance != 0:
            dx, dy = dx / distance, dy / distance
        self.rect.move_ip(dx * self.speed, dy * self.speed)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

