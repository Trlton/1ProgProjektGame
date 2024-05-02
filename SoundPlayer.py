import pygame

class SoundPlayer:
    def playSound(self, filePath):
        sfx = pygame.mixer.Sound(filePath)
        sfx.play()