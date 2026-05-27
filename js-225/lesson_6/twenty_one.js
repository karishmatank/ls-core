const shuffle = require('shuffle-array');
const rlSync = require('readline-sync');
const MAX_HAND_VALUE = 21;

class Card {
  static MAX_ACE_VALUE = 11;
  static MIN_ACE_VALUE = 1;
  static NAMED_CARD_VALUES = {
    'K': 10,
    'Q': 10,
    'J': 10,
    'A': Card.MAX_ACE_VALUE,
  };

  #rank;
  #suit;

  constructor(rank, suit) {
    this.rank = rank;
    this.suit = suit;
  }

  get rank() {
    return this.#rank;
  }

  set rank(rank) {
    this.#rank = rank;
  }

  get suit() {
    return this.#suit;
  }

  set suit(suit) {
    this.#suit = suit;
  }

  info() {
    return `${this.rank} of ${this.suit}`;
  }

  value() {
    if (Number.isNaN(Number(this.rank))) {
      return Card.NAMED_CARD_VALUES[this.rank];
    }
    return Number(this.rank);
  }
}

class Deck {
  static SUITS = ['Spades', 'Hearts', 'Clubs', 'Diamonds'];
  static RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'];

  constructor() {
    this.reset();
  }

  reset() {
    this.cards = [];

    Deck.SUITS.forEach(suit => {
      Deck.RANKS.forEach(rank => {
        this.cards.push(new Card(rank, suit));
      });
    });

    shuffle(this.cards);
  }

  deal(numCards) {
    let cards = [];
    for (let i = 0; i < numCards; i += 1) {
      cards.push(this.cards.pop());
    }
    return cards;
  }
}

class Player {
  #balance;

  constructor() {
    this.#balance = 5;
    this.hand = [];
  }

  get balance() {
    return this.#balance;
  }

  incrementBalance() {
    this.#balance += 1;
  }

  decrementBalance() {
    this.#balance -= 1;
  }

  makeChoice() {
    let choice;
    while (true) {
      choice = rlSync.question("Player choose - 'hit' or 'stay': ").toLowerCase().trim();
      let possibleChoices = ['hit', 'stay'];
      if (possibleChoices.includes(choice)) {
        break;
      }
      console.log("Hmm, that's not a valid option, try again!");
    }
    return choice;
  }
}

class Dealer {
  static HIT_THRESHOLD = 17;

  constructor() {
    this.hand = [];
    this.hideCards = true;
  }


}

let Hand = {
  getNumAces() {
    return this.hand.filter(card => card.rank === 'A').length;
  },
  reset() {
    this.hand = [];
  },
  value() {
    let sum = this.hand.reduce((acc, card) => {
      return acc + card.value();
    }, 0);

    for (let i = 0; i < this.getNumAces(); i += 1) {
      if (sum > MAX_HAND_VALUE) {
        sum -= (Card.MAX_ACE_VALUE - Card.MIN_ACE_VALUE);
      } else {
        break;
      }
    }
    return sum;
  },
  hit(cards) {
    this.hand = this.hand.concat(cards);
  },
  stay() {
    console.log(`${this.constructor.name} chose to stay!`);
  },
  isBusted() {
    return this.value() > MAX_HAND_VALUE;
  },
  displayValue() {
    console.log(`${this.constructor.name}'s hand value is ${this.value()}`);
  },
  showHand() {
    if (this.hideCards) {
      console.log(`${this.constructor.name}'s cards are: ${this.hand[0].info()} and unknown card`);
    } else {
      console.log(`${this.constructor.name}'s cards are: ${this.hand.map(card => card.info()).join(', ')}`);
    }
  }
};

Object.assign(Player.prototype, Hand);
Object.assign(Dealer.prototype, Hand);

class TwentyOneGame {
  constructor() {
    this.deck = new Deck();
    this.player = new Player();
    this.dealer = new Dealer();
  }

  static displayWelcomeMessage() {
    console.log("Welcome to Twenty-One!");
  }

  static displayGoodbyeMessage() {
    console.log("Thanks for playing Twenty-One!");
  }

  play() {
    TwentyOneGame.displayWelcomeMessage();

    while (true) {
      this.#playOneGame();
      this.#displayBalance();
      if (this.player.balance <= 0) {
        console.log("You are broke!");
        break;
      }

      if (this.player.balance >= 10) {
        console.log("You are rich!");
        break;
      }

      if (!this.#isContinuing()) {
        break;
      }
    }

    TwentyOneGame.displayGoodbyeMessage();

  }

  #playOneGame() {
    this.#reset();

    this.dealCards();
    this.player.showHand();

    this.playerTurn();
    if (!this.player.isBusted()) {
      this.dealer.hideCards = false;
      this.dealerTurn();
    }

    console.log();

    let winner = this.#determineWinner();
    if (winner) {
      this.adjustPlayerBalance(winner);
    }

    this.#displayBustedResult();
    this.displayResult(winner);

  }

  #reset() {
    this.player.reset();
    this.dealer.reset();
    this.deck.reset();
  }

  dealCards() {
    this.player.hit(this.deck.deal(2));
    this.dealer.hit(this.deck.deal(2));
  }

  playerTurn() {
    while (true) {
      let choice = this.player.makeChoice();
      if (choice === 'stay') {
        this.player.stay();
        break;
      }

      this.player.hit(this.deck.deal(1));
      this.player.showHand();
      this.player.displayValue();

      if (this.player.isBusted()) {
        break;
      }
    }
  }

  dealerTurn() {
    while (this.dealer.value() < Dealer.HIT_THRESHOLD) {
      console.log('Dealer will hit.');
      this.dealer.hit(this.deck.deal(1));
      this.dealer.showHand();
      this.dealer.displayValue();
    }
  }

  #determineWinner() {
    if (this.player.isBusted()) {
      return this.dealer;
    }
    if (this.dealer.isBusted()) {
      return this.player;
    }

    if (this.dealer.value() > this.player.value()) {
      return this.dealer;
    } else if (this.player.value() > this.dealer.value()) {
      return this.player;
    } else {
      return null;
    }
  }

  adjustPlayerBalance(winner) {
    if (winner === this.player) {
      this.player.incrementBalance();
    } else {
      this.player.decrementBalance();
    }
  }

  #displayBustedResult() {
    if (this.player.isBusted()) {
      console.log("You busted :/ Dealer wins!");
    } else if (this.dealer.isBusted()) {
      console.log("Dealer busted, you win!");
    }
  }

  displayResult(winner) {
    this.player.showHand();
    this.dealer.showHand();
    if (winner === this.player) {
      console.log("You win!");
    } else if (winner === this.dealer) {
      console.log("Dealer wins!")
    } else {
      console.log("It was a tie.");
    }
  }

  #displayBalance() {
    console.log(`Your balance is ${this.player.balance}`);
  }

  #isContinuing() {
    let playAgain;
    while (true) {
      let options = ['y', 'n'];
      playAgain = rlSync.question("Play again? (y/n): ").toLowerCase().trim();
      if (options.includes(playAgain)) {
        break;
      }
      console.log("Hmm, that's not a valid response. y/n only.");
    }

    return playAgain === 'y';
  }
}

let game = new TwentyOneGame();
game.play();