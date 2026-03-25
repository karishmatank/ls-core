// What will the following code log to the console and why? Don't run the code until after you have tried to answer.

let a = 7;

function myValue(a) {
  a += 10;
}

myValue(a);
console.log(a);

/*
This prints 7.

This is pretty similar to part 1. Even though we rename the local variable within myValue to `a` instead of `b`, it is
still separate from the global variable `a` declared and initialized on line 3. Local variable `a` shadows global
variable `a`.
*/