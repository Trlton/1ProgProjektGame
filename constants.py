import pygame.event

# Surface = gameScreen

# Framerate
FPS = 60

# Screen Reolution
resolution = (1920,1080) # monitor resolution (width, height)
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Playspace
gameWidth = 2500
gameHeight = 1580

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255,0,0)

# Game Title
GAME_TITLE = "__main__"

#PLAYER values
playerPNG = "midlertidigPlayerPNG.png"

playerMaxSpeed = 10
playerMaxHealth = 10

playerHitboxHeight = 50
playerHitboxWidth = 50

    #Control bindings
        #Movement
upBinding = pygame.K_w
downBinding = pygame.K_s
leftBinding = pygame.K_a
rightBinding = pygame.K_d

diagonal_movement_multiplier = 0.71

playerAcceleration = 0.9

        #Shooting bindings
spacebinding = pygame.K_SPACE

        #General bindings
escBinding = pygame.K_ESCAPE
