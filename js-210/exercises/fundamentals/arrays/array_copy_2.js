/*
In the previous exercise, the value of the reference gets copied.
For this exercise, only the values of the array should be copied, but not the reference.
Implement two alternative ways of doing this.

Here is the code from the previous exercise:
let myArray = [1, 2, 3, 4];
const myOtherArray = myArray;

myArray.pop();
console.log(myOtherArray);

myArray = [1, 2];
console.log(myOtherArray);
*/

/*
Option 1 - Create a shallow copy. Since the elements of the array are primitives, this
will be fine as we can't mutate any of the elements. We can use the slice method to create a shallow copy
*/

let myArray = [1, 2, 3, 4];
const myOtherArray = myArray.slice();

myArray.pop();
console.log(myOtherArray);

myArray = [1, 2];
console.log(myOtherArray);

/*
Option 2 - Use a for loop to populate myOtherArray
*/

myArray = [1, 2, 3, 4];
const anotherArray = []; // I renamed this
for (let element of myArray) {
  anotherArray.push(element);
}

myArray.pop();
console.log(anotherArray);

myArray = [1, 2];
console.log(anotherArray);