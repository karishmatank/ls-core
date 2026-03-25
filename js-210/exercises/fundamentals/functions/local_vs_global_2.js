// What will the following code log to the console and why? Don't run the code until after you have tried to answer.

var myVar = 'This is global';

function someFunction() {
  var myVar = 'This is local';
  console.log(myVar);
}

someFunction();

/*
This will print 'This is local'.

We log to the console only within `someFunction`. In this case, the local variable `myVar` shadows the global variable
`myVar`, so line 7 can only access the local `myVar`.
*/