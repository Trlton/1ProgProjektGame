
def Enemyboi():
    class Enemy(GameObject):
        def __init__(self, screen, xpos, ypos, width, height, maxHealth, xSpeed, ySpeed, maxSpeed, sprite_path=None):
            super().__init__(screen, xpos, ypos, width, height, maxHealth, sprite_path)
            self.xSpeed = xSpeed
            self.ySpeed = ySpeed
            self.maxSpeed = maxSpeed

            sprite_path = Single ranged henchman.png

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