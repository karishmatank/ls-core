/*
We love to visit museums if they are about science or computers.
We're undecided when it comes to modern art, and would rather not go in most cases.
However, we're willing to go to any modern art museum that is about Andy Warhol (we like him!)
or that is located in nearby Amsterdam. We'd rather skip any other museums.

We tried to implement these preferences in a function, so we can automatically sort through
long lists of museums and find the ones that sound interesting.
However, our Boolean check is flawed, as it fails some of our test cases. Can you fix it?
*/

function wantToVisit(museum, city) {
  return museum.includes('Computer')
      || museum.includes('Science')
      && !(
        museum.includes('Modern')
        && museum.includes('Art')
        && museum.includes('Andy Warhol')
        || city === 'Amsterdam'
      );
}

// Tests (should all print 'true')

console.log(wantToVisit('Computer Games Museum', 'Berlin') === true);
console.log(wantToVisit('National Museum of Nature and Science', 'Tokyo') === true);
console.log(wantToVisit('Museum of Modern Art', 'New York') === false);
console.log(wantToVisit('El Paso Museum of Archaeology', 'El Paso') === false);
console.log(wantToVisit('NEMO Science Museum', 'Amsterdam') === true); // X
console.log(wantToVisit('National Museum of Modern Art', 'Paris') === false);
console.log(wantToVisit('Andy Warhol Museum of Modern Art', 'Medzilaborce') === true); // X
console.log(wantToVisit('Moco: Modern Contemporary Art', 'Amsterdam') === true); // X
console.log(wantToVisit('Van Gogh Museum', 'Amsterdam') === false);
console.log(wantToVisit('Andy Warhol Museum', 'Melbourne') === false);


/*
I've tried to reformat the logic by using parenthesis based on the order of priority:

museum.includes('Computer') ||
(
  museum.includes('Science') && !(
      (museum.includes('Modern') && museum.includes('Art') && museum.includes('Andy Warhol')) || city === 'Amsterdam'
  )
)

The issue is how the logic after the first || is structured. && has priority over ||, which means
the right operand to the first || is the entirety of the rest of the logic.
In addition, the && bind more tightly inside the negated block, which causes issues
with NEMO Science Museum, where we return false because we negate the reuslt essentially from city === 'Amsterdam'
to return false.
This is also an issue for 'Andy Warhol Museum of Modern Art', where we would be interested in that
museum, but it will short circuit to false because the museum doesn't include the word 'Science'.
Similar story with 'Moco: Modern Contemporary Art'

This is obviously really hard to read, so we can structure our code more cleanly as shown below:
*/

function wantToVisit(museum, city) {
  let isComputer = museum.includes('Computer');
  let isScience = museum.includes('Science');
  let isModernArt = museum.includes('Modern') && museum.includes('Art');
  let isInterestingArt = isModernArt && (museum.includes('Andy Warhol') || city === 'Amsterdam');

  return isComputer || isScience || isInterestingArt;
}