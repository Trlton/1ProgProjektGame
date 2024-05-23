#bør virke
import pygame
from pygame.math import Vector2
import constants as game_constants

class GameObject:
    def __init__(self):
        self.xSpeed = 0
        self.ySpeed = 0
        self.widthHitbox = 0
        self.heightHitbox = 0
        self.maxHealth = 0
        self.currentHealth = 0

    def healthChange(self, damage):
        self.currentHealth -= damage
        print(self.currentHealth)
        if self.currentHealth > self.maxHealth:
            self.currentHealth = self.maxHealth

class Player(GameObject):
    def __init__(self, screen, xpos, ypos, width, height):
        super().__init__()
        self.rect = pygame.Rect(xpos, ypos, width, height)
        self.pos = Vector2(xpos, ypos)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)
        self.currentHealth = game_constants.playerMaxHealth
        self.screen = screen

    def updatePlayer(self):
        self.acc = Vector2(0, 0)

        # Check input and set acceleration
        keys = pygame.key.get_pressed()
        if keys[game_constants.leftBinding]:
            self.acc.x = -1
        if keys[game_constants.rightBinding]:
            self.acc.x = 1
        if keys[game_constants.upBinding]:
            self.acc.y = -1
        if keys[game_constants.downBinding]:
            self.acc.y = 1

        if self.acc.length_squared() > 0:
            self.acc = self.acc.normalize()

        self.acc *= game_constants.playerAcceleration

        # Apply friction
        self.vel *= 0.9

        # Update velocity
        self.vel += self.acc

        # Update position
        self.pos += self.vel + 0.5 * self.acc

        # Update the rect position
        self.rect.center = self.pos

    def draw(self, screen, hitboxColor, camera):
        adjusted_rect = self.rect.move(camera.camera.topleft)
        pygame.draw.rect(screen, hitboxColor, adjusted_rect)
