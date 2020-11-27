import pygame

class Ball:
    def __init__(self, screen, color, posX, posY, radius):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.radius = radius
        self.showBall()

    def showBall(self):
        pygame.draw.circle(self.screen,self.color,(self.posX, self.posY), self.radius)