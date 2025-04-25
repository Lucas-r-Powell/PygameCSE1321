import pygame
import Config
class background:
    def __init__(self):
        self.texture = pygame.image.load(Config.GRASS_IMAGE_PATH)
        self.texture = pygame.transform.scale(self.texture,(100,100))
        self.blocksize = self.texture.get_width()
        self.rect = self.texture.get_rect()

    def draw_pattern(self,surface):
          #the texture must be a square
        for y in range(0, Config.HEIGHT, self.blocksize):
            for x in range(0, Config.WIDTH, self.blocksize):
                rect = pygame.Rect(x,y, self.blocksize,self.blocksize)
                if (x // self.blocksize) % 2 == (y // self.blocksize) % 2:
                    surface.blit(self.texture, rect)
                else:
                    surface.blit(self.texture,rect)