/*
Write a function named makeMultipleLister that, when invoked and passed a number,
returns a function that logs every positive integer multiple of that number less than 100. Usage looks like this:

> let lister = makeMultipleLister(13);
> lister();
13
26
39
52
65
78
91
*/

function makeMultipleLister(number) {
  return function() {
    let result = number;
    while (result < 100) {
      console.log(result);
      result += number;
    }
  };
}

let lister = makeMultipleLister(13);
lister();
// 13
// 26
// 39
// 52
// 65
// 78
// 91

/*
Write a program that uses two functions, add and subtract, to manipulate a running total value.
When you invoke either function with a number, it should add or subtract that number from the running total
and log the new total to the console. Usage looks like this:

> add(1);
1
> add(42);
43
> subtract(39);
4
> add(6);
10
*/

function makeTracker() {
  let total = 0;
  return {
    add: function(num) {
      total += num;
      console.log(total);
    },
    subtract: function(num) {
      total -= num;
      console.log(total);
    },
  };
}

let { add, subtract } = makeTracker();

add(1);
// 1
add(42);
// 43
subtract(39);
// 4
add(6);
// 10


/*
Given the following code:

function startup() {
  let status = 'ready';
  return function() {
    console.log('The system is ready.');
  };
}

let ready = startup();
let systemStatus = // ?

Is there a way to set the value of systemStatus to the value of the inner variable status without
changing startup in any way? If so, how?
*/

function startup() {
  let status = 'ready';
  return function() {
    console.log(`The system is ${status}.`);
  };
}

let ready = startup();
let systemStatus = ready();

/*
EDIT- I think I misunderstood the question. I thought the question was asking us basically to build it out. However,
I think it is asking whether we can access local variable `status` from the global scope, which we can't.
*/