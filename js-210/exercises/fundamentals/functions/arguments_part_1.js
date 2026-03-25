// What will the following code log to the console and why? Don't run the code until after you have tried to answer.

let a = 7;

function myValue(b) {
  b += 10;
}

myValue(a);
console.log(a);

/*
This will print 7.

We first declare and initialize global variable `a` to the value 7. We then invoke `myValue`, passing in `a`. Given
`a` references an immutable object, this behaves more like "pass-by-value" in JavaScript. Within `myValue`, parameter `b`
references the value 7 now as well. We then use augmented assignment to reassign local variable `b` to `17`. However,
because `b` is a local variable, it has no affect outside of the function, as we aren't returning `b` or reassigning
global variable `a`. Thus, when we log `a` to the console on line 10, we still print 7.
*/