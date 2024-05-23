import pygame
from pygame.math import Vector2
import constants as game_constants
#bør virke
class gameObject:
    xSpeed = 0
    ySpeed = 0
    widthHitbox = 0
    heightHitbox = 0
    maxHealth = 0
    currentHealth = 0

    def healthChange(self, playermaxHealth, playercurrentHealth, damage):
        playercurrentHealth -= damage
        print(playercurrentHealth)
        if playercurrentHealth > playermaxHealth:
            playercurrentHealth = playermaxHealth


class player(gameObject):
    def __init__(self, screen, xpos, ypos, width, height):
        super().__init__()
        self.rect = pygame.Rect(width, height)
        self.xplayer = xpos
        self.yplayer = ypos
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

        self.acc *= game_constants.playerMaxSpeed
        self.pos += self.acc

        # Update player position
        self.rect.center = self.pos

    def draw(self, screen, hitboxColor, camera):
        adjusted_rect = self.rect.move(camera.camera.topleft)
        pygame.draw.rect(screen, hitboxColor, adjusted_rect)