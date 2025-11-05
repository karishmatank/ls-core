"""
Rock Paper Scissors is a two-player game where each player chooses one of three possible moves: rock, paper, or scissors.
The chosen moves will then be compared to see who wins, according to the following rules:
    - Rock beats scissors (rock crushes scissors)
    - Scissors beats paper (scissors cut paper)
    - Paper beats rock (paper wraps rock)

If the players choose the same move, then it's a tie.

Nouns: player, move, rule
Verbs: choose, compare

Player
    - choose
Move
Rule

    - compare

"""
import random
    

class Move:
    CHOICES = ('rock', 'paper', 'scissors', 'lizard', 'spock')
    USER_WIN_SCENARIOS = {
        # User wins with following user choice: computer choice scenarios
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["paper", "spock"],
        "spock": ["rock", "scissors"]
    }

    def __init__(self, choice):
        self.choice = choice
    
    def __gt__(self, other):
        """Greater than means self's choice wins against other's choice"""
        if not isinstance(other, Move):
            return NotImplemented
        
        return other.choice in Move.USER_WIN_SCENARIOS.get(self.choice)
    
    def __eq__(self, other):
        if not isinstance(other, Move):
            return NotImplemented

        return self.choice == other.choice
    
    def __str__(self):
        return self.choice


class Player:
    def __init__(self):
        self.move = None
        self.score = 0
    
    def increment_score(self):
        self.score += 1


class Human(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        while True:
            choice = input(f"Choose one: {", ".join(Move.CHOICES)}: ").lower().strip()
            if choice in Move.CHOICES:
                break
            print("Hmm, that's not a valid choice, please choose again!")
        self.move = Move(choice)


class Computer(Player):
    def __init__(self):
        super().__init__()

    def choose(self, human_last_move=None):
        choice = random.choice(Move.CHOICES)
        self.move = Move(choice)


class R2D2(Computer):
    def choose(self, human_last_move=None):
        self.move = Move("rock")


class HAL(Computer):
    def choose(self, human_last_move=None):
        choices = Move.CHOICES + ('scissors', 'scissors', 'scissors')
        choice = random.choice(choices)
        self.move = Move(choice)
    

class Daneel(Computer):
    def choose(self, human_last_move=None):
        if human_last_move:
            self.move = Move(human_last_move)
        else:
            choice = random.choice(Move.CHOICES)
            self.move = Move(choice)


class RPSGame:
    MAX_SCORE = 5

    def __init__(self):
        self._human = Human()
        self._computer = Daneel()
        self._human_moves = []
        self._computer_moves = []

    @staticmethod
    def _display_welcome_message():
        print("Welcome to Rock Paper Scissors!")

    @staticmethod
    def _display_goodbye_message():
        print("Thanks for playing Rock Paper Scissors. Goodbye!")
    
    def _get_winner(self):
        if self._human.move > self._computer.move:
            return self._human
        elif self._computer.move > self._human.move:
            return self._computer
        else:
            return None

    def _display_winner(self, winner):
        print(f"You chose: {self._human.move}")
        print(f"The computer chose: {self._computer.move}")

        if winner == self._human:
            print('You win!')

        elif winner == self._computer:
            print("Computer wins!")

        else:
            print("It's a tie")

    def _display_score(self):
        print(f"Your score is: {self._human.score}")
        print(f"The computer's score is: {self._computer.score}")

    def _display_prior_moves(self):
        print(f"Your last 5 moves were: {', '.join([str(move) for move in self._human_moves[-5:]])}")
        print(f"The computer's 5 moves were: {', '.join([str(move) for move in self._computer_moves[-5:]])}")

    def _display_ultimate_winner(self):
        if self._human.score == 5:
            print("You won 5 times!")
        else:
            print("The computer won 5 times!")
    
    def _play_again(self):
        answer = input("Would you like to play again? (y/n): ")
        return answer.lower().startswith('y')
    
    def _reset_game(self):
        self._human.score = 0
        self._computer.score = 0
        self._human_moves = []
        self._computer_moves = []

    def _record_moves(self):
        self._human_moves.append(self._human.move)
        self._computer_moves.append(self._computer.move)

    def play(self):
        self._display_welcome_message()
        while True:
            self._reset_game()

            while (self._human.score < RPSGame.MAX_SCORE and 
                   self._computer.score < RPSGame.MAX_SCORE):
                self._human.choose()

                try:
                    last_human_choice = self._human_moves[-1].choice
                except IndexError:
                    last_human_choice = None
                self._computer.choose(last_human_choice)
                
                self._record_moves()

                winner = self._get_winner()
                self._display_winner(winner)

                if winner:
                    winner.increment_score()
                self._display_score()

                self._display_prior_moves()
                print()

            self._display_ultimate_winner()

            if not self._play_again():
                break

        self._display_goodbye_message()

game = RPSGame()
game.play()
