import pygame
from pygame.locals import *
import constants as game_constants
import playerclass
from Enemyparrentclass import *
from cameraClass import Camera
from Block import BlockClass

pygame.init()

# Setting up the display
gameScreen = pygame.display.set_mode((game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT))
pygame.display.set_caption(game_constants.GAME_TITLE)

# Create clock for fps control
clock = pygame.time.Clock()


# use player object
player_object = playerclass.player(gameScreen,
                       game_constants.gameWidth // 2,
                       game_constants.gameHeight // 2,
                       game_constants.playerHitboxWidth,
                       game_constants.playerHitboxHeight)


# make camera obejct:
                    # values are witdh and height of playspace
camera = Camera(game_constants.gameWidth,
                game_constants.gameHeight)

# Create block objects with paths to the PNG images
block_size = 50  # Assuming each block is 50x50 pixels
block_image_path = 'Square_Block.png'
blocks = []

# Create a barrier of blocks around the map
for xCoord in range(0, game_constants.gameWidth, block_size):
    blocks.append(BlockClass(xCoord, 180, block_size, block_size, block_image_path))  # Top edge
    blocks.append(BlockClass(xCoord, game_constants.gameHeight - 180 - block_size, block_size, block_size, block_image_path))  # Bottom edge

for yCoord in range(0, game_constants.gameHeight, block_size):
    blocks.append(BlockClass(320, yCoord, block_size, block_size, block_image_path))  # Left edge
    blocks.append(BlockClass(game_constants.gameWidth - 320 - block_size, yCoord, block_size, block_size, block_image_path))  # Right edge

#Create block path that the player goes through in the map:
for pathX in range (320+block_size, game_constants.gameWidth // 2):
    blocks.append(BlockClass(pathX, game_constants.gameHeight // 3, block_size, block_size, block_image_path))  # Top edge
    blocks.append(BlockClass(pathX, game_constants.gameHeight // 3 - block_size*4, block_size, block_size, block_image_path))  # Bottom edge

# Create an enemy object
Enemy = Enemyboi(gameScreen,
              100, 100,
              game_constants.playerHitboxWidth, game_constants.playerHitboxHeight,
              10,
              2,
              "Billedefolder/Singlerangedhenchman.png")

# Testing grounds terrain - checkered playground
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
        elif event.type == KEYDOWN:
            if event.key == game_constants.escBinding:
                running = False

    # Update player
    player_object.updatePlayer(blocks)

    # Update camera
    camera.update(player_object)

    # Update enemy
#    Enemy.update(player_object.pos)

    # Draw functions
    gameScreen.fill(game_constants.BLACK)
    draw_checkered_background(gameScreen, 50, camera)
    player_object.draw(gameScreen, camera)
#    Enemy.draw()

    # Update the display
    # Update player
    player_object.updatePlayer(blocks)

    # Update camera onto player
    camera.update(player_object)

    # draw functions stuff
    gameScreen.fill(game_constants.BLACK)
    draw_checkered_background(gameScreen, 100, camera)
    player_object.draw(gameScreen, camera)

    # Draw blocks
    for block in blocks:
        block.draw(gameScreen, camera)
  
    # update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(game_constants.FPS)

pygame.quit()
