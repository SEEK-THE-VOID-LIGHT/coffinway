from boundary import *
from playerclass import *
from boundaries import *
from story import *
import pygame

pygame.init()
win = pygame.display.set_mode((1280,1080), pygame.FULLSCREEN)
bg = pygame.image.load('mediaassets/background.jpg')
logo = pygame.image.load('mediaassets/coffinwaylogo.png')
npc = pygame.image.load('mediaassets/npc1.png')
talk = pygame.mixer.Sound('mediaassets/talk.wav')
npc = pygame.transform.scale(npc, (35,45))
clock = pygame.time.Clock()

def redrawGameWindow():
    if storycount == 11:
        win.fill((0,0,0))
        font = pygame.font.SysFont('comicsans', 60)
        text = font.render("ENDE", 1, (255,255,255))
        text1 = font.render("Danke fuer's spielen", 1, (255,255,255))
        win.blit(text, (1280//2 - text.get_width(), 1080 //2))
        win.blit(text1, (1280 // 2 - text.get_width() - 100, 1080 // 2 + 60))
    else:
        win.blit(bg, (0,0))
        #win.fill((255,255,255))
        #creategrid(win, boundaries[1].boundaryhitbox)
        #creategrid(win, 1)
        for i in boundaries:
            i.draw(win)
        for i in actions:
            i.draw(win)
            if i.getnpcstate():
                win.blit(npc, (i.x - 40, i.y + 10))
        player.draw(win)

    pygame.display.update()


if __name__ == "__main__":
    ### SETUP ###
    run = False
    menu = True
    player = playerclass(700, 1020)
    boundaries = []
    actions = []
    ticker = 0
    storycount = returnstorycount()
    save(storycount)

    actionlocations = getlevel(storycount)
    for i in range(len(boundarylocations)):
        boundaries.append(boundary(int(boundarylocations[i][0]), int(boundarylocations[i][1])))
    for i in range(len(boundarylocations1)):
        boundaries.append(boundary1(int(boundarylocations1[i][0]), int(boundarylocations1[i][1])))
    for i in range(len(actionlocations)):
        actions.append(actiontrigger(int(actionlocations[i][0]), int(actionlocations[i][1]), actionlocations[i][2], actionlocations[i][3], actionlocations[i][4]))
    for i in range(len(bigboundarylocations)):
        boundaries.append(bigboundary(int(bigboundarylocations[i][0]), int(bigboundarylocations[i][1])))
    ### SETUP END ###

    ### MAIN LOOP ###
    for i in range(10):
        while menu:

            temp = True
            if not pygame.mixer.music.get_busy():
                if temp:
                    music = pygame.mixer.music.load('mediaassets/menu.mp3')
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1)
                    temp = False

            clock.tick(27)
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    run = False
            win.fill((0,0,0))
            font = pygame.font.SysFont('comicsans', 50)
            text = font.render('Press ENTER to start/continue game', 1, (255,255,255))
            win.blit(text, (300 ,800))
            win.blit(logo, (170,100))

            menukeys = pygame.key.get_pressed()

            if menukeys[pygame.K_ESCAPE]:
                run = False
                menu = False
            if menukeys[pygame.K_RETURN]:
                temp = True
                pygame.mixer.music.stop()
                menu = False
                run = True

            pygame.display.update()

        while run:

            temp = True
            if not pygame.mixer.music.get_busy():
                if temp:
                    music = pygame.mixer.music.load('mediaassets/game.mp3')
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1)
                    temp = False

            clock.tick(27)
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()


            if keys[pygame.K_LEFT] and player.x > 65:
                player.x -= player.moveVelocity
                for i in boundaries:
                    if i.collision(player) == True:
                        player.x += player.moveVelocity
                player.left = True
                player.right = False
                player.up = False
                player.down = False
                player.standing = False

            elif keys[pygame.K_RIGHT] and player.x + player.width < 1215:
                player.left = False
                player.right = True
                player.up = False
                player.down = False
                player.standing = False
                player.x += player.moveVelocity
                for i in boundaries:
                    if i.collision(player) == True:
                        player.x -= player.moveVelocity

            elif keys[pygame.K_DOWN] and player.y + player.height < 1080:
                player.left = False
                player.right = False
                player.up = False
                player.down = True
                player.standing = False
                player.y += player.moveVelocity
                for i in boundaries:
                    if i.collision(player) == True:
                        player.y -= player.moveVelocity

            elif keys[pygame.K_UP] and player.y > 0:
                player.left = False
                player.right = False
                player.up = True
                player.down = False
                player.standing = False
                player.y -= player.moveVelocity
                for i in boundaries:
                    if i.collision(player) == True:
                        player.y += player.moveVelocity
            else:
                player.standing = True
                player.walkCount = 0

            if keys[pygame.K_SPACE]:
                if run:
                    for i in actions:
                        if i.collision(player) == True:
                            talk.play()
                            player.messagebox(i.text, win)
                            if i.getlevelswitch():
                                storycount += 1
                                actionlocations = getlevel(storycount)
                                actions.clear()
                                for i in range(len(actionlocations)):
                                    actions.append(actiontrigger(int(actionlocations[i][0]), int(actionlocations[i][1]),
                                                                 actionlocations[i][2], actionlocations[i][3],
                                                                 actionlocations[i][4]))
                                    save(storycount)


            if keys[pygame.K_0]:
                ticker += 1
                if ticker == 1:
                    player.hitvisible *= -1
                    for i in boundaries:
                        i.boundaryhitbox *= -1
                    for i in actions:
                        i.boundaryhitbox *= -1
                if ticker == 5:
                    ticker = 0

            if keys[pygame.K_9]:
                player.messagebox(f"{str(player.x)}-{str(player.y)}", win)

            if keys[pygame.K_ESCAPE]:
                pygame.time.delay(500)
                temp = False
                pygame.mixer.music.stop()
                run = False
                menu = True

            redrawGameWindow()
