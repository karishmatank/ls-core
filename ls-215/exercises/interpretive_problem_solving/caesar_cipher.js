/*
THIS PROBLEM IS CONSIDERED HARDER THAN THE LS216 DIFFICULTY.


Write a function that implements the Caesar Cipher. The Caesar Cipher is one of the earliest and simplest ways to encrypt plaintext so that a message can be transmitted securely. It is a substitution cipher in which each letter in a plaintext is substituted by the letter located a given number of positions away in the alphabet. For example, if the letter 'A' is right-shifted by 3 positions, it will be substituted with the letter 'D'. This shift value is often referred to as the key. The "encrypted plaintext" (ciphertext) can be decoded using this key value.

The Caesar Cipher only encrypts letters (including both lower and upper case). Any other character is left as is. The substituted letters are in the same letter case as the original letter. If the key value for shifting exceeds the length of the alphabet, it wraps around from the beginning.


My questions:
- Is this off of the English alphabet?
- Will we always receive a string and a number? What about other data types?
- Might we receive a different number of inputs than 2 (less than or greater than 2)?
- Confirm that if we receive an empty string, we should output an empty string?
- What happens if the key is negative? What do we output?
- What happens if the key is not an integer? What do we do?
- Do we have to worry about keys being NaN or Infinity / -Infinity?
- Confirm that if we receive a string with no alphabetical chars, output will match the input


Input: string, key (number)
Output: string (encrypted)
Rules:
- Caesar cipher => shift each alphabetical char of the input by the number of spaces noted by the key
  - If the shift leads us past the last letter of the alphabet, we should wrap around to the beginning of the alphabet
- Keep letters in the same case they appear in
- Only encrypt alphabetical chars
- If we receive a string with no alphabetical chars, output will match input
- This is based on the standard English alphabet
- Assume first argument always str, second always number. Exactly 2 arguemnts
- Assume key is a non-negaetive integer. Don't worry about NaN / Infinity


Data structures:
- alphabet -> string / array
- string chars -> array (?)


Algorithm:

HELPER: isUppercase(char) -> boolean
- Return true if char is >= 'A' && <= 'Z'

HELPER: isLowercase(char) -> boolean
- Return true if char is >= 'a' && <= 'Z'

HELPER: getEncryptedChar(char, key, alphabet) -> string (char)
- Get index of char in `alphabet`
- Add `key` to that index, wrapping around if we go past the length of the alphabet -> `newIndex`
- Return the letter at the `newIndex` index of `alphabet`

High-level:
- Set const ALPHABET to 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
- Split input into chars -> `chars` array
- Iterate through `chars`:
  - If the char is uppercase -> isUppercase
    - Set `alphabet` to the uppercase version of `ALPHABET`
  - If the char is lowercase -> isLowercase
    - Set `alphabet` to the lowercase version of `ALPHABET`
  - Else:
    - just keep the char as is, move on to the next char

  - Get encrypted char - `getEncryptedChar`

- Combine all results from the iteration
- Return the combined resulting string
*/

const ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

function isUppercase(char) {
  return char >= 'A' && char <= 'Z';
}

function isLowercase(char) {
  return char >= 'a' && char <= 'z';
}

function getEncryptedChar(char, key, alphabet) {
  let idx = alphabet.indexOf(char);
  let newIdx = (idx + key) % alphabet.length;
  return alphabet[newIdx];
}

function caesarEncrypt(input, key) {
  let chars = input.split('');
  return chars.map(char => {
    let alphabet;
    if (isUppercase(char)) {
      alphabet = ALPHABET.toUpperCase();
    } else if (isLowercase(char)) {
      alphabet = ALPHABET.toLowerCase();
    } else {
      return char;
    }

    return getEncryptedChar(char, key, alphabet);
  }).join('');
}


// simple shift
console.log(caesarEncrypt('A', 0) === 'A');       // "A"
console.log(caesarEncrypt('A', 3) === 'D');       // "D"

// // wrap around
console.log(caesarEncrypt('y', 5) === 'd');       // "d"
console.log(caesarEncrypt('a', 47) === 'v');      // "v"

// // all letters
console.log(caesarEncrypt('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 25) === "ZABCDEFGHIJKLMNOPQRSTUVWXY");
// "ZABCDEFGHIJKLMNOPQRSTUVWXY"
console.log(caesarEncrypt('The quick brown fox jumps over the lazy dog!', 5) === "Ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl!");
// "Ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl!"

// many non-letters
console.log(caesarEncrypt('There are, as you can see, many punctuations. Right?; Wrong?', 2) === "Vjgtg ctg, cu aqw ecp ugg, ocpa rwpevwcvkqpu. Tkijv?; Ytqpi?");
// "Vjgtg ctg, cu aqw ecp ugg, ocpa rwpevwcvkqpu. Tkijv?; Ytqpi?"

console.log(caesarEncrypt('', 0) === ''); // ''
console.log(caesarEncrypt('', 3) === ''); // ''
console.log(caesarEncrypt('. $789!', 3) === '. $789!'); // '. $789!'