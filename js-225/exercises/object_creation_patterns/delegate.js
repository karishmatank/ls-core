/*
Write a delegate function that can be used to delegate the behavior of a method or function to another object's method.
delegate takes a minimum of two arguments: (1) the object and (2) name of the method on the object.
The remaining arguments, if any, are passed — as arguments — to the objects' method that it delegates to.
The delegate function should return the same value returned by calling the other object's method.

Note that this is not the same as using bind. bind returns a new function, whereas delegate maintains the reference.
*/

function delegate(obj, method, ...args) {
  return function() {
    return obj[method].call(obj, ...args);
  };
}

const foo = {
  name: 'test',
  bar(greeting) {
    console.log(`${greeting} ${this.name}`);
  },
};

const baz = {
  qux: delegate(foo, 'bar', 'hello'),
};

baz.qux();   // logs 'hello test';

foo.bar = () => { console.log('changed'); };

baz.qux();          // logs 'changed'