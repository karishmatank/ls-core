function staggeredCase(string) {
  let nextLowercase = false;

  return string
    .split('')
    .reduce((acc, char) => {
      if (/[a-z]/ig.test(char)) {
        if (nextLowercase) {
          acc += char.toLowerCase();
          nextLowercase = false;
        } else {
          acc += char.toUpperCase();
          nextLowercase = true;
        }
      } else {
        acc += char;
      }
      return acc;
    }, '');
}

console.log(staggeredCase('I Love Launch School!'));        // "I lOvE lAuNcH sChOoL!"
console.log(staggeredCase('ALL CAPS'));                     // "AlL cApS"
console.log(staggeredCase('ignore 77 the 444 numbers'));    // "IgNoRe 77 ThE 444 nUmBeRs"