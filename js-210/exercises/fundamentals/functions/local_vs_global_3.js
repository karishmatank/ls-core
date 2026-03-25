// What will the following code log to the console and why? Don't run the code until after you have tried to answer.

var myVar = 'This is global';

function someFunction() {
  myVar = 'This is local';
}

someFunction();
console.log(myVar);

/*
This will print "This is local". Here, when we call `someFunction`, we end up reassigning the global variable `myVar`
from within the function given we don't declare a local `myVar` variable. Thus, when we log `myVar` to the console
on line 10, we'll print "This is local" as we've reassigned the global variable that line 10 has access to.
*/