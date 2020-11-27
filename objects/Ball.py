import pygame

class Ball:
    def __init__(self, screen, color, posX, posY, radius):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.radius = radius
        self.direcX = 0
        self.direcY = 0
        self.showBall()



    def showBall(self):
        pygame.draw.circle(self.screen, self.color, (self.posX, self.posY), self.radius)

    def startMovingBall(self):
        self.direcX = 15
        self.direcY = 5

    def moveBall(self):
        self.posX  += self.direcX
        self.direcY += self.direcY