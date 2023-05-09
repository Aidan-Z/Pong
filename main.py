from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
import time


s = Screen()
s.title("PONG")
s.setup(width=800, height=600)
s.bgcolor('black')
s.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
b = Ball()

r_score = ScoreBoard()
l_score = ScoreBoard()
line = ScoreBoard()

s.listen()
s.onkey(r_paddle.up, "Up")
s.onkey(r_paddle.down, "Down")
s.onkey(l_paddle.up, "w")
s.onkey(l_paddle.down, "s")


r_paddle.generate_paddle()
l_paddle.generate_paddle()


def main():
    game_on = True
    # line.line()
    while game_on:
        time.sleep(b.ball_speed) #build dificulty setting
        s.update()
        b.move()
        l_score.score_l()
        r_score.score_r()
        if b.ycor() > 280 or b.ycor() < -280:
            b.bounce()


        if b.xcor() > 335 and b.distance(r_paddle) < 50:
            b.pad_hit()
        if b.xcor() == -330 and b.distance(l_paddle) < 50:
            b.pad_hit()
        if b.xcor() > 380:
            b.reset_b()
            l_score.add_score_l()
        if b.xcor() < -380:
            b.reset_b()
            r_score.add_score_r()







    s.exitonclick()

if __name__ == '__main__':
    main()