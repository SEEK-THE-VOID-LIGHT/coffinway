import pygame

class playerclass(object):
    walkLeft = [pygame.image.load('mediaassets/left1.png'), pygame.image.load('mediaassets/left2.png'),
                pygame.image.load('mediaassets/left3.png')]
    walkRight = [pygame.image.load('mediaassets/right1.png'), pygame.image.load('mediaassets/right2.png'),
                 pygame.image.load('mediaassets/right3.png')]
    walkDown = [pygame.image.load('mediaassets/down1.png'), pygame.image.load('mediaassets/down2.png'),
                pygame.image.load('mediaassets/down3.png')]
    walkUp = [pygame.image.load('mediaassets/up1.png'), pygame.image.load('mediaassets/up2.png'),
              pygame.image.load('mediaassets/up3.png')]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 28
        self.height = 60
        self.right = False
        self.left = False
        self.up = False
        self.down = True
        self.standing = True
        self.color = (0, 255, 255)
        self.moveVelocity = 4
        self.walkCount = 0
        self.hitbox = (self.x, self.y, 28, 60)
        self.hitvisible = -3

    def draw(self, win):
        if self.walkCount + 1 >= 10:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            if self.right:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            if self.up:
                win.blit(self.walkUp[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            if self.down:
                win.blit(self.walkDown[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(self.walkRight[0], (self.x, self.y))
            if self.left:
                win.blit(self.walkLeft[0], (self.x, self.y))
            if self.up:
                win.blit(self.walkUp[0], (self.x, self.y))
            if self.down:
                win.blit(self.walkDown[0], (self.x, self.y))
        #print(f"{self.standing} - {self.right} - {self.left} - {self.up} - {self.down}")

        self.hitbox = (self.x + 10, self.y + 10, 28, 55)
        pygame.draw.rect(win, (0, 0, 255), self.hitbox, self.hitvisible)

    def messagebox(self, input, win):
        font = pygame.font.SysFont('comicsans', 50)
        text = font.render(input, 1, (255, 255, 255))
        textx = 1280 / 2 - text.get_width() // 2
        texty = 950
        textwidth = text.get_width() + 50
        pygame.draw.rect(win, (0,0,0), (textx - 10, texty + 5, textwidth +20, 60))
        pygame.draw.rect(win, (28,128,96), (textx, texty, textwidth, 70))
        pygame.draw.rect(win, (0, 0, 0), (textx, texty, textwidth, 70), 10)
        win.blit(text, (textx + 25, texty + 15))
        pygame.display.update()
        i = 0
        while i < 200:
            pygame.time.delay(10)
            i += 1
