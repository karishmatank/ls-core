/*
What will the code below output to the console?
*/

let message = 'Hello from the global scope!';

function func(message) {
  message = 'Hello from the function scope!';
  console.log(message);
}

func(message);
console.log(message);

/*
This will print:

Hello from the function scope!
Hello from the global scope!
*/


/*
What will the code below log to the console? What does this output demonstrate in relation to the output of problem one?
*/

let myObj = { message: 'Greetings from the global scope!' };

function func(obj) {
  obj.message = 'Greetings from the function scope!';
  console.log(obj.message);
}

func(myObj);

console.log(myObj.message);

/*
This will print 'Greetings from the function scope!' 2x.

In this problem, we're mutating an object rather than reassigning a local variable.
*/


/*
What will the code below log to the console?
*/

/*let*/ message = 'Hello from the global scope!';

function func() {
  message = 'Hello from the function scope!';
  console.log(message);
}

func();
console.log(message);

/*
This will log 'Hello from the function scope!' 2x.
We are reassigning the global variable `message` here.
*/


/*
What will the code below log to the console?
*/

let a = 10;
let obj = {
  a
}

let newObj = obj;
newObj.a += 10;

console.log(obj.a === a);
console.log(newObj.a === obj.a);

/*
This will log:
false
true

We create a new object `obj` with one property `a` with a value of 10.
We then set `newObj` to reference the same object in memory as `obj` and increase the value of the `a`
property in that object to 20.
`obj.a` now references the value 20, whereas global variable `a` has the value 10, so the first expression is false
`newObj` and `obj` reference the same object, so the second expression turns into `10 === 10`, which is true.
*/


/*
If objects are mutable, why does the second to last line return false?
*/

let animal = {
  name: 'Pumbaa',
  species: 'Phacochoerus africanus',
};

let menagerie = {
  warthog: animal,
};

animal = {
  name: 'Timon',
  species: 'Suricata suricatta',
};

menagerie.meerkat = animal;

menagerie.warthog === animal; // false
menagerie.meerkat === animal; // true


/*
That's because we reassigned the global variable `animal` to a new object in memory.
The value of `warthog` references the object whose name is Pumbaa and species is Phacochoerus africanus.
The global variable animal no longer references that same object, a we've reassigned it.
That's why the last line returns true.
*/