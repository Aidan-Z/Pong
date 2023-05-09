from turtle import Turtle
POS = [(0, -280), (0, -260), (0, -240), (0, -220), (0, -200),
       (0, -180), (0, -160),]
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.speed(0)
        self.r_score = 0
        self.l_score = 0

    def line(self):
        self.goto(0, -280)
        self.right(90)
        self.shape('square')
        for i in POS:
            self.stamp()
            self.forward(20)





    def score_r(self):
        self.goto(50, 220)
        self.write(self.r_score, align='center', font=('Helvetica', 70, 'normal'))


    def score_l(self):
        self.goto(-50, 220)
        self.write(self.l_score, align='center', font=('Helvetica', 70, 'normal'))

    def add_score_r(self):
        self.clear()
        self.r_score += 1
        self.score_r()

    def add_score_l(self):
        self.clear()
        self.l_score += 1
        self.score_l()


