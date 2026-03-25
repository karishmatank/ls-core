// What will the following code log to the console and why? Don't run the code until after you have tried to answer.

function someFunction() {
  myVar = 'This is global';
}

someFunction();
console.log(myVar);

/*
What this prints depends on strict mode vs non-strict mode.
In strict mode, we'll get a ReferenceError as we haven't properly declared the variable.
In non-strict mode, we'll print 'This is global' as JavaScript will create an implicit global variable
when we run line 4 and assign it the value 'This is global'. This variable thus is accessible to line 8.

EDIT: The better way to phrase the behavior for non-strict mode is that "JavaScript creates a property on the global
object, which then behaves like a global variable and is accessible in the outer scope."

*/