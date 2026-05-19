/*
Read the following code carefully. What do you think is logged on the last line. Try to answer the question before you run the code.
*/

const person = {
  firstName: 'Rick ',
  lastName: 'Sanchez',
  fullName: this.firstName + this.lastName,
};

console.log(person.fullName);

/*
I ended up running the code. At first, I thought `this` would reference `person`, but I realized that the
examples we've been looking at were in functions / methods, of which `fullName` is not either.

The other thing to remember is that strict mode only really affects what happens inside functions / methods.
In this case, `this` isn't `undefined` in strict mode, it still attaches to the global / window object, as it
does in this case in sloppy mode too.

Therefore, we get `undefined + undefined`, which yields and prints `NaN`.
*/