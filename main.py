import pygame
import os
import playerclass
import SoundPlayer
from Parrentclass import GameObejct
from Terrianclass import terrainprøve
from Enemyparrentclass import Enemyboi

pygame.init()
info = pygame.display.Info()
gameWindowWidth, gameWindowHeight = info.current_w, info.current_h
display = pygame.display.set_mode((gameWindowWidth, gameWindowHeight))

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
