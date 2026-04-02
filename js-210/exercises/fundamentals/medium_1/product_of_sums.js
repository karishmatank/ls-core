/*
The productOfSums function shown below is expected to return the product of the sums of two arrays of numbers.
Read through the following code. Will it produce the expected result? Why or why not?
*/

function productOfSums(array1, array2) {
  let result = total(array1) * total(array2);
  return result;
}

function total(numbers) {
  let sum;

  for (let i = 0; i < numbers.length; i += 1) {
    sum += numbers[i];
  }

  sum;
}

/*
No, this won't produce the expected result. We aren't actually returning the sum from `total`,
so `total(array1)` and `total(array2)` will both result in `undefined`. We then have `undefined * undefined`,
which results in `NaN`.

EDIT- Missed the second issue, which is that within `total`, we never initialize `sum` to anything.
It doesn't start at 0, it essentially starts at undefined. (Note that `sum` is only in the TDZ if we try to access it
before it has been declared, such as if we had `sum += numbers[i]` before we saw `let sum`.
This is why `sum` has the value `undefined` by the time we enter into the for loop.)
*/
