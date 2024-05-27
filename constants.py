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
gameHeight = 2000

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255,0,0)

# Game Title
GAME_TITLE = "__main__"

#PLAYER values
playerPNG = "andreTateBaseModel.png"
playerLeftPNG = "andreTateBaseModel.png"
playerRightPNG = "andreTateBaseModel.png"
playerUpPNG = "andreTateBaseModel.png"
playerDownPNG = "andreTateBaseModel.png"
playerMaxSpeed = 5
playerMaxHealth = 10

playerHitboxHeight = 133
playerHitboxWidth = 66

bulletSpeed = 1
bulletWidth = 100
bulletHeight = 10
    #Control bindings
        #Movement
upBinding = pygame.K_w
downBinding = pygame.K_s
leftBinding = pygame.K_a
rightBinding = pygame.K_d

diagonal_movement_multiplier = 0,71

escBinding = pygame.K_ESCAPE
        #Shooting bindings



