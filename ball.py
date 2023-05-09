from turtle import Turtle
# import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def reset_b(self):
        self.home()
        self.x_move *= -1
        self.ball_speed = 0.1
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1 #reverse

    def pad_hit(self):
        self.x_move *= -1
        self.ball_speed *= 0.9











