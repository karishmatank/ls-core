function swapCase(string) {
  let chars = string.split('');
  let swappedCase = chars.map(char => {
    if (isLowerCase(char)) {
      return char.toUpperCase();
    } else if (isUpperCase(char)) {
      return char.toLowerCase();
    } else {
      return char;
    }
  });
  return swappedCase.join('');
}

function isLowerCase(char) {
  return char >= 'a' && char <= 'z';
}

function isUpperCase(char) {
  return char >= 'A' && char <= 'Z';
}

console.log(swapCase('CamelCase'));              // "cAMELcASE"
console.log(swapCase('Tonight on XYZ-TV'));      // "tONIGHT ON xyz-tv"