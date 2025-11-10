import random
import os

def clear_screen():
    os.system('clear')

class Square:
    INITIAL_MARKER = " "
    HUMAN_MARKER = "X"
    COMPUTER_MARKER = "O"

    def __init__(self, marker=INITIAL_MARKER):
        self._marker = marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, marker):
        self._marker = marker

    def __str__(self):
        return self.marker

    def is_unused(self):
        return self.marker == Square.INITIAL_MARKER

class Board:
    CENTER_KEY = 5

    def __init__(self):
        self.initialize()

    def display(self):
        print()
        print("     |     |")
        print(f"  {self.squares[1]}  |"
              f"  {self.squares[2]}  |"
              f"  {self.squares[3]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[4]}  |"
              f"  {self.squares[5]}  |"
              f"  {self.squares[6]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[7]}  |"
              f"  {self.squares[8]}  |"
              f"  {self.squares[9]}")
        print("     |     |")
        print()

    def mark_square_at(self, choice, marker):
        self.squares[choice].marker = marker

    def unused_squares(self):
        return [key for key, square in self.squares.items() if square.is_unused()]

    def is_full(self):
        return len(self.unused_squares()) == 0

    def count_markers_for(self, player, keys):
        markers = [self.squares[key].marker for key in keys]
        return markers.count(player.marker)

    def count_empty_markers(self, keys):
        markers = [self.squares[key] for key in keys if self.squares[key].is_unused()]
        return len(markers)

    def display_with_clear(self):
        clear_screen()
        print("\n")
        self.display()

    def initialize(self):
        self.squares = {key: Square() for key in range(1, 10)}

    def reset(self):
        self.initialize()
        clear_screen()

    def get_opportunity_key(self, combo):
        for key in combo:
            if self.squares[key].is_unused():
                return key

    def is_center_available(self):
        return self.squares[Board.CENTER_KEY].is_unused()

class Player:
    def __init__(self, marker):
        self.marker = marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, value):
        self._marker = value

class Human(Player):
    def __init__(self):
        super().__init__(Square.HUMAN_MARKER)

class Computer(Player):
    def __init__(self):
        super().__init__(Square.COMPUTER_MARKER)

class TTTGame:
    POSSIBLE_WINNING_ROWS = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7),
    )
    WINNING_SCORE = 3

    def __init__(self):
        self.board = Board()
        self.human = Human()
        self.computer = Computer()
        self.human_score = 0
        self.computer_score = 0
        self._is_human_first = True

    @staticmethod
    def _display_welcome_message():
        clear_screen()
        print("Welcome to Tic Tac Toe!")
        print()

    @staticmethod
    def _display_goodbye_message():
        print("Thanks for playing Tic Tac Toe! Goodbye!")

    @staticmethod
    def _join_or(lst, delimiter=", ", before_last_element="or"):
        string_output = ""
        before_last_element += " "

        if len(lst) == 1:
            return str(lst[0])
        if len(lst) == 2:
            string_output = f"{lst[0]} {before_last_element} {lst[1]}"
        else:
            for idx, element in enumerate(lst):
                string_output += str(element)
                if idx != len(lst) - 1:
                    string_output += delimiter
                if idx == len(lst) - 2:
                    string_output += before_last_element

        return string_output
    
    def _display_round_results(self):
        if self._is_winner(self.human):
            print("You won this round!")
        elif self._is_winner(self.computer):
            print("Computer won this round!")
        else:
            print("A tie game. How boring.")

    def _display_results(self):
        if self._is_winner(self.human):
            print("You won! Congratulations!")
        elif self._is_winner(self.computer):
            print("I won! I won! Take that, human!")

    def _increment_score(self):
        if self._is_winner(self.human):
            self.human_score += 1
        elif self._is_winner(self.computer):
            self.computer_score += 1

    def _display_score(self):
        print(f"Your score is {self.human_score}.")
        print(f"Computer's score is {self.computer_score}.")

    def _human_moves(self):
        valid_choices = self.board.unused_squares()
        choices_list = [str(choice) for choice in valid_choices]
        choices_str =  self._join_or(choices_list)

        while True:
            choice = input(f"Choose a square ({choices_str}): ")
            try:
                choice = int(choice)
                if choice in valid_choices:
                    break
            except ValueError:
                pass

            print("Sorry, that's not a valid choice.")
            print()

        self.board.mark_square_at(choice, self.human.marker)

    def _is_game_over(self):
        return self.board.is_full() or self._someone_won()

    def _is_winner(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self._three_in_a_row(player, row):
                return True

        return False

    def _three_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row) == 3

    def _someone_won(self):
        return self._is_winner(self.human) or self._is_winner(self.computer)

    def _reset_scores(self):
        self.human_score = 0
        self.computer_score = 0

    def _detect_opportunity_or_threat(self):
        for combo in TTTGame.POSSIBLE_WINNING_ROWS:
            human_count = self.board.count_markers_for(self.human, combo)
            computer_count = self.board.count_markers_for(self.computer, combo)
            empty_count = self.board.count_empty_markers(combo)

            if ((human_count == 2 and empty_count == 1) or
                (computer_count == 2 and empty_count == 1)):
                return self.board.get_opportunity_key(combo)
        return None

    def _is_opportunity_or_threat(self):
        return self._detect_opportunity_or_threat() is not None

    def _computer_moves(self):
        if self._is_opportunity_or_threat():
            choice = self._detect_opportunity_or_threat()
        elif self.board.is_center_available():
            choice = Board.CENTER_KEY
        else:
            valid_choices = self.board.unused_squares()
            choice = random.choice(valid_choices)

        self.board.mark_square_at(choice, self.computer.marker)

    def _play_one_round(self):
        while True:
            if self._is_human_first:
                self._human_moves()
            else:
                self._computer_moves()

            self.board.display_with_clear()
            if self._is_game_over():
                break

            if self._is_human_first:
                self._computer_moves()
            else:
                self._human_moves()

            if self._is_game_over():
                break

            self.board.display_with_clear()

    def _play_one_game(self):
        self._reset_scores()

        while (self.human_score < TTTGame.WINNING_SCORE and
               self.computer_score < TTTGame.WINNING_SCORE):
            self.board.initialize()
            self.board.display()

            self._play_one_round()

            self._display_round_results()
            self._increment_score()
            self._display_score()

            self._is_human_first = not self._is_human_first
        self._display_results()

    def _is_continuing(self):
        while True:
            play_again = input("Play again? (y/n): ").lower().strip()
            if play_again in ['y', 'n']:
                break
            print("Hmm, that's not a valid response. y/n only.")

        return play_again == 'y'

    def play(self):
        self._display_welcome_message()

        while True:
            self._play_one_game()
            if not self._is_continuing():
                break

        self._display_goodbye_message()



game = TTTGame()
game.play()
