import pygame
import random
from Player import player
from HeartBar import HeartBar



class Medkit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load("game-images/CSE_1311_images/Medkit.png").convert_alpha()
        scaled_image = pygame.transform.scale(original_image, (100, 100))  # or whatever size you want
        self.image = scaled_image
        self.rect = self.image.get_rect()

        hitbox_width = self.rect.width * 1
        hitbox_height = self.rect.height * 1
        self.rect = pygame.Rect(0, 0, hitbox_width, hitbox_height)


       #Position
        padding_x = 40
        padding_y = 40
        self.rect.topleft = (
            random.randint(padding_x, 1280 - int(hitbox_width) - padding_x),
            random.randint(padding_y, 720 - int(hitbox_height) - padding_y)
        )

        self.heal_amount = 4
        print(f"Medkit spawned at: {self.rect.topleft}")

    def collision(self, player):
        if player.rect.colliderect(self.rect):
            player.Gain_health(self.heal_amount)
            self.kill()

    def draw(self,surface):
        surface.blit(self.image,self.rect)