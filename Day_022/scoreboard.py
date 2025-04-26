from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", align="center", font=("Courier", 20, "bold"))
        self.goto(100, 200)
        self.write(f"{self.r_score}", align="center", font=("Courier", 20, "bold"))


    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Increases the score and updates the scoreboard."""
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align="center", font=("Courier", 18, "bold"))
