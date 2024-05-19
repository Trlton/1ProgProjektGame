
from pygame import *
import constants

class gameObejct :
    xSpeed = 0
    ySpeed = 0
    widthHitbox = 0
    heightHitbox = 0
    maxHealth = 0
    currentHealth = 0



    def healthChange(maxHealth, currentHealth, damage):
        #Damages or heals entity based on how much damage the damage source deals.
        #Negative damage = healing
        currentHealth -= damage
        if currentHealth > maxHealth:
            currentHealth = maxHealth

    def __init__(self,screen, xpos, ypos, width, height):
        self.rect = pygame.Rect(xpos,ypos,width,height)
        self.rect.center = (xpos,ypos)

    def draw(self,screen, hitboxColor):
        pygame.draw.rect(screen, (hitboxC0olor), self.rect)











































