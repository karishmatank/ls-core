/*
THIS PROBLEM IS HARDER THAN WHAT WE'LL SEE ON THE LS216 EXAM.

Write a function that implements the Vigenere Cipher.
The case of the keyword doesn't matter—in other words, the resulting encryption won't change depending
on the case of the keyword's letters (e.g., 'MEat' === 'mEaT').

My questions:
- Will the inputs always be two strings? Will the first always represent the text and the second the keyword?
- What happens if we receive different data types for the inputs?
- What happens if we receive more than 2 arguments or less than 2 arguments? What do we do?
- If the first arg is empty, do we return an empty string?
- If the first arg onnly has non-alpha chars, do we end up just returnign the same value?
- What happens if the keyword is an empty string?
- What happens if the keyword has non-alphabetic chars? What do we do then?


Input: string (text) and string (keyword)
Output: string (encrypted text)
Rules:
- Vigenere cipher uses the same concept as Caesar cipher to encrypt except we shift based on the letters of
  the keyword
- We keep looping through the letters of the keyword to find the next value off of which to shift a plaintext char
- The shift value is the index of the keyword letter that we are shifting by (0-25)
- The case of the keyword doesn't matter -> 'a' and 'A' both have shift value 0
- However, the case of the text does matter -> we need to retain case
- We do not shift non-alphabetic chars. We keep them as is and in the same placement as they appear in the input.
- We'll always get exactly 2 inputs as strings. Don't worry about other data types or fewer / more arguemnts
- If first arg is '', return ''
- If first arg has no alpha chars, basically end up returning the same value
- Assume keyword will be a non-empty string made up of only alphabetical chars


Data structures:
Characters of the text -> array

characters of the keyword -> array
pointer of the keyword -> number

alphabet -> string


Algorithm:

HELPER: createShiftTracker(keyword) -> closure
- Convert `keyword` to uppercase
- Set lastIdx to undefined
- Return a function:
  - If `lastIdx` is undefined:
    - Set `lastIdx` to 0
  - Otherwise, set it to `lastIdx` + 1, but wrap around back to 0 if `lastIdx` + 1 exceeds the length of `keyword`
  - Get the char of `keyword` at `lastIdx` -> `char`
  - Get the index of `char` within `ALPHABET` -> return this value

HELPER: getEncodedLetter(uppercaseLetter, shiftValue) -> string (letter)
- Get the index of `uppercaseLetter` within ALPHABET -> `current`
- Shift `current` by adding `shiftValue`, but wrap around if the result exceeds the length of `ALPHABET` -> `new`
- Get the letter in `ALPHABET` at `new` and return


HELPER: isUppercase(char) -> boolean
- Return true if char >= 'A' and <= 'Z'

HELPER: isLowercase(char) -> boolean
- Return true if char >= 'a' and <= 'z'

High-level:
- Set const ALPHABET to 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' (outside of the function)

- Split input into chars -> `chars`
- Set `transformedChars` to empty array
- Invoke `createShiftTracker` to get the tracker based on keyword -> `getShiftValue`
- For each char in `chars`:
  - If it is an uppercase letter:
    - Get the next shift value -> Invoke `getShiftValue`
    - Using the shift value, get the transformed letter of the alphabet using uppercase alphabet
      - getEncodedLetter
    - Push new letter to `transformedChars`
  - If it is a lowercase letter:
    - Convert letter to uppercase
    - Get the next shift value -> Invoke `getShiftValue`
    - Using the shift value, get the transformed letter of the alphabet using lowercase alphabet
      - getEncodedLetter
    - Convert resulting letter back to lowercase
    - Push new lowercase letter to `transformedChars`
  - Else:
    - keep the char as is, add to end of `transformedChars`
- Join `transformedChars` together into one string and return
*/

const ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

function isUppercase(char) {
  return char >= 'A' && char <= 'Z';
}

function isLowercase(char) {
  return char >= 'a' && char <= 'z';
}

function createShiftTracker(keyword) {
  keyword = keyword.toUpperCase();
  let lastIdx = undefined;
  return function() {
    if (lastIdx === undefined) {
      lastIdx = 0;
    } else {
      lastIdx = (lastIdx + 1) % keyword.length;
    }

    let char = keyword[lastIdx];
    return ALPHABET.indexOf(char);
  }
}

function getEncodedLetter(uppercaseLetter, shiftValue) {
  let current = ALPHABET.indexOf(uppercaseLetter);
  let newIdx = (current + shiftValue) % ALPHABET.length;
  return ALPHABET[newIdx];
}


function encode(text, keyword) {
  let getShiftValue = createShiftTracker(keyword);
  let chars = text.split('').map((char) => {
    if (isUppercase(char)) {
      return getEncodedLetter(char, getShiftValue());
    } else if (isLowercase(char)) {
      return getEncodedLetter(char.toUpperCase(), getShiftValue()).toLowerCase();
    } else {
      return char;
    }
  });
  return chars.join('');
}

console.log(encode("Pineapples don't go on pizzas!", 'meat') === "Bmnxmtpeqw dhz'x gh ar pbldal!");
console.log(encode("Pineapples don't go on pizzas!", 'MeAt') === "Bmnxmtpeqw dhz'x gh ar pbldal!");

console.log(encode("Pin", 'meat') === "Bmn");
console.log(encode("", 'meat') === "");
console.log(encode("$$(() *", 'meat') === "$$(() *");
console.log(encode("Hi!", 'a') === "Hi!");
console.log(encode("Hi!", 'aaa') === "Hi!");