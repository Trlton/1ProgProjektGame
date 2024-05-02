from pygame import *

class gameObejct :
    xSpeed = 0
    ySpeed = 0
    maxSpeed = 0
    widthHitbox = 0
    heightHitbox = 0
    maxHealth = 0
    currentHealth = 0



    def healthChange(maxHealth, currentHealth, damage):
        #Damages or heals entity based on how much damage the damage source deals.
        #Negative damage = healing
        currentHealth -= damage
        print(currentHealth)
        if currentHealth > maxHealth:
            currentHealth = maxHealth


    def __init__(self,screen,xpos,ypos):
        self.x = xpos
        self.y = ypos
        self.gameWidget = screen
        self.screenWidth = self.gameWidget.get_size()[0]
        self.screenHeight = self.theScreen.get_size()[1]


    def hitbox(self):
        pygame.Rect()

    def update(self):
        self.x+=self.xSpeed
        self.y+=self.ySpeed




























