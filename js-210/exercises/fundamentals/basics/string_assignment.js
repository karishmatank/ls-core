/*
Take a look at the following code:
*/

// let myName = 'Bob';
// const saveName = myName;
// myName = 'Alice';
// console.log(myName, saveName);

/*
What does this code log to the console? Think about it for a moment before continuing.

This will print "Alice Bob". myName has value 'Alice' after the reassignment, saveName has the value 'Bob'

*/

/*
Now let's look at something slightly different:
*/

const myName = 'Bob';
const saveName = myName;
myName.toUpperCase();
console.log(myName, saveName);

/*
What does this code log? Can you explain these results?

This will print 'Bob Bob'.
1) We can't reassign constants anyway
2) myName.toUpperCase() returns a new string, which we aren't storing anywhere. Strings are immutable, so
   toUpperCase() can't mutate myName anyway

*/