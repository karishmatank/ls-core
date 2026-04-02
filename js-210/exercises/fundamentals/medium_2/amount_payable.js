/*
What does the following code log? Why is this so?
*/

let startingBalance = 1;
const chicken = 5;
const chickenQuantity = 7;

function totalPayable(item, quantity) {
  return startingBalance + (item * quantity);
}

startingBalance = 5;
console.log(totalPayable(chicken, chickenQuantity));

startingBalance = 10;
console.log(totalPayable(chicken, chickenQuantity));

/*
This will print:
40
45

When we call `totalPayable` the first time, `startingBalance` has a value of 5 in the global scope.
We pass in `chicken` and `chickenQuantity`, which behaves more like "pass by value" here because `chicken`
and `chickenQuantity` have immutable values.
Within `totalPayable`, there is no local `startingBalance` value, so JS will look into the global scope and find
that `startingBalance` has a value of 5. 5 + (5 * 7) = 40.

When we call `totalPayable` the second time, we've reassigned `startingBalance` to the value 10
and thus reference 10 within `totalPayable`. Therefore, the second time, we'll print 45.

EDIT- Can mention "closures" in the explanation too.
*/