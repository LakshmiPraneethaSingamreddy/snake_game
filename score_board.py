from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0,260)
        self.score=0
        self.high_score=int(open("data.txt").read())
        self.write_score()

    def write_score(self,):
        self.clear()
        self.write(f"Score: {self.score},High Score: {self.high_score}",align='center',font=('Arial',20,'normal'))

    def increase_score(self):
        self.score+=1
        self.write_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER!!", align='center', font=('Arial', 20, 'normal'))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            open("data.txt",'w').write(str(self.high_score))
        self.score=0
        self.write_score()



