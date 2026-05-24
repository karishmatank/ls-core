/*
Use the method we learned above to assign foo below to a new Object with prot as its prototype.
*/

let prot = {};

let foo = Object.create(prot);

/*
Use getPrototypeOf to demonstrate the prototypal relationship between prot and foo.
*/

console.log(Object.getPrototypeOf(foo) === prot);

/*
Use isPrototypeOf to demonstrate the prototypal relationship between prot and foo.
*/

console.log(prot.isPrototypeOf(foo));

/*
What will the last two lines of the code below return? Why?
*/

/*let*/ prot = {};

/*let*/ foo = Object.create(prot);

prot.isPrototypeOf(foo);
Object.prototype.isPrototypeOf(foo);

/*
The first will return true, and is the same code as we had in the prior parts.
The second will print false, because `prot` is the prototype of `foo`, not `Object.prototype`.

EDIT: Second will print true!
This is because of prototype chaining. Object.prototype is on foo's prototype chain
because the prototype of prot is Object.prototype
*/