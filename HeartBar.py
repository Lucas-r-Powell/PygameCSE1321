import pygame
from Config import PLAYER_HEALTH, WIDTH, HEARTBAR

class HeartBar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.health = PLAYER_HEALTH

        self.x = WIDTH - 410
        self.y = -10
        scale = (400, 200)
        self.Hearts = pygame.transform.scale(pygame.image.load(HEARTBAR[self.health]), scale)
        self.image = self.Hearts
    def update_health(self, new_health):
        scale = (400, 200)
        self.health = min(new_health, 10)
        self.image = pygame.transform.scale(pygame.image.load(HEARTBAR[self.health]), scale)

    def draw(self, surface):
        surface.blit(self.image,(self.x,self.y))
