import pygame, sys

from objects.Ball import Ball

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

ball = Ball(screen, WHITE, WIDTH//2, HEIGHT // 2, 8)

#main loop

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

