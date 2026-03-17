/*
In this exercise, you will write a program that asks the user for a phrase,
then outputs the number of characters in that phrase.
Go over the documentation for String to find an appropriate method to use.
*/

// Examples
// Please enter a phrase: walk
// // console output
// There are 4 characters in "walk".

// Please enter a phrase: walk, don't run
// // console output
// There are 15 characters in "walk, don't run".

let rlSync = require('readline-sync');
let phrase = rlSync.question("Please enter a phrase: ");

console.log(`There are ${phrase.length} characters in "${phrase}".`);

// Ignore spaces
// let phraseNoSpaces = phrase.replaceAll(' ', '');
let phraseNoSpaces = phrase.replace(/ /g, '');
console.log(`There are ${phraseNoSpaces.length} non-space characters in "${phrase}".`);

// Ignore all non-alphabetical characters
let phraseAlpha = phrase.replace(/[^a-zA-Z]/g, '');
console.log(`There are ${phraseAlpha.length} alphabetical characters in "${phrase}".`);