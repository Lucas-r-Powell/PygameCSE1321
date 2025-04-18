import pygame

class Button():
    def __init__(self, x, y, image, hover_image, scale, click_sound=None, alt_click_sound=None):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.hover_image = pygame.transform.scale(hover_image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.click_sound = click_sound
        self.alt_click_sound = alt_click_sound

    def draw(self, surface, use_alt_sound=False):
        action = False
        pos = pygame.mouse.get_pos()

        current_image = self.image

        if self.rect.collidepoint(pos):
            current_image = self.hover_image
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                action = True
                if use_alt_sound and self.alt_click_sound:
                    self.alt_click_sound.play()
                elif self.click_sound:
                    self.click_sound.play()

        surface.blit(current_image, self.rect.topleft)

        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

        return action
