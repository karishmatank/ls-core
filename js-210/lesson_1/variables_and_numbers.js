let numerator = 10;
const DENOMINATOR = 2;

let answer = numerator / DENOMINATOR;
console.log(answer); // Should be 5

let incrementer = 1;
let start = incrementer;
let end;
let difference;

let numLoops = 3;
for (let i = 0; i < numLoops; i += 1) {
  incrementer += 1;
}

numLoops = 2;
for (let i = 0; i < numLoops; i += 1) {
  incrementer++;
}

end = incrementer;
difference = end - start;

console.log(end); // Should be 6
console.log(difference); // Should be 5

answer = (11 + 31) * 3;
console.log(answer); // Should be 126