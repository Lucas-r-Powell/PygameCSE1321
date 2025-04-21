import pygame

class BrightnessSlider:
    def __init__(self, x, y, w, h, brightness):
        self.rect = pygame.Rect(x, y, w, h)
        self.slider_rect = pygame.Rect(x + brightness * w, y, 10, h)
        self.dragging = False
        self.brightness = brightness

    def draw(self, screen):
        pygame.draw.rect(screen, (180, 180, 180), self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.slider_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.slider_rect.collidepoint(event.pos):
            self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            self.slider_rect.x = max(self.rect.x, min(event.pos[0], self.rect.x + self.rect.width))
            self.brightness = (self.slider_rect.x - self.rect.x) / self.rect.width

    def get_brightness(self):
        return self.brightness
