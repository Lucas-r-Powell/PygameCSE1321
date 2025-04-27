import pygame
import Config
import random
import math

class zombie(pygame.sprite.Sprite):
    def __init__(self, iframes):
        super().__init__()
        self.health = Config.ZOMBIE_HEALTH
        self.speed = Config.ZOMBIE_SPEED
        self.image = pygame.transform.scale(pygame.image.load(Config.ZOMBIE_IMAGE_PATH).convert_alpha(), (125,125))
        self.initalsprite = self.image.copy()
        self.rect = self.image.get_rect(center=self.spawn_off_screen())
        self.deadSound = pygame.mixer.Sound(Config.ZOMBIE_DEATH_SOUND_PATH)
        self.IFrames = iframes
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
    
    def turn_towards_player(self,player):
        dx, dy = player.rect.centerx - self.rect.centerx, player.rect.centery - self.rect.centery 
        angle = math.degrees(math.atan2(dy, dx))
        self.image = pygame.transform.rotate(self.initalsprite, -angle - 90)
        self.rect = self.image.get_rect(center=self.rect.center)


    def draw(self, surface):
        surface.blit(self.image, self.rect)

