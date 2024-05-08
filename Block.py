import pygame

#BLOCK TYPES:
#Square Block
#Wide Block
#Tall Block
#Ghost Block
#Custom Block (choose  xy coords)

class BlockClass:
    color = (100, 100, 100)

    def __init__(self, screen, type, _x, _y, customWidth, customHeight): #, _x, _y, _width, _height):
        self.theScreen = screen
        self.x = _x
        self.y = _y

        if type == "Square Block":
            self.width = 50
            self.height = 50
        elif type == "Wide Block":
            self.width = 100
            self.height = 50
        elif type == "Tall Block":
            self.width = 50
            self.height = 100
        elif type == "Ghost Block":
            self.width = 50
            self.height = 50
            self.collidable = False
        elif type == "Custom Block":
            self.width = customWidth
            self.height = customHeight


    def draw(self):
        #TODO: FIX THIS CODE WHEN YOU HAVE SPRITES.
        #sprite = pygame.image.load(type + ".bmp")
        #spriterect = sprite.get_rect()
        #self.theScreen.blit(sprite, spriterect)
        pygame.draw.rect(self.theScreen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
