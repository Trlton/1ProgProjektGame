import pygame
from pygame.locals import *
import constants as game_constants
from playerClass import player
from cameraClass import Camera


pygame.init()

# setting up the display
gameScreen = pygame.display.set_mode((game_constants.resolution))
pygame.display.set_caption(game_constants.GAME_TITLE)

# Create clock for fps controll for ease of use
clock = pygame.time.Clock()


# use player object
player_object = player(gameScreen,
                       game_constants.GAME_WIDTH // 2,
                       game_constants.GAME_HEIGHT // 2,
                       game_constants.playerHitboxWidth,
                       game_constants.playerHitboxHeight)

# make camera obejct:
                    # values are witdh and height of playspace
camera = Camera(game_constants.GAME_WIDTH,
                game_constants.GAME_HEIGHT)

# testing grounds terrain - checkered playground
def draw_checkered_background(surface, block_size, camera):
    for y in range(0, camera.height, block_size):
        for x in range(0, camera.width, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            adjusted_rect = rect.move(camera.camera.topleft)
            if (x // block_size + y // block_size) % 2 == 0:
                pygame.draw.rect(surface, game_constants.WHITE, adjusted_rect)
            else:
                pygame.draw.rect(surface, game_constants.GRAY, adjusted_rect)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    # Update player
    player_object.updatePlayer()

    # Update camera onto player
    camera.update(player_object)

    # draw functions stuff
    gameScreen.fill(game_constants.BLACK)
    draw_checkered_background(gameScreen, 100, camera)
    player_object.draw(gameScreen, game_constants.RED, camera)

    # update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(game_constants.FPS)

pygame.quit()
