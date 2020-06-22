import pygame
bigboundarylocations = [[855,420], [127,705], [265,705], [127,745], [265,745], [225, 420], [234, 420], [420, 290], [137,190], [330,70], [290,70], [260, -25]]

#vertical
boundarylocations = [[720, 680], [720, 575], [545, 680], [545, 575],
                     [831, 460], [976, 460],
                     [865, 740], [865, 820], [945, 740], [945, 820], [905, 740], [905, 820], [1140,930],
                     #fence
                     [780, 330], [780, 280], [190,550], [400,420]]


#horizontal
boundarylocations1 = [[545, 575], [620, 575], [545, 750], [620, 750], [90,12],
                      [855, 558], [1120, 558], [1020, 500],
                      [925,770], [925,820], [1000, 820], [1000, 740], [1000, 770],
                      #fence
                      [50,1023], [200,1023], [350,1023], [425,1023], [800,1023], [950,1023], [1100,1023], [1020, 500], [1120, 800], [90,330], [250, 330],
                      [285,520], [360,840]]

def creategrid(win, visible):
    gridmesaurement = 50
    for j in range(1200 // gridmesaurement + 10):
        for k in range(1080 // gridmesaurement + 1):
            pygame.draw.rect(win, (0, 0, 0), (j * gridmesaurement, k * gridmesaurement, gridmesaurement, gridmesaurement), visible)