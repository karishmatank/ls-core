// What will the following code log to the console and why? Don't run the code until after you have tried to answer.

let a = [1, 2, 3];

function myValue(b) {
  b[2] += 7;
}

myValue(a);
console.log(a);

/*
This will print: [1, 2, 10].

When we invoke `myValue`, we pass in `a`. Since `a` references an array, this behaves more like "pass by reference",
where parameter `b` within `myValue` now references the same array as global variable `a`.
Thus, when we mutate the array within the body of `myValue`, we'll see the mutation reflected when we reference
global variable `a` as well. We reassign the element at index 2 to be 10 (3 + 7).
*/