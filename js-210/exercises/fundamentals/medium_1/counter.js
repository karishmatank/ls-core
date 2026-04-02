/*
What will the following code snippets log?
*/

// 1
var counter = 5;
var rate = 3;
console.log('The total value is ' + String(counter * rate));

function counter(count) {
  // ...
}

/*
This will print 'The total value is 15.'. Even though functions get "hoisted" over var declarations,
we reassign `counter` to reference the number 5 on the first line of the execution phase.
By the time we run the console.log statement, `counter` will have value 5 and `rate` will have value 3.
*/




// 2
function counter(count) {
  // ...
}

console.log('The total value is ' + String(counter * rate));

var counter = 5;
var rate = 3;


/*
At this point, when we run the console.log statement, counter still references a function, and `rate` is undefined.
We haven't assigned `counter` to 5 and `rate` to 3 yet.
We can't really multiply a function by undefined, so that should result in NaN?
We then coerce NaN to a string, which results in 'NaN'.
Therefore, we print 'The total value is NaN'.
*/




// 3
var counter = 5;
var rate = 3;

function counter(count) {
  // ...
}

console.log('The total value is ' + String(counter * rate));


/*
This matches the same behavior as snippet 1. It doesn't matter that we have the function definition earlier
in this case, as it gets "hoisted" during the creation phase.
*/




// 4
let counter = 5;
let rate = 3;

function counter(count) {
  // ...
}

console.log('The total value is ' + String(counter * rate));


/*
This will throw a SyntaxError, as we can't have `counter` declared with `function` and `let`.
Therefore, nothing will print.

EDIT: SyntaxError, not ReferenceError. Also forgot that the error occurs when we try to define the function.
That's because the function definition comes sequentially last.
*/