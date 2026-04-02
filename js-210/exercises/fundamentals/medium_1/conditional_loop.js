/*
The following program is expected to log each number between 0 and 9 (inclusive) that is a multiple of 3.
Read through the code shown below. Will it produce the expected result? Why or why not?
*/

let i = 0;
while (i < 10) {
  if (i % 3 === 0) {
    console.log(i);
  } else {
    i += 1;
  }
}

/*
No, this won't work. We've put the increment logic under an else block, meaning that the first time we
run this, when i = 0, the if condition will be true as 0 % 3 === 0, we'll print 0, and then we'll keep running
the loop infinitely while printing 0. We'll never end up incrementing `i` as intended.
*/