// What will the following code log to the console and why? Don't run the code until after you have tried to answer.

var myVar = 'This is global';

function someFunction() {
  console.log(myVar);
}

someFunction();

/*
This will print "This is global". When we invoke `someFunction`, we look for `myVar` first in the function scope.
We don't find it, so JavaScript will look towards the next scope out, which is the global scope. We find `myVar` there
and print its value to the console.
*/