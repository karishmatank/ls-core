/*
Write two functions that each take two strings as arguments. Their expected behaviors are as follows:

- The indexOf function searches for the first instance of a substring in firstString that matches the string secondString,
and returns the index of the character where that substring begins.
- The lastIndexOf function searches for the last instance of a substring in firstString that matches the string secondString,
and returns the index of the character where that substring begins.
- Both functions return -1 if firstString does not contain the substring specified by secondString.

indexOf('Some strings', 's');                      // 5
indexOf('Blue Whale', 'Whale');                    // 5
indexOf('Blue Whale', 'Blute');                    // -1
indexOf('Blue Whale', 'leB');                      // -1

lastIndexOf('Some strings', 's');                  // 11
lastIndexOf('Blue Whale, Killer Whale', 'Whale');  // 19
lastIndexOf('Blue Whale, Killer Whale', 'all');    // -1

You may use the square brackets ([]) to access a character by index (as shown below),
and the length property to find the string length.
However, you may not use any other properties or methods from JavaScript's built-in String class.
*/

function getSubstring(string, startIdx, subLength) {
  let subString = '';
  for (let idxSubstr = startIdx; idxSubstr < startIdx + subLength; idxSubstr += 1) {
    subString += string[idxSubstr];
  }
  return subString;
}

function indexOf(firstString, secondString) {
  for (let idx = 0; idx < firstString.length - secondString.length + 1; idx += 1) {
    // Form a substring from firstString based on the length of secondString
    let subString = getSubstring(firstString, idx, secondString.length);
    if (subString === secondString) {
      return idx;
    }
  }

  return -1;
}

function lastIndexOf(firstString, secondString) {
  for (let idx = firstString.length - secondString.length; idx >= 0; idx -= 1) {
    // Form a substring from firstString based on the length of secondString
    let subString = getSubstring(firstString, idx, secondString.length);
    if (subString === secondString) {
      return idx;
    }
  }

  return -1;
}

console.log(indexOf('Some strings', 's'));                      // 5
console.log(indexOf('Blue Whale', 'Whale'));                    // 5
console.log(indexOf('Blue Whale', 'Blute'));                    // -1
console.log(indexOf('Blue Whale', 'leB'));                      // -1

console.log(lastIndexOf('Some strings', 's'));                  // 11
console.log(lastIndexOf('Blue Whale, Killer Whale', 'Whale'));  // 19
console.log(lastIndexOf('Blue Whale, Killer Whale', 'all'));    // -1
console.log(lastIndexOf('Blue Whale, Whale Killer', 'Whale'));  // 12

/*
If you haven't used it yet, implement the lastIndexOf function by reusing your indexOf function.
*/

function reverseString(string) {
  let reversed = '';
  for (let char of string) {
    reversed = char + reversed;
  }
  return reversed;
}

function lastIndexOf(firstString, secondString) {
  // Reverse each string
  firstString = reverseString(firstString);
  secondString = reverseString(secondString);

  let idx = indexOf(firstString, secondString);
  if (idx === -1) {
    return idx;
  }
  return firstString.length - idx - secondString.length;
}

/*
Another way to have solved this is to keep calling indexOf for each substring. Instead of in `indexOf`, where we
stop after the first match, still go left to right but keep looking beyond the first match. Keep track of the
highest index value that matches, then return that index.
*/