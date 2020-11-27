import pygame

class Paddle:

    def __init__(self, screen, color, posX, posY, width, height):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.showPaddle()


    def showPaddle(self):
        pygame.draw.rect(self.screen, self.color, (self.posX, self.posY, self.width, self.height))