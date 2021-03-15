from Field import Field
import random

class Computer:
    def __init__(self, symbol: str):
        self.symbol = symbol
    
    def move(self, field: Field):
        while True:
            row = random.randint(0, 2)
            column = random.randint(0, 2)

            if field.field[row][column] == " ":
                field.field[row][column] = self.symbol
                return field.field    
        