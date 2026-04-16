/*
Write a function named myOwnEvery that's similar to the Array.prototype.every method.
It should take an array and a function as arguments,
and return true if every element passed to the function evaluates as truthy.
*/

function myOwnEvery(array, func) {
  for (let idx = 0; idx < array.length; idx += 1) {
    if (!func(array[idx])) return false;
  }
  return true;
}

let isAString = value => typeof value === 'string';
console.log(myOwnEvery(['a', 'a234', '1abc'], isAString));       // true
console.log(myOwnEvery([1, 'a234', '1abc'], isAString));

/*
EDIT- Don't use forEach here, it won't work. This was the original form of my answer:
function myOwnEvery(array, func) {
  array.forEach(element => {
    if (!func(element)) return false;
  });
  return true;
}

This only returns false from the arrow function that we pass into forEach. It doesn't stop
forEach from iterating through each element and it doesn't actually return false
from the `myOwnEvery` function itself.
*/