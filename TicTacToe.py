import os
from Player import Player
from Field import Field
from Computer import Computer

clear = lambda: os.system("cls || clear")

if __name__ == '__main__':
    field = Field()
    first = Player("o")
    firstTurn = True

    while True:
        try:
            opponent = int(input("Play against...\n1: Player\n2: Computer\n"))
            if opponent == 1:
                second = Player("x")
                break
            else:
                second = Computer("x")
                break
        except:
            print("Please enter a valid number")

    while True:
        clear()
        print(field)
        field.checkField()

        if firstTurn == True:
            field.field = first.move(field)
        else:
            field.field = second.move(field)
        
        firstTurn = not firstTurn