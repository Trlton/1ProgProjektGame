import pygame

class BlockClass:
    def __init__(self, x, y, width, height, image_path):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))

    def draw(self, surface, camera):
        adjusted_rect = self.rect.move(camera.camera.topleft)
        surface.blit(self.image, adjusted_rect)
