/*
Write a Function named myForEach that is similar to the built-in Array.prototype.forEach method.
Your Function should take an array and another Function as arguments.
The Function passed to myForEach should reassign a variable in the outer scope.
For instance, in the code fragment below, the Function passed to myForEach reassigns the min variable.
*/

function myForEach(array, func) {
  for (let idx = 0; idx < array.length; idx += 1) {
    func(array[idx]);
  }
}

let min = Infinity;
let getMin = value => (min = value <= min ? value : min);
myForEach([4, 5, 12, 23, 3], getMin);
console.log(min);                        // 3


/*
EDIT: Given the real forEach invokes the callback and passes in 3 arguments, we should do the same instead.
See below.
*/

function myForEach(array, func) {
  for (let idx = 0; idx < array.length; idx += 1) {
    func(array[idx], idx, array);
  }
}