import pygame


WHITE = (255, 255, 255)


class Score:
    def __init__(self, screen, points, posY, posX):
        self.screen = screen
        self.points = points
        self.posY = posY
        self.posX = posX
        self.font = pygame.font.SysFont("monospace", 80, bold=True)
        self.label = self.font.render(self.points, 0, WHITE)
        self.showScore()

    def showScore(self):
        self.screen.blit(self.label, (self.posX - self.label.get_rect().width//2, self.posY))


    def increase(self):
        points = int(self.points) + 1
        self.points = str(points)
        self.label = self.font.rende(self.points, 0, WHITE)