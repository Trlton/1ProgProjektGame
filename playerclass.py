import pygame
from pygame.math import Vector2
import constants as game_constants


class player():


    def __init__(self, screen, xpos, ypos, width, height):
        super().__init__()
        self.rect = pygame.Rect(xpos, ypos, width, height)
        self.pos = Vector2(xpos, ypos)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)
        self.currentHealth = game_constants.playerMaxHealth
        self.screen = screen


        # dictionary for different states of the player - later used to change via Movement
        self.images = {
            "idle": pygame.image.load(game_constants.playerPNG).convert_alpha(),
            "up": pygame.image.load(game_constants.playerUpPNG).convert_alpha() if hasattr(game_constants, "playerUpPNG") else None,
            "down": pygame.image.load(game_constants.playerDownPNG).convert_alpha() if hasattr(game_constants, "playerDownPNG") else None,
            "left": pygame.image.load(game_constants.playerLeftPNG).convert_alpha() if hasattr(game_constants, "playerLeftPNG") else None,
            "right": pygame.image.load(game_constants.playerRightPNG).convert_alpha() if hasattr(game_constants, "playerRightPNG") else None,
        }
        self.current_image = self.images["idle"]

    def updatePlayer(self, blocks):
        self.acc = Vector2(0, 0)

        # Check input and set image and acceleration
        keys = pygame.key.get_pressed()
        if keys[game_constants.leftBinding]:
            self.acc.x = -1
            self.current_image = self.images.get("left", self.images["idle"])
        if keys[game_constants.rightBinding]:
            self.acc.x = 1
            self.current_image = self.images.get("right", self.images["idle"])
        if keys[game_constants.upBinding]:
            self.acc.y = -1
            self.current_image = self.images.get("up", self.images["idle"])
        if keys[game_constants.downBinding]:
            self.acc.y = 1
            self.current_image = self.images.get("down", self.images["idle"])

        if self.acc.length_squared() > 0:
            self.acc = self.acc.normalize()

        self.acc *= game_constants.playerMaxSpeed
        self.pos += self.acc

        # Update player position
        self.rect.center = self.pos

        # Handle collisions
        self.handle_collisions(blocks)

    def handle_collisions(self, blocks):
        for block in blocks:
            if self.rect.colliderect(block.rect):
                if self.acc.x > 0:  # Moving right
                    self.rect.right = block.rect.left
                if self.acc.x < 0:  # Moving left
                    self.rect.left = block.rect.right
                if self.acc.y > 0:  # Moving down
                    self.rect.bottom = block.rect.top
                if self.acc.y < 0:  # Moving up
                    self.rect.top = block.rect.bottom

    def draw(self, screen, camera):
        adjusted_rect = self.rect.move(camera.camera.topleft)
        screen.blit(self.current_image, adjusted_rect)


