from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0,260)
        self.score=0
        self.write_score()

    def write_score(self,):
        self.write(f"Score: {self.score}",align='center',font=('Arial',20,'normal'))

    def increase_score(self):
        self.clear()
        self.score+=1
        self.write_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!!", align='center', font=('Arial', 20, 'normal'))


