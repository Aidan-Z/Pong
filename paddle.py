from turtle import Turtle
LOC = [(350, 0), (-350, 0)]
class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.x = x
        self.y = y



    def generate_paddle(self):
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(self.x, self.y)



    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)