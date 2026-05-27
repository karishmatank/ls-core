/*
Build a tic-tac-toe game.

Rules:
- 2 player game (human, computer)
- The board is a 3x3 grid
- Players take turn marking squares
- The first player to mark 3 squares together wins:
  - In a row
  - In a column
  - Diagonal
- The first player uses X, the second uses O

*/

const readline = require("readline-sync");

const EMPTY_MARKER = ' ';
const PLAYER_MARKER = 'X';
const COMPUTER_MARKER = 'O';

class Square {
  #marker;

  constructor() {
    this.mark = EMPTY_MARKER;
  }

  get mark() {
    return this.#marker;
  }

  set mark(newMarker) {
    this.#marker = newMarker;
  }

  isEmpty() {
    return this.mark === EMPTY_MARKER;
  }
}

class Board {
  constructor() {
    this.squares = {};
    for (let idx = 1; idx < 10; idx += 1) {
      this.squares[idx] = new Square();
    }
  }

  display() {
    console.log();
    console.log("     |     |");
    console.log(`  ${this.squares[1].mark}  |` +
                `  ${this.squares[2].mark}  |` +
                `  ${this.squares[3].mark}`);
    console.log("     |     |");
    console.log("-----+-----+-----");
    console.log("     |     |");
    console.log(`  ${this.squares[4].mark}  |` +
                `  ${this.squares[5].mark}  |` +
                `  ${this.squares[6].mark}`);
    console.log("     |     |");
    console.log("-----+-----+-----");
    console.log("     |     |");
    console.log(`  ${this.squares[7].mark}  |` +
                `  ${this.squares[8].mark}  |` +
                `  ${this.squares[9].mark}`);
    console.log("     |     |");
    console.log();
  }

  markOccupied(squareNumber, marker) {
    this.squares[squareNumber].mark = marker;
  }

  isBoardFull() {
    let squares = Object.values(this.squares);
    return !squares.some(square => square.isEmpty());
  }

  countMarkersFor(player, keys) {
    let count = 0;
    for (let key of keys) {
      count += (this.squares[key].mark === player.marker);
    }
    return count;
  }

  unusedSquareIndices() {
    return Object.keys(this.squares).filter(key => this.squares[key].isEmpty());
  }
}

class Player {
  constructor(marker) {
    this.marker = marker;
  }
}

class Human extends Player {
  constructor() {
    super(PLAYER_MARKER);
  }

  chooseMove(availableMoves) {
    let availableStr = availableMoves.join(', ');
    let choice;

    while (true) {
      choice = readline.question(`Choose a square (${availableStr}): `);
      if (availableMoves.includes(choice)) {
        break;
      }
      console.log("Sorry, that's not a valid choice.\n");
    }

    return choice;
  }
}

class Computer extends Player {
  constructor() {
    super(COMPUTER_MARKER);
  }

  chooseMove(availableMoves) {
    let maxIdx = availableMoves.length;
    let chosenIdx = Math.floor(Math.random() * maxIdx);
    return availableMoves[chosenIdx];
  }
}

class Game {
  static POSSIBLE_WINNING_ROWS = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
      [1, 4, 7],
      [2, 5, 8],
      [3, 6, 9],
      [1, 5, 9],
      [3, 5, 7],
  ];

  constructor() {
    this.board = new Board();
    this.human = new Human();
    this.computer = new Computer();
  }

  static displayWelcomeMessage() {
    console.log("Welcome to Tic Tac Toe!\n");
  }

  static displayGoodbyeMessage() {
    console.log("Thanks for playing Tic Tac Toe! Goodbye!\n");
  }

  getAvailableMoves() {
    return this.board.unusedSquareIndices();
  }

  recordMove(choice, marker) {
    this.board.markOccupied(choice, marker);
  }

  isGameOver() {
    return this.board.isBoardFull() || this.someoneWon();
  }

  someoneWon() {
    return this.isWinner(this.human) || this.isWinner(this.computer);
  }

  isWinner(player) {
    for (let combo of Game.POSSIBLE_WINNING_ROWS) {
      if (this.threeInARow(player, combo)) {
        return true;
      }
    }
    return false;
  }

  threeInARow(player, row) {
    return this.board.countMarkersFor(player, row) == 3;
  }

  humanTurn() {
    this.recordMove(this.human.chooseMove(this.getAvailableMoves()), this.human.marker);
  }

  computerTurn() {
    this.recordMove(this.computer.chooseMove(this.getAvailableMoves()), this.computer.marker);
  }

  displayResults() {
    if (this.isWinner(this.human)) {
      console.log("You won! Congratulations!");
    } else if (this.isWinner(this.computer)) {
      console.log("I won! I won! Take that, human!");
    } else {
      console.log("A tie game. How boring.");
    }
  }

  play() {
    Game.displayWelcomeMessage();
    this.board.display();

    while (true) {
      // Human moves
      this.humanTurn();
      if (this.isGameOver()) {
        break;
      }

      // Computer moves
      this.computerTurn();
      if (this.isGameOver()) {
        break;
      }

      this.board.display();
    }

    this.board.display();
    this.displayResults();
    Game.displayGoodbyeMessage();
  }
}

let game = new Game();
game.play();