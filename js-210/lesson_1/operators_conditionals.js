let apples = 3;
let bananas = 5;

if (apples == bananas) { // Loose equality!
  console.log("Equal!");
}

bananas = '3';
if (apples == bananas) { // Loose equality!
  console.log("Equal!"); // <--
}

if (apples === bananas) { // Strong equality
  console.log("Equal!");
}
// 3 !== '3'

if (apples === bananas) {
  console.log("Equal!");
} else {
  console.log("Not equal.") // <--
}

if (apples === bananas) {
  console.log("Equal!");
} else if (apples == bananas) {
  console.log("Equal but different types.") // <--
} else {
  console.log("Not equal.")
}

if (apples === bananas) {
  console.log("Equal!");
} else {
  if (apples == bananas) {
    console.log("Equal but different types.") // <--
  } else {
    console.log("Not equal.")
  }
}

apples = 3;
bananas = 3;
let areEqual = apples === bananas;
console.log(areEqual);

apples = 3;
bananas = undefined;
let eitherOr = apples || bananas;
console.log(eitherOr);

bananas = 1;
eitherOr = apples || bananas;
console.log(eitherOr);
eitherOr = bananas || apples;
console.log(eitherOr);

let lastName = 'Last';
let familyMessage = lastName === 'Last' ? "You're part of the family!" : "You're not family.";
console.log(familyMessage);