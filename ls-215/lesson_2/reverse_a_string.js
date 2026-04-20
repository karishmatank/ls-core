function reverse(string) {
  let chars = string.split('');
  chars.reverse();
  return chars.join('');
}

console.log(reverse('hello'));                  // returns "olleh"
console.log(reverse('The quick brown fox'));    // returns "xof nworb kciuq ehT"