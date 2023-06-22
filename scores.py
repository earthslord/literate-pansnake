from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.highscore = int(data.read())
        self.penup()
        self.goto(0, 270)
        self.pencolor("white")
        self.hideturtle()
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.score}. Highscore: {self.highscore}", align='center', font=('Consolas', 20, 'bold'))

    def score_plus(self):
        self.score += 10
        self.score_update()

    def reset_sb(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt','w') as data2:
                data2.write(str(self.highscore))
        self.score = 0
        self.score_update()



    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align='center', font=('Consolas', 40, 'bold'))
