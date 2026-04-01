/*
What will the following code log to the console and why? Don't run the code until after you have tried to answer.
*/

const myArray = ['a', 'b', 'c'];

console.log(myArray[0]);
console.log(myArray[-1]);

myArray[-1] = 'd';
myArray['e'] = 5;
myArray[3] = 'f';

console.log(myArray[-1]);
console.log(myArray['e']);
console.log(myArray);

/*
This will print:
a
undefined
d
5
['a', 'b', 'c', 'f']

EDIT: Missed that it also prints the other properties too for the last line.
Last line should be [ 'a', 'b', 'c', 'f', '-1': 'd', e: 5 ]

We can access array elements through their indices, coerced into strings, that's why myArray[0] returns the
element at index 0, which is `a`. However, the array has no property -1 as of line 8, so we print undefined.
-1 doesn't access the array from the back to front as it does in Python.

We then set the value for property `-1` to value `d` as well as value `5` for property `e`.
We then add a new element to the array under index 3.

When we print the array, we'll first print the elements with non-negative integer indices, which are
a, b, c, f, as those have non-negative integer indices. We then print the other properties.
*/