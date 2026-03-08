// Q1: Greet Victor 3x. Use a variable and don't hardcode 'Victor'

const fullName = 'Victor';
console.log(`Good Morning, ${fullName}.`);
console.log(`Good Afternoon, ${fullName}.`);
console.log(`Good Evening, ${fullName}.`);

// Q2: Calculate and report the future age of a person in 10, 20, 30, 40 years
const age = 20;
for (let i = 10; i <= 40; i += 10) {
  console.log(`In ${i} years, you will be ${age + i} years old.`);
}

// Q3: What happens when we run the following? Why?
{
  let foo = 'bar';
}

console.log(foo);

/*
We get an error. The reason is because of variable scoping-
variables declared with `let` or `const` in JavaScript are block scoped.
We define `foo` within a block, so it isn't accessible outside of the block.
*/

// Q4: What happens when we run the following? Why?
const NAME = 'Victor';
console.log('Good Morning, ' + NAME);
console.log('Good Afternoon, ' + NAME);
console.log('Good Evening, ' + NAME);

NAME = 'Joe';
console.log('Good Morning, ' + NAME);
console.log('Good Afternoon, ' + NAME);
console.log('Good Evening, ' + NAME);

/*
The console will print the first 3 log functions with `NAME` as value 'Victor'
However, we then get an error because we are trying to reassign a constant.
*/

// Q5: What does this log to the console? Why?
let foo = 'bar';
{
  let foo = 'qux';
}

console.log(foo);

/*
This prints 'bar' to the console.
We declare a separate `foo` variable within the block, but that is block-scoped, so we can't
access that outside of the block. It isn't a reassignment of the `foo` from the outer scope.
*/

// Q6: Will this program produce an error when run? Why or why not?
const FOO = 'bar';
{
  const FOO = 'qux';
}

console.log(FOO);

/*
No, this will not produce an error. We are declaring a new constant `FOO` within the block
that shadows the `FOO` from the outer scope. When we print later on, we'll see `'bar'` in the console.
*/