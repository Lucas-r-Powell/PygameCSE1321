import pygame
import Config
import math


class Weapons:
    lastreloadtime = 0
    def __init__(self):
        self.dmg = Config.WEAPON_DMG
        self.sprite = pygame.image.load(Config.WEAPON_SPRITE).convert_alpha()
        self.ammo = Config.WEAPONAMMO
        self.noammo = False
        self.reloading = False
        self.firesound = pygame.mixer.Sound(Config.WEAPONFX["shotgun"])
        self.emptysound = pygame.mixer.Sound(Config.WEAPONFX["shotgunempty"])
        self.reloadsound = pygame.mixer.Sound(Config.WEAPONFX["shotgunreload"])

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
        if self.reloading == False:
            if self.ammo["shotgun"] > 0:
                self.noammo = False
                self.ammo["shotgun"] -= 1
                self.firesound.play()
            else:
                self.emptysound.play()
                self.noammo = True

    def reload(self, time):
        if self.ammo["shotgun"] == Config.MAXWEAPONAMMO["shotgun"]:
            self.reloading = False
        elif time - Config.LASTRELOADTIME > Config.TIMETORELOAD["shotgun"]:
            self.reloading = True
            self.reloadsound.play()
            Config.LASTRELOADTIME = time
            self.ammo["shotgun"] = Config.MAXWEAPONAMMO["shotgun"]
            self.reload(0)
        else:
            self.reloading = False


    def draw(self, screen, player_topright, rotation_angle):
        rotated_image = pygame.transform.rotate(self.sprite, -rotation_angle - 90)
        new_rect = rotated_image.get_rect(center=player_topright)
        screen.blit(rotated_image, new_rect)
