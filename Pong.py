import pygame, sys

from objects.Ball import Ball
from objects.Paddle import Paddle
from objects.CollisionControl import CollisionControl
from objects.Score import Score

pygame.init()

WIDTH, HEIGHT = 900, 500
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def paint_screen():
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, (WIDTH//2, 0),(WIDTH//2, HEIGHT), 6)

def reset():
    paint_screen()
    score1.restart_score_()
    score2.restart_score_()
    paddle1.restart_paddle_position()
    paddle2.restart_paddle_position()

paint_screen()


pygame.display.set_caption('Pong!')

ball = Ball(screen, WHITE, WIDTH//2, HEIGHT // 2, 16)
paddle1 = Paddle(screen, WHITE, 15, HEIGHT//2-60, 20, 120)
paddle2 = Paddle(screen, WHITE, WIDTH-20-15, HEIGHT//2-60, 20, 120)
collision = CollisionControl()
score1 = Score(screen, '0', WIDTH//4, 15)
score2 = Score(screen, '0', WIDTH - WIDTH//4, 15)
#VARIABLES
playing = False
#main loop

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p and not playing:
                ball.startMoving()
                playing = True
            if event.key == pygame.K_r:
                reset()
                playing = False
            if event.key == pygame.K_w:
                paddle1.state = 'up'
            if event.key == pygame.K_s:
                paddle1.state = 'down'
            if event.key == pygame.K_UP:
                paddle2.state = 'up'
            if event.key == pygame.K_DOWN:
                paddle2.state = 'down'

        if event.type == pygame.KEYUP:
            paddle1.state = 'stopped'
            paddle2.state = 'stopped'


        if playing:
            #settng screen
            paint_screen()

            #moving ball
            ball.moveBall()

            #showing ball
            ball.showBall()


            #Paddl1
            paddle1.movePaddle()
            paddle1.clamp()
            paddle1.showPaddle()


            #Paddl2
            paddle2.movePaddle()
            paddle2.clamp()
            paddle2.showPaddle()

            #checing and setting collisions
            if collision.collision_ball_paddle1(ball, paddle1):
                ball.paddle_collision()

            if collision.collision_ball_paddle2(ball, paddle2):
                ball.margin_collision()

            if collision.collision_ball_margin(ball):
                ball.margin_collision()

            if collision.check_for_player1_goal(ball):
                paint_screen()
                score1.increase()
                ball.restart_ball_position()
                paddle1.restart_paddle_position()
                paddle2.restart_paddle_position()
                playing = False

            if collision.check_for_player2_goal(ball):
                paint_screen()
                score2.increase()
                ball.restart_ball_position()
                paddle1.restart_paddle_position()
                paddle2.restart_paddle_position()
                playing = False


        score1.showScore()
        score2.showScore()



