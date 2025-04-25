import pygame
from player import player

class HeartBar(pygame.sprite.Sprite):
    def __init__(self,x, y, player_instance):
        super().__init__()
        self.load_animations()
        self.player_instance = player_instance
        self.image = self.Hearts[10]
        self.x = x
        self.y = y

    def Lose_health(self,damage):
        self.player_instance.health-= damage
        if self.player_instance.health < 0:
            self.player_instance.health = 0

    def Gain_health(self,heal):
        self.player_instance.health+= heal
        if self.player_instance.health > 10:
            self.player_instance.health = 10

    def load_animations(self):
        scale = (400, 200)  # Change this to the size you want (width, height)
        self.Hearts = [
            pygame.transform.scale(pygame.image.load("game-images/0hearts.png").convert_alpha(), scale),
            pygame.transform.scale(pygame.image.load("game-images/.5hearts.png").convert_alpha(), scale),
            pygame.transform.scale(pygame.image.load("game-images/1hearts.png").convert_alpha(), scale),
            pygame.transform.scale(pygame.image.load("game-images/1.5hearts.png").convert_alpha(), scale),
            pygame.transform.scale(pygame.image.load("game-images/2hearts.png").convert_alpha(), scale),
            pygame.transform.scale(pygame.image.load("game-images/2.5hearts.png").convert_alpha(), scale),
            pygame.transform.scale(pygame.image.load("game-images/3hearts.png").convert_alpha(), scale),
            pygame.transform.scale(pygame.image.load("game-images/3.5hearts.png").convert_alpha(), scale),
            pygame.transform.scale(pygame.image.load("game-images/4hearts.png").convert_alpha(), scale),
            pygame.transform.scale(pygame.image.load("game-images/4.5hearts.png").convert_alpha(), scale),
            pygame.transform.scale(pygame.image.load("game-images/5hearts.png").convert_alpha(), scale),
        ]

    def draw(self, surface):
        self.image = self.Hearts[self.player_instance.health]
        surface.blit(self.image,(self.x,self.y))
