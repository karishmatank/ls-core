/*
In the following code, a user creates a person object literal and defines two methods for returning the person's first
and last names. What is the result when the user tries out the code on the last line?
*/

const person = {
  firstName() {
    return 'Victor';
  },
  lastName() {
    return 'Reyes';
  },
};

console.log(`${person.firstName} ${person.lastName}`);

/*
This will print the string representation of a function both times. `firstName` and `lastName` are methods of the
`person` object. We haven't called them in the console.log call however, so we'll print the string representation
of those methods instead.

EDIT: Not quite! With template literals, JS will force the function object to be converted to a string, which
logs its source code. Instead, if we didn't use a template literal, as I show below, we would get the concise
representation [Function: firstName], etc.
*/


console.log("***");
console.log(person.firstName);
