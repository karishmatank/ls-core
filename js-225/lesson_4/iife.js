/*
Will the code below execute?
*/

function() {
  console.log("Sometimes, syntax isn't intuitive!")
}();

/*
No, because we are trying to call a function declaration
*/

/*
Edit the code from problem one so it executes without error.
*/

(function() {
  console.log("Sometimes, syntax isn't intuitive!")
})();

/*
The code below throws an error:
*/

var sum = 0;
var numbers;

sum += 10;
sum += 31;

numbers = [1, 7, -3, 3];

function sum(arr) {
  return arr.reduce(function(sum, number) {
    sum += number;
    return sum;
  }, 0);
}

sum += sum(numbers);  // ?

/*
What kind of problem does this error highlight? Use an IIFE to address it, so that code runs without error.
*/

/*
We are using `sum` for both the function and variable name, which means the function definition will be overwritten
when we assign the value 0 to `sum` on the first line.

Instead, we should do this:
*/

var sum = 0;
var numbers;

sum += 10;
sum += 31;

numbers = [1, 7, -3, 3];

sum += (function(arr) {
  return arr.reduce(function(sum, number) {
    sum += number;
    return sum;
  }, 0);
})(numbers);

/*
Consider the output below:

countdown(7);
7
6
5
4
3
2
1
0
Done!

Implement a function countdown that uses an IIFE to generate the desired output.
*/

let countdown = function(start) {
  (function(count) {
    for (let i = count; i >= 0; i -= 1) {
      console.log(i);
    }
    console.log('Done!');
  })(start);
};

countdown(7);

/*
Is the named function in this IIFE accessible in the global scope?
*/

(function foo() {
  console.log('Bar');
})();

foo() // ?

/*
No. `foo` is defined within its own scope within the IIFE.
*/

/*
For an extra challenge, refactor the solution to problem 4 using recursion, bearing in mind that a named function created in an IIFE can be referenced inside of the IIFE.
*/

/*let*/ countdown = function(start) {
  (function printNum(count) {
    if (count < 0) {
      console.log('Done!');
      return;
    }
    console.log(count);
    printNum(count - 1);

  })(start);
};

countdown(7);