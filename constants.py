import pygame.event

# Framerate
FPS = 60

# Screen Reolution
SCREEN_HEIGHT = 1080
SCREEN_WIDTH = 1920

# Playspace
gameWidth = 2500
gameHeight = 2500

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255,0,0)

# Game Title
GAME_TITLE = "__main__"

#PLAYER values
playerMaxSpeed = 10
playerMaxHealth = 10


    #Control bindings
        #Movement
upBinding = pygame.K_w
downBinding = pygame.K_s
leftBinding = pygame.K_a
rightBinding = pygame.K_d


diagonal_movement_multiplier = 0,71
