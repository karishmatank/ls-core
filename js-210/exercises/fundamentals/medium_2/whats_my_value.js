/*
What will the following program log to the console? Can you explain why?
*/

const array = ['Apples', 'Peaches', 'Grapes'];

array[3.4] = 'Oranges';
console.log(array.length);
console.log(Object.keys(array).length);

array[-2] = 'Watermelon';
console.log(array.length);
console.log(Object.keys(array).length);

/*
This will print:
3
4
3
5

On both lines 7 and 11, we're adding properties to the array, as the keys are not non-negative integers.
The length of the array as a result remains at 3, whereas the added properties do get reflected
within the call to `Object.keys`.

*/