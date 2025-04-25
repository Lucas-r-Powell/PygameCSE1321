import pygame
import Config
import math

class Weapons:
    def __init__(self):
        self.dmg = Config.WEAPON_DMG
        self.sprite = pygame.image.load(Config.WEAPON_SPRITE)
        self.ammo = Config.WEAPONAMMO
        self.firesound = pygame.mixer.Sound(Config.WEAPONFX)
        self.emptysound = pygame.mixer.Sound(Config.WEAPONFX)

    def Hitscan(self,line_start, line_end, circle_center, circle_radius):
        ax, ay = line_start
        bx, by = line_end
        cx, cy = circle_center

        AB = (bx - ax, by - ay)
        AC = (cx - ax, cy - ay)
        AB_mag = math.sqrt(AB[0] ** 2 + AB[1] ** 2)
        AB_unit = (AB[0] / AB_mag, AB[1] / AB_mag)
        projection_length = AC[0] * AB_unit[0] + AC[1] * AB_unit[1]
        projection = (AB_unit[0] * projection_length, AB_unit[1] * projection_length)
        closest_point = (ax + projection[0], ay + projection[1])
        distance = math.sqrt((closest_point[0] - cx) ** 2 + (closest_point[1] - cy) ** 2)

        return distance <= circle_radius

    def fire(self):
        if self.ammo > 0:
            pass
    def reload(self):
        pass

    def drop(self):
        pass

    def pickup(self):
        pass