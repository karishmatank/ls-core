import random

class GuessingGame:
    def __init__(self):
        self.min_guess = 1
        self.max_guess = 100
        self.max_num_guesses = 7
    
    def _initialize_game(self):
        self._answer = random.randint(self.min_guess, self.max_guess)
        self._guesses_remaining = self.max_num_guesses
    
    def _validate_guess(self, guess):
        try:
            guess = int(guess)
        except ValueError:
            return None
        
        if guess < self.min_guess or guess > self.max_guess:
            return None
        return guess
    
    def _get_guess(self):
        while True:
            guess = input(f"Enter a number between {self.min_guess} " +  
                          f"and {self.max_guess}: ")
            guess = self._validate_guess(guess)
            if guess:
                break
            print("Invalid guess. ", end="")
        return guess
    
    def _is_guess_correct(self, guess):
        return guess == self._answer
    
    def _display_guidance(self, guess):
        if guess < self._answer:
            print("Your guess is too low.")
        elif guess > self._answer:
            print("Your guess is too high.")
        else:
            print("That's the number!\n")
            print("You won!")
        print()
    
    def _display_guesses_remaining(self):
        print(f"You have {self._guesses_remaining} guesses remaining.")
        
    def play(self):
        self._initialize_game()
        while self._guesses_remaining > 0:
            self._display_guesses_remaining()
            guess = self._get_guess()
            self._display_guidance(guess)
            if self._is_guess_correct(guess):
                return
            self._guesses_remaining -= 1
        print("You have no more guesses. You lost!")

game = GuessingGame()
game.play()