function substrings(string) {
  let substrings = [];
  for (let idxStart = 0; idxStart < string.length; idxStart += 1) {
    for (let idxEnd = idxStart + 1; idxEnd <= string.length; idxEnd += 1) {
      substrings.push(string.slice(idxStart, idxEnd));
    }
  }
  return substrings;
}

console.log(substrings('abcde'));

// returns
// [ "a", "ab", "abc", "abcd", "abcde",
//   "b", "bc", "bcd", "bcde",
//   "c", "cd", "cde",
//   "d", "de",
//   "e" ]