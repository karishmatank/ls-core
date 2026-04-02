/*
Read through the code below and determine what will be logged.
You may refer to the ASCII Table to look up character code values.
http://www.ascii-code.com/
*/

function one() {
  function log(result) {
    console.log(result);
  }

  function anotherOne(...args) {
    let result = '';
    for (let i = 0; i < args.length; i += 1) {
      result += String.fromCharCode(args[i]);
    }

    log(result);
  }

  function anotherAnotherOne() {
    console.log(String.fromCharCode(87, 101, 108, 99, 111, 109, 101));
    anotherOne(116, 111);
  }

  anotherAnotherOne();
  anotherOne(116, 104, 101);
  return anotherOne;
}

one()(77, 97, 116, 114, 105, 120, 33);

/*
This will print:

Welcome
to
the
Matrix!

We first invoke `one`, which calls `anotherAnotherOne` and `anotherOne` before returning `anotherOne`,
which is a closure that closes over `log`. The initial calls to `anotherAnotherOne` and `anotherOne`
print the "Welcome to the" portion. We then immediately invoke the returned closure, passing in the
ASCII values for "Matrix!", which is subsequently printed.
*/
