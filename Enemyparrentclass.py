import pygame

class gameObject:
    xSpeed = 0
    ySpeed = 0
    widthHitbox = 0
    heightHitbox = 0
    maxHealth = 0
    currentHealth = 0

    def healthChange(self, maxHealth, currentHealth, damage):
        # Damages or heals entity based on how much damage the damage source deals.
        # Negative damage = healing
        currentHealth -= damage
        print(currentHealth)
        if currentHealth > maxHealth:
            currentHealth = maxHealth

class Enemy(gameObject):
    def __init__(self, screen, xpos, ypos, width, height, maxHealth, xSpeed, ySpeed, maxSpeed, sprite_path=None):
        super().__init__()
        self.rect = pygame.Rect(xpos, ypos, width, height)
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.maxSpeed = maxSpeed

        self.image_path = "Billedefolder\\Singlerangedhenchman.png"
        self.image = pygame.image.load(self.image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
    def move(self):
        self.rect.x += self.xSpeed
        self.rect.y += self.ySpeed

        # Ensure the enemy doesn't exceed max speed
        if self.xSpeed > self.maxSpeed:
            self.xSpeed = self.maxSpeed
        if self.ySpeed > self.maxSpeed:
            self.ySpeed = self.maxSpeed

    def update(self):
        # Update enemy logic here (e.g., movement, AI)
        self.move()

    def draw(self, surface, camera):
        adjusted_rect = self.rect.move(camera.camera.topleft)
        surface.blit(self.image, adjusted_rect)

from Playerclasstest import player

class CollisionDetector:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy


        def crash(self):
            if self.player.y < self.enemy.y:
                if self.player.x < self.enemy.x or self.player.x > self.enemy.x:
                    if self.player.x < self.enemy.x_position:
                        return True
                    import SpriteParrentClass
                    self.currentHealth=  self.currentHealth - 1
                    return False

                    #gør det afhægigt af velocity
                    # giv hp damage
