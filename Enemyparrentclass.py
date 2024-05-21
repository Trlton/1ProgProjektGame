
def Enemyboi():
    class Enemy(GameObject):
        def __init__(self, screen, xpos, ypos, width, height, maxHealth, xSpeed, ySpeed, maxSpeed, sprite_path=None):
            super().__init__(screen, xpos, ypos, width, height, maxHealth, sprite_path)
            self.xenemy = xpos
            self.yenemy = ypos
            self.xSpeed = xSpeed
            self.ySpeed = ySpeed
            self.maxSpeed = maxSpeed

            sprite_path = Singlerangedhenchman.png


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

    def draw(self):
        super().draw()

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
