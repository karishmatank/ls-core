function octalToDecimal(numberString) {
  let power = numberString.length - 1;
  let total = 0;
  for (let char of numberString) {
    total += Number(char) * (8 ** power);
    power -= 1;
  }
  return total;
}

console.log(octalToDecimal('1'));           // 1
console.log(octalToDecimal('10'));          // 8
console.log(octalToDecimal('130'));         // 88
console.log(octalToDecimal('17'));          // 15
console.log(octalToDecimal('2047'));        // 1063
console.log(octalToDecimal('011'));         // 9

/* EDIT: The solution above isn't really in abstraction, so I decided to try again */

function octalToDecimal(numberString) {
  let digits = numberString.split('').map(digit => Number(digit));
  return digits.reduce((accumulator, digit, index) => {
    let power = numberString.length - 1 - index;
    return accumulator + digit * (8 ** power);
  }, 0);
}