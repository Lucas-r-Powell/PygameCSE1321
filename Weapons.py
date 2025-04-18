import pygame
import Config

class Weapons:
    def __init__(self):
        self.dmg = Config.WEAPONDMG
        self.sprite = pygame.image.load(Config.WEAPONSPRITE)
        self.ammo = Config.WEAPONAMMO
        self.firesound = pygame.mixer.Sound(Config.WEAPONFX)
        self.emptysound = pygame.mixer.Sound(Config.WEAPONFX)

    def fire(self):
        if self.ammo > 0:
            pass
    def reload(self):
        pass

    def drop(self):
        pass

    def pickup(self):
        pass