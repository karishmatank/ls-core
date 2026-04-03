/*
Write a function that takes a string argument consisting of a first name, a space, and a last name, and
returns a new string consisting of the last name, a comma, a space, and the first name.
*/

function swapName(name) {
  let [firstName, lastName] = name.split(' ');
  return lastName + ', ' + firstName;
}

console.log(swapName('Joe Roberts'));    // "Roberts, Joe"