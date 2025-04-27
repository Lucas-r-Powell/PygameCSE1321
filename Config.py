#settings
import pygame

DEBUG = True

WIDTH, HEIGHT = 1280, 720
#background
GRASS_IMAGE_PATH = "game-images/Grasstexture.jpg"
TREE_IMAGE_PATH = "game-images/tree.png"
#player Values
PLAYER_SPEED = 10
PLAYER_DASH_TIME = 5
PLAYER_HEALTH = 1

PLAYER_IMAGE_PATH = "game-images/player.png"
PLAYER_DEATH_SOUND_PATH = "game-sounds/Deathfx.mp3"

LASTDAMAGE = 0

HEARTBAR = [
    "game-images/CSE_1311_images/0hearts.png",
    "game-images/CSE_1311_images/_5hearts.png",
    "game-images/CSE_1311_images/1hearts.png",
    "game-images/CSE_1311_images/1.5hearts.png",
    "game-images/CSE_1311_images/2hearts.png",
    "game-images/CSE_1311_images/2.5hearts.png",
    "game-images/CSE_1311_images/3hearts.png",
    "game-images/CSE_1311_images/3.5hearts.png",
    "game-images/CSE_1311_images/4hearts.png",
    "game-images/CSE_1311_images/4.5hearts.png",
    "game-images/CSE_1311_images/5hearts.png"
]

ZOMBIE_HORDE_NUM = 5

#zombies
ZOMBIE_HEALTH = 1
ZOMBIE_SPEED = 5
ZOMBIE_DAMAGE = 1
ZOMBIE_SPAWN_EVENT = pygame.USEREVENT + 1

MEDKIT_SPAWN_EVENT = pygame.USEREVENT + 2

ZOMBIE_IMAGE_PATH = "game-images/zombie.png"
ZOMBIE_DEATH_SOUND_PATH = "game-sounds/Zombiedeathsound.mp3"
#Weapons


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
    "shotgun": 2000,
    "Rifle": 3000,
    "Sniper": 3000
}

IFRAMES = 500
