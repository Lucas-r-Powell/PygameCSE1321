#settings
import pygame

WIDTH, HEIGHT = 1280, 720
#background
GRASS_IMAGE_PATH = "game-images/Grasstexture.jpg"
TREE_IMAGE_PATH = "game-images/tree.png"
#player Values
PLAYER_SPEED = 10
PLAYER_DASH_TIME = 5
PLAYER_HEALTH = 10

PLAYER_IMAGE_PATH = "game-images/player.png"
PLAYER_DEATH_SOUND_PATH = "game-sounds/Deathfx.mp3"

ZOMBIE_HORDE_NUM = 5

#zombies
ZOMBIE_HEALTH = 1
ZOMBIE_SPEED = 11
ZOMBIE_SPAWN_EVENT = pygame.USEREVENT + 1

ZOMBIE_IMAGE_PATH = "game-images/"
ZOMBIE_DEATH_SOUND_PATH = "game-sounds/"
#Weapons
RELOAD_SOUND_EVENT = pygame.USEREVENT + 2

LASTRELOADTIME = 0

WEAPON_DMG = 1
WEAPON_SPRITE = "game-images/shotgun.png"
WEAPONFX = {
    "Knife": "",
    "shotgun": "game-sounds/Shotgunfx.mp3",
    "shotgunempty":"game-sounds/emptyshotgunfx.mp3",
    "shotgunreload" : "game-sounds/shotgunreload.mp3",
    "Rifle": "",
    "Sniper": ""
}

WEAPONAMMO = {
    "Knife": -1,
    "shotgun": 6,
    "Rifle": 30,
    "Sniper": 12
}

MAXWEAPONAMMO = {
    "Knife": -1,
    "shotgun": 6,
    "Rifle": 30,
    "Sniper": 12
}

TIMETORELOAD = {
    "Knife": 0,
    "shotgun": 1000,
    "Rifle": 3000,
    "Sniper": 3000
}

