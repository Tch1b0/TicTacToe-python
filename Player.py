from Field import Field

class Player:
    def __init__(self, symbol: str):
        self.symbol = symbol
    
    def move(self, field: Field):
        while True:
            try:
                row = int(input("row: ")) - 1
                column = int(input("column: ")) - 1

                if field.field[row][column] == " ":
                    field.field[row][column] = self.symbol
                    return field.field
                else:
                    print("That spot is already taken!")

            except:
                print("please enter a valid number")