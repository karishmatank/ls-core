/*
The penultimate function takes a string as an argument and returns the next-to-last word in the string.
The function assumes that "words" are any sequence of non-whitespace characters.
The function also assumes that the input string will always contain at least two words.
The penultimate function in the example below does not return the expected result.
Run the code below, check the current result, identify the problem, explain what the problem is,
and provide a working solution.
*/

function penultimate(string) {
  return string.split(' ')[-2];
}

console.log(penultimate('last word'));                    // expected: "last"
console.log(penultimate('Launch School is great!'));      // expected: "is"

/*
The issue is that we are trying to locate the property with key '-2'. In JS, we can't just negatively
index an array as we can do in Python. Because there is no property with key '-2', the function will
return `undefined`.

The fix is to properly index the array to find the second to last character, as shown below:
*/

function penultimateV2(string) {
  return string.split(' ').slice(-2, -1).pop();
}

console.log(penultimateV2('last word'));                    // expected: "last"
console.log(penultimateV2('Launch School is great!'));      // expected: "is"