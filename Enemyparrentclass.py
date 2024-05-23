import pygame
from pygame.math import Vector2
import constants as game_constants
class Enemyboi:
    def __init__(self, screen, xpos, ypos, width, height, maxHealth, maxSpeed, sprite_path=None):
        self.screen = screen
        self.rect = pygame.Rect(xpos, ypos, width, height)
        self.pos = Vector2(xpos, ypos)
        self.maxHealth = maxHealth
        self.currentHealth = maxHealth
        self.maxSpeed = maxSpeed
        self.maxSpeed = maxSpeed

        sprite_path = "Billedefolder/Singlerangedhenchman.png"
#bør ændres nu
class Enemycloserange():
    def __init__(self, screen, xpos, ypos, width, height, maxHealth, xSpeed, ySpeed, maxSpeed, sprite_path=None):
        super().__init__(screen, xpos, ypos, width, height, maxHealth, sprite_path)
        self.xenemycloserange = xpos
        self.yenemycloserange = ypos
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.maxSpeed = maxSpeed

def healthChangeenemy(self, enemymaxHealth, enemycurrentHealth, damage):
    enemycurrentHealth -= damage
    print(enemycurrentHealth)
    if enemycurrentHealth > enemymaxHealth:
        enemycurrentHealth = enemymaxHealth

def move(self):
    self.rect.x += self.xSpeed
    self.rect.y += self.ySpeed

    # Ensure the enemy doesn't exceed max speed
    if self.xSpeed > self.maxSpeed:
        self.xSpeed = self.maxSpeed
    if self.ySpeed > self.maxSpeed:
        self.ySpeed = self.maxSpeed

def update(self):
    # Update enemy logic here (e.g., movement, AI)
    self.move_towards_player(player_pos)

def draw(self):
    super().draw()

from Playerclasstest import Player

class CollisionDetector:
    def __init__(self, player, enemy, enemyclose):
        self.player = player
        self.enemy = enemy
        self.enemyclose = enemyclose


    def crash(self):
        if self.player.y < self.enemy.y:
            if self.player.x < self.enemy.x or self.player.x > self.enemy.x:
                if self.player.x < self.enemy.x_position:
                    if self.player.y < self.enemyclose.y:
                        if self.player.x < self.enemyclose.x or self.player.x > self.enemyclose.x:
                            if self.player.x < self.enemyclose.x_position:
                                if self.enemy.x < self.enemyclose.x_position:
                                    if self.enemy.y < self.enemyclose.y_position:
                                        return True
                                    enemycurrentHealth = self.currentHealth - 1
                                    playercurrentHealth = Player.currentHealth - 1
                import SpriteParrentClass
                return False

def move_towards_player(self, player_pos):
    direction = player_pos - self.pos
    if direction.length() > 0:
        direction = direction.normalize() * self.maxSpeed
    self.pos += direction
    self.rect.center = self.pos

def update(self, player_pos):
    self.move_towards_player(player_pos)

def draw(self):
    self.screen.blit(self.sprite, self.rect.topleft)

def take_damage(self, damage):
    self.currentHealth -= damage
    if self.currentHealth <= 0:
        self.currentHealth = 0
        # Add logic for what happens when the enemy dies (e.g., remove from game)


#class EnemyCloserange(enemy):
# Inherit from Enemy and can add specific behaviors for close-range enemies
#   pass
#gør det afhægigt af velocity
# giv hp damage


