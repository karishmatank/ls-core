// What will the following code log to the console and why? Don't run the code until after you have tried to answer.

console.log(a);

var a = 1;

/*
This will print `undefined`.

When JavaScript runs the creation phase, it "hoists" the variable declaration for `a`. Since we use `var` for the
declaration, we assign `a` to the value `undefined` at first. We next log the value of `a`, which is still
undefined when we start the execution phase. We only reassign `a` to `1` after logging its value.
*/