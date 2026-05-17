/*
What will the code below log to console?
*/

let obj = {
  message: 'JavaScript',
};

function foo() {
  console.log(this.message);
}

foo.bind(obj);

/*
This won't print anyting to the console as is, since we aren't invoking any functions or logging to the console.
If we were to assign the resulting function from `foo.bind(obj)` to a separate variable and then invoke that function,
we would print: 'JavaScript' to the console, as we've permanently bound that function to have the context of `obj`.
*/

/*
What will the code below output?
*/

/*let*/ obj = {
  a: 2,
  b: 3,
};

function foo() {
  return this.a + this.b;
}

let bar = foo.bind(obj);

console.log(bar());

/*
This will print 5. We are invoking `bar`, which is a function that has `obj` as its permanent context.
When we invoke `bar`, we get the `a` and `b` properties from `obj`, which are 2 and 3, respectively, and we add them
up to get a return value of 5.
*/

/*
What will the code below log to the console?
*/

let positiveMentality = {
  message: 'JavaScript makes sense!',
};

let negativeMentality = {
  message: 'JavaScript makes no sense!',
};

function foo() {
  console.log(this.message);
}

/*let*/ bar = foo.bind(positiveMentality);

negativeMentality.logMessage = bar;
negativeMentality.logMessage();

/*
This will print "JavaScript makes sense!". We are creating a function that is bound to `positiveMentality`,
and we're creating a `logMessage` property on `negativeMentality` to reference that bound function.
We then invoke the method, but because its context is already bound to `positiveMentality`, `this.message`
references the value `'JavaScript makes sense!'`.
*/

/*
What will the code below output?
*/

/*let*/ obj = {
  a: 'Amazebulous!',
};
let otherObj = {
  a: "That's not a real word!",
};

function foo() {
  console.log(this.a);
}

/*let*/ bar = foo.bind(obj);

bar.call(otherObj);

/*
This will print:
Amazebulous!

`bar` is the resulting function from binding `obj` to `foo`.
As a result, even though we call `bar` by passing in `otherObj` as context, it effectively doesn't do anything.

*/
