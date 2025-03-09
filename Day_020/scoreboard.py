from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears previous score and writes updated score."""
        self.clear()  # Remove old score
        self.write(f"Scoreboard: {self.score}", align="center", font=("Courier", 18, "bold"))

    def increase_score(self):
        """Increases the score and updates the scoreboard."""
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align="center", font=("Courier", 18, "bold"))
