from turtle import Turtle

with open("data.txt") as f:
    highscore_data = f.read()

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = highscore_data
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears previous score and writes updated score."""
        self.clear()  # Remove old score
        self.write(f"Scoreboard: {self.score} "f"Highscore: {self.highscore}", align="center", font=("Courier", 18, "bold"))

    def increase_score(self):
        """Increases the score and updates the scoreboard."""
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > int(self.highscore):
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.highscore))
        else:
            self.score = 0
