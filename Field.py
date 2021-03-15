from time import sleep  

class Field:
    def __init__(self):
        self.field = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

    def __str__(self):
        text = ""
        text += ("  1 2 3\n")
        text += (f"1 {self.field[0][0]}|{self.field[0][1]}|{self.field[0][2]}\n")
        text += ("  -|-|-\n")
        text += (f"2 {self.field[1][0]}|{self.field[1][1]}|{self.field[1][2]}\n")
        text += ("  -|-|-\n")
        text += (f"3 {self.field[2][0]}|{self.field[2][1]}|{self.field[2][2]}\n")
        return text

    def checkField(self):
        for i in range(0, 2):
            if self.field[i][0] == self.field[i][1] and self.field[i][1] == self.field[i][2] and self.field[i][0] != " ":
                self.endGame(winner=self.field[i][0])

            elif self.field[0][i] == self.field[1][i] and self.field[1][i] == self.field[2][i] and self.field[0][i] != " ":
                self.endGame(winner=self.field[0][i])   

        if self.field[0][0] == self.field[1][1] and self.field[1][1] == self.field[2][2] and self.field[0][0] != " ":
            self.endGame(winner=self.field[0][0])
            
        elif self.field[0][2] == self.field[1][1] and self.field[1][1] == self.field[2][0] and self.field[0][2] != " ":
            self.endGame(winner=self.field[0][2])

    def endGame(self, winner: str):
        quit(print(f"{winner} won!"))