import pygame



WIDTH, HEIGHT = 900, 500

from objects import Ball


class CollisionControl:

    def collision_ball_paddle1(self, ball,paddle1):
        if ball.posY + ball.radius > paddle1.posY and ball.posY - ball.radius < paddle1.posY + paddle1.height:
            if ball.posX - ball.radius <= paddle1.posX + paddle1.width:
                return True
        return False

    def collision_ball_paddle2(self, ball, paddle2):
        if ball.posY + ball.radius > paddle2.posY and ball.posY - ball.radius < paddle2.posY + paddle2.height:
            if ball.posX + ball.radius >= paddle2.posX + paddle2.width:
                return True
        return False


    def collision_ball_margin(self, ball):
        #top collision
        if ball.posX - ball.radius <= 0:
            return True
        # bottom collision
        if ball.posY + ball.radius >= HEIGHT:
            return True
        return False

    def check_for_player1_goal(self, ball):
        return ball.posX  - ball.radius >= WIDTH

    def check_for_player2_goal(self, ball):
        return ball.posY + ball.radius <=0
