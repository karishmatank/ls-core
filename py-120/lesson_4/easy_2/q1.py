"""
Update this code so that Bingo inherits the play method from the Game class.
"""

class Game:
    def play(self):
        return 'Start the game!'

class Bingo(Game):
    pass

bingo = Bingo()
print(bingo.play())