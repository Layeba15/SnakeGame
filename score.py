from turtle import Turtle
ALIGN = "center"
FONT = ("courier", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        with open("high_score.txt", mode="r") as file:
            h_score = file.read()
            if int(h_score) > int(self.high_score):
                self.high_score = h_score
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def increase(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
