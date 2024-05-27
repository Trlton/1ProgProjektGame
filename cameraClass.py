import pygame  
import constants

#This class makes the player centered - until player reaches the sides

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + int(constants.SCREEN_WIDTH / 2)
        y = -target.rect.centery + int(constants.SCREEN_HEIGHT / 2)

        # Stop camera movement when reached sides / map end
        x = min(-130, x)  # left side
        y = min(-80, y)  # top side
        x = max(-(self.width - constants.SCREEN_WIDTH -130), x)  # right side
        y = max(-(self.height - constants.SCREEN_HEIGHT -80), y)  # bottom side

        self.camera = pygame.Rect(x, y, self.width, self.height)