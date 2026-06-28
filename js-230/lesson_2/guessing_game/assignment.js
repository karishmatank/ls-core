/*
This assignment aims to create a guessing game that asks the player to guess an integer between 1 and 100 chosen by the computer.
The program first picks a value using a random number generator.
The player then enters her guess and submits it, and the program checks whether the guess is
higher, lower, or equal to the computer's chosen number and reports the result.
The player may continue to play until she guesses the number.
*/

/*
Steps:

1)
Create an event listener that will run when the document's DOMContentLoaded event fires.
In the subsequent steps, you'll add code to this event listener so that it will run when the page finishes loading.

2)
Create a local variable named answer in the DOMContentLoaded listener.
Its value should be a randomly generated integer between 1 and 100, inclusive.

3)
Add an event listener that will run when the user submits the form.
It should retrieve the value from the input text field and convert it to a number with parseInt.
Store the number in a local variable named guess.

The browser shouldn't send the form content to the server; you can prevent it from doing that with preventDefault.
If you send the data, the page will refresh after each submission, and you'll lose everything!

4)
Create a local variable named message.
We will use message in subsequent problems to store a message that we will show to the user.

5)
Check whether the guess is higher than the answer.
If it is, set the message variable to a message that says the answer is lower than the guess.

6)
Update the code so that it sets message to an appropriate value
when the answer is higher than the guess and another message when it is correct.

7)
Display the message determined by problems 5 and 6 on the page.
Find the message element on the page with querySelector and set its textContent property to the value of message.

8)
Add an event listener that fires when the user clicks the "New game" link.

9)
In the event listener for a new game, change the answer to a new random number from 1 to 100,
and set the message shown to the user to one that asks the player to guess a number.
Remember to prevent the default behavior that occurs when we click on a link.

10)
Try on your own to figure out what steps need to be taken to count the number of guesses and
display it once the user has guessed correctly. Make sure that the counter is reset when starting a new game.

11)
Bonus Question If you want an extra challenge, add the following features:

- Check whether the input value is a valid integer; display an appropriate message if it is not.
- Disable the Guess button once the user guesses the number.
  (You may need to use MDN to determine how to do this.) When you disable the box,
  it should change to a dimmer color (your choice) and take on a flatter appearance (use the box-shadow property).
*/

document.addEventListener('DOMContentLoaded', () => {
  let answer;
  let numGuesses;

  let form = document.querySelector('form');
  let input = document.getElementById('guess');
  let messageElement = document.querySelector('p');
  let inputSubmitElement = document.querySelector('input[type="submit"]');

  function startNewGame() {
    answer = Math.floor(Math.random() * 100) + 1;
    numGuesses = 0;
    messageElement.textContent = 'Guess a number from 1 to 100';
    inputSubmitElement.disabled = false;
  }

  function isValidGuess(guess) {
    if (Number.isNaN(guess)) {
      messageElement.textContent = 'Please insert a valid integer from 1 to 100.';
      return false;
    }
    return true;
  }

  startNewGame();

  form.addEventListener('submit', (event) => {
    event.preventDefault();

    let guess = parseInt(input.value, 10);
    if (isValidGuess(guess)) {
      numGuesses += 1;
      let message;

      if (guess > answer) {
        message = `The answer is lower than ${guess}.`;
      } else if (guess < answer) {
        message = `The answer is higher than ${guess}.`;
      } else {
        message = `Correct! It took you ${numGuesses} guess${numGuesses > 1 ? 'es' : ''}.`;
        inputSubmitElement.disabled = true;
      }

      messageElement.textContent = message;
    }

  });

  let newGameLink = document.querySelector('a');
  newGameLink.addEventListener('click', (event) => {
    event.preventDefault();
    startNewGame();
  })
});