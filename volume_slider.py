import pygame

class VolumeSlider:
    def __init__(self, x, y, width, height, initial_volume=0.8):
        self.rect = pygame.Rect(x, y, width, height)
        self.slider_rect = pygame.Rect(x + int(width * initial_volume), y - 5, 10, height + 10)
        self.dragging = False
        self.volume = initial_volume

    def draw(self, screen):
        # Draw the slider background
        pygame.draw.rect(screen, (180, 180, 180), self.rect)
        # Draw the slider knob
        pygame.draw.rect(screen, (0, 128, 0), self.slider_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.slider_rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                new_x = max(self.rect.left, min(event.pos[0], self.rect.right))
                self.slider_rect.x = new_x
                self.volume = (new_x - self.rect.left) / self.rect.width
                pygame.mixer.music.set_volume(self.volume)

    def get_volume(self):
        return self.volume
