import pygame
class boundary(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.boundaryhitbox = -2
        self.width = 50
        self.height = 150
        self.color = (255,0,0)

    def collision(self, player):
        if player.x + player.width > self.x and player.x < self.x + self.width:
            if player.y + player.height > self.y and player.y < self.y + self.height:
                return True

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), self.boundaryhitbox)
        #pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

class boundary1(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.boundaryhitbox = -2
        self.width = 150
        self.height = 50
        self.color = (255,0,0)

    def collision(self, player):
        if player.x + player.width > self.x and player.x < self.x + self.width:
            if player.y + player.height > self.y and player.y < self.y + self.height:
                return True

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), self.boundaryhitbox)
        #pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

class bigboundary(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.boundaryhitbox = -2
        self.width = 150
        self.height = 150
        self.color = (255,80,0)

    def collision(self, player):
        if player.x + player.width > self.x and player.x < self.x + self.width:
            if player.y + player.height > self.y and player.y < self.y + self.height:
                return True

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), self.boundaryhitbox)
        #pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

class actiontrigger(object):
    def __init__(self, x, y, text, switchstate, npc):
        self.x = x
        self.y = y
        self.text = text
        self.switchstate = switchstate
        self.npc = npc
        self.boundaryhitbox = -2
        self.width = 20
        self.height = 20
        self.color = (0,255,0)

    def getlevelswitch(self):
        if self.switchstate:
            return True
        else:
            return False

    def getnpcstate(self):
        if self.npc:
            return True
        else:
            return False

    def collision(self, player):
        if player.x + player.width > self.x and player.x < self.x + self.width:
            if player.y + player.height > self.y and player.y < self.y + self.height:
                return True

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), self.boundaryhitbox)
        #pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))