import pygame, sys

from objects.Ball import Ball
from objects.Paddle import Paddle

pygame.init()

WIDTH = 900
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def paint_screen():
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, (WIDTH//2, 0),(WIDTH//2, HEIGHT), 6)

paint_screen()


pygame.display.set_caption('Pong!')

ball = Ball(screen, WHITE, WIDTH//2, HEIGHT // 2, 16)
paddle1 = Paddle(screen, WHITE, 15, HEIGHT//2-60, 20, 120)
paddle2 = Paddle(screen, WHITE, WIDTH-20-15, HEIGHT//2-60, 20, 120)

#main loop

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

