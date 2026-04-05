/*
The following code is a simplified (and not so serious) model of how we read a software development book.
But running this code results in a stack overflow. What is wrong?
*/

const totalPages = 364;
let energy = 100;

function read() {
  let currentPage = 1;

  while (energy > 0 && currentPage < totalPages) {
    currentPage += 1;
    energy -= (5 + currentPage * 0.1);
  }

  console.log(`Made it to page ${String(currentPage)}.`);

  // Drink a cup of coffee.
  energy = 100;

  // Continue reading.
  if (currentPage < totalPages) {
    read();
  } else {
    console.log('Done!');
  }
}

read();

/*
Every time we call the recursive `read` call on line 24, we start over at page 1.
Because the math is always the same, we'll get to the same page before our energy goes to 0
and then we'll drink coffee and start the process all over again. After drinking coffee,
we don't pick up at the page we were at before drinking coffee, we start again at page 1.
Therefore, this program essentially never ends.

We should move the `let currentPage = 1` declaration outside of the function.
*/