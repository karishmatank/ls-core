/*
In this exercise, you will implement your own version of the Array.prototype.reverse method.
Your implementation should differ from the built-in method in the following two ways:

It should accept either a string or an array as an argument.
It should return a new string or array.
*/

function reverse(inputForReversal) {
  let result;
  if (Array.isArray(inputForReversal)) {
    result = [];
    for (let idx = inputForReversal.length - 1; idx >= 0; idx -= 1) {
      result.push(inputForReversal[idx]);
    }
  } else if (typeof inputForReversal === 'string') {
    result = '';
    for (let idx = inputForReversal.length - 1; idx >= 0; idx -= 1) {
      result += inputForReversal[idx];
    }
  } else {
    return undefined;
  }

  return result;

}

console.log(reverse('Hello'));           // "olleH"
console.log(reverse('a'));               // "a"
console.log(reverse([1, 2, 3, 4]));      // [4, 3, 2, 1]
console.log(reverse([]));                // []

const array = [1, 2, 3];
console.log(reverse(array));             // [3, 2, 1]
console.log(array);                      // [1, 2, 3]