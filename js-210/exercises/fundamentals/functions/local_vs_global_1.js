// What will the following code log to the console and why? Don't run the code until after you have tried to answer.

var myVar = 'This is global';

function someFunction() {
  var myVar = 'This is local';
}

someFunction();
console.log(myVar);

/*
This will print 'This is global'.
In JavaScript, variables declared with `var` are function scoped. Therefore, the `myVar` variable inside
`someFunction` is a separate local variable. We call `someFunction` but don't do much with the local `myVar`- it just
disappears after we finish executing `someFunction`. The `myVar` accessible to line 10 is the global `myVar` with
value `'This is global'`.
*/