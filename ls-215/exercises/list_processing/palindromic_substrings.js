// From previous exercise
function substrings(string) {
  let substrings = [];
  for (let idxStart = 0; idxStart < string.length; idxStart += 1) {
    for (let idxEnd = idxStart + 1; idxEnd <= string.length; idxEnd += 1) {
      substrings.push(string.slice(idxStart, idxEnd));
    }
  }
  return substrings;
}

function palindromes(string) {
  let substr = substrings(string);
  return substr.filter(str => {
    if (str.length === 1) return false;
    let p = str.split('').reverse().join('');
    return str === p;
  });
}

console.log(palindromes('abcd'));       // []
console.log(palindromes('madam'));      // [ "madam", "ada" ]

console.log(palindromes('hello-madam-did-madam-goodbye'));
// returns
// [ "ll", "-madam-", "-madam-did-madam-", "madam", "madam-did-madam", "ada",
//   "adam-did-mada", "dam-did-mad", "am-did-ma", "m-did-m", "-did-", "did",
//   "-madam-", "madam", "ada", "oo" ]

console.log(palindromes('knitting cassettes'));
// returns
// [ "nittin", "itti", "tt", "ss", "settes", "ette", "tt" ]