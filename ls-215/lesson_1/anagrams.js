function anagram(word, list) {
  return list.filter(candidate => isAnagram(word, candidate));
}

function isAnagram(word, candidate) {
  let wordChars = word.split('').sort();
  let candidateChars = candidate.split('').sort();
  return areArraysEqual(wordChars, candidateChars);
}

function areArraysEqual(arr1, arr2) {
  if (arr1.length !== arr2.length) return false;
  return arr1.every((num, idx) => num === arr2[idx]);
}

console.log(anagram('listen', ['enlists', 'google', 'inlets', 'banana']));  // [ "inlets" ]
console.log(anagram('listen', ['enlist', 'google', 'inlets', 'banana']));   // [ "enlist", "inlets" ]