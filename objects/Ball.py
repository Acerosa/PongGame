import pygame

WIDTH, HEIGHT = 900, 500

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

    def startMoving(self):
        self.direcX = 15
        self.direcY = 5

    def moveBall(self):
        self.posX += self.direcX
        self.posY += self.direcY

    def paddle_collision(self):
        self.direcX = -self.direcX

    def margin_collision(self):
        self.direcY = -self.direcY

    def restart_ball_position(self):
        self.posX = WIDTH//3

        self.posY = HEIGHT//2

        self.showBall()

