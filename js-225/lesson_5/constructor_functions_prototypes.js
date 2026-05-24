/*
What does the following code log to the console?
*/

let a = 1;
let foo;
let obj;

function Foo() {
  this.a = 2;
  this.bar = function() {
    console.log(this.a);
  };
  this.bar();
}

foo = new Foo();

foo.bar();
Foo();

obj = {};
Foo.call(obj);
obj.bar();

console.log(this.a);

/*
This will print:
2
2
TypeError (if we're in strict mode), 2 in sloppy mode
  - When we call `Foo` as a regular function, `this` in strict mode is `undefined`, in sloppy mode references
    the `global` or `window` objects
(The following will only print in sloppy mode)
2
2
2 (EDIT: note, in Node, this will print undefined instead because of the separate module scope)

*/

/*
What does the following code log to the console?
*/

/*
let RECTANGLE = {
  area() {
    return this.width * this.height;
  },
  perimeter() {
    return 2 * (this.width + this.height);
  },
};

function Rectangle(width, height) {
  this.width = width;
  this.height = height;
  this.area = RECTANGLE.area();
  this.perimeter = RECTANGLE.perimeter();
}

let rect1 = new Rectangle(2, 3);
console.log(rect1.area);
console.log(rect1.perimeter);
*/

/*
This will log NaN twice.

The issue is that we invoke the `area` and `perimeter` methods on `RECTANGLE`, which means that
`this` inside both methods references the `RECTANGLE` object, which doesn't have `width` or `height` properties.
Thus, the expression `this.width` and `this.height` will both return `undefined`
*/

/*
How do you fix this problem?
*/

let RECTANGLE = {
  area() {
    return this.width * this.height;
  },
  perimeter() {
    return 2 * (this.width + this.height);
  },
};

function Rectangle(width, height) {
  this.width = width;
  this.height = height;
  this.area = RECTANGLE.area.call(this);
  this.perimeter = RECTANGLE.perimeter.call(this);
}

let rect1 = new Rectangle(2, 3);
console.log(rect1.area);
console.log(rect1.perimeter);

/*
Write a constructor function Circle, that takes a radius as an argument.
You should be able to call an area method on the created objects to get the circle's area.
Test your implementation with the following code:
*/

function Circle(radius) {
  this.radius = radius;
}

Circle.prototype.area = function() {
  return this.radius ** 2 * Math.PI;
};

/*let*/ a = new Circle(3);
let b = new Circle(4);

console.log(a.area().toFixed(2)); // => 28.27
console.log(b.area().toFixed(2)); // => 50.27

/*
What will the following code log out and why?
*/

let ninja;
function Ninja() {
  this.swung = true;
}

ninja = new Ninja();

Ninja.prototype.swingSword = function() {
  return this.swung;
};

console.log(ninja.swingSword());

/*
This will print true.
We instantiate a new object from the Ninja constructor function, which will have one property `swung`
with value `true`.
Later, when we invoke the `swingSword` method, which we are able to do on `ninja` as `ninja`'s object prototype
references `Ninja.prototype`, where `swingSword` lives, `this` references the `ninja` object, which again
has a `swung` property with value `true`, and thus will print true.
*/

/*
What will the following code log out and why?
*/

/*let*/ ninja;
function Ninja() {
  this.swung = true;
}

ninja = new Ninja();

Ninja.prototype = {
  swingSword: function() {
    return this.swung;
  },
};

console.log(ninja.swingSword());

/*
EDIT: I didn't get this one right.
We initialize a new object from the `Ninja` constructor function, where the object prototype references
the `Ninja.prototype` object at the time.
We then reassign `Ninja.prototype` to a new object, but the object prototype of the `ninja` object
still references the original function prototype object.
Therefore, we won't find `swingSword` in the prototype chain for `ninja`.
Thus, we'll see an error.
*/

/*
Implement the method described in the comments below:
*/

let ninjaA;
let ninjaB;
function Ninja() {
  this.swung = false;
}

ninjaA = new Ninja();
ninjaB = new Ninja();

// Add a swing method to the Ninja prototype which
// returns the calling object and modifies swung
Ninja.prototype.swing = function() {
  this.swung = !this.swung;
  return this;
};

console.log(ninjaA.swing().swung);      // must log true
console.log(ninjaB.swing().swung);      // must log true

/*
In this problem, we'll ask you to create a new instance of an object,
without having direct access to the constructor function:
*/

/*let*/ ninjaA = (function() {
  function Ninja(){};
  return new Ninja();
})();

// create a ninjaB object
/*let*/ ninjaB = new ninjaA.constructor();

console.log(ninjaB.constructor === ninjaA.constructor);    // should log true

/*
EDIT: above is correct, but another way is through Object.create:
*/

ninjaB = Object.create(Object.getPrototypeOf(ninjaA));


/*
Follow the steps below:

Create an object called shape that has a getType method.
Define a Triangle constructor function whose prototype is shape. Objects created with Triangle should have
four own properties: a, b, c (representing the sides of a triangle), and type.
Add a new method to the prototype called getPerimeter.
Test your implementation with the following code:
*/

let shape = {
  getType() {
    return this.type;
  }
};

function Triangle(a, b, c) {
  this.a = a;
  this.b = b;
  this.c = c;
  this.type = 'triangle';
}

Triangle.prototype = shape;
Triangle.prototype.constructor = Triangle;
Triangle.prototype.getPerimeter = function() {
  return this.a + this.b + this.c;
};

let t = new Triangle(3, 4, 5);
console.log(t.constructor);                 // Triangle(a, b, c)
console.log(shape.isPrototypeOf(t));        // true
console.log(t.getPerimeter());              // 12
console.log(t.getType());                   // "triangle"

/*
NOTE:
An earlier attempt used `Object.setPrototypeOf` within the constructor function,
however, that still leaves Triangle.prototype as an empty object.
In addition, we have to remember to reset the constructor to `Triangle` given we are reassigning
`Triangle.prototype`.
*/

/*
Update the following code so that, instead of logging the values, each statement logs the name of the
constructor to which it belongs.
*/

console.log("Hello");
console.log([1,2,3]);
console.log({name: 'Srdjan'});

/*
Expected output:
String
Array
Object
*/

console.log("Hello".constructor.name);
console.log([1,2,3].constructor.name);
console.log({name: 'Srdjan'}.constructor.name);

/*
Since a constructor is just a function, it can be called without the new operator,
and this can lead to unexpected results and errors especially for inexperienced programmers.

Write a constructor function that can be used with or without the new operator,
and return the same result in either form. Use the code below to check your solution:
*/

function User(first, last) {
  if (!(this instanceof User)) {
    return new User(first, last);
  }
  this.first = first;
  this.last = last;
  this.name = this.first + ' ' + this.last;
}

let name = 'Jane Doe';
let user1 = new User('John', 'Doe');
let user2 = User('John', 'Doe');

console.log(name);         // => Jane Doe
console.log(user1.name);   // => John Doe
console.log(user2.name);   // => John Doe

/*
Create a function that can create an object with a given object as its prototype, without using Object.create.
*/

function createObject(obj) {
  let newObj = {};
  Object.setPrototypeOf(newObj, obj);
  return newObj;
}

let foo = {
  a: 1
};

let bar = createObject(foo);
console.log(foo.isPrototypeOf(bar));         // true

/*
EDIT: This works, but MDN actually mentions that it's not ideal to use setPrototypeOf as it is an extremely slow process.
Instead, they recommend to create a new object with the desired object prototype using Object.create.
Since we can't do that for this example, we can instead create a new constructor function within
our `createObject` function and set the function prototype.
*/

function createObject(obj) {
  function F() {
  }
  F.prototype = obj;
  let newObj = new F();
  return newObj;
}


/*
Similar to the problem above, without using Object.create,
create a begetObject method that you can call on any object to create an object inherited from it:
*/

Object.prototype.begetObject = function() {
  function F() {}
  F.prototype = this;
  return new F();
}

let foo = {
  a: 1,
};

let bar = foo.begetObject();
console.log(foo.isPrototypeOf(bar));         // true

/*
NOTE: An earlier answer I gave was:

Object.prototype.begetObject = function() {
  function F() {}
  F.prototype = Object.getPrototypeOf(this);
  return new F();
}

This answer is incorrect because it creates "sibling" objects instead of parent/child objects.
In this case, it takes whatever the prototype is of the `this` object and asks the new object to
inherit from that parent. Instead, we want the `this` object to be the parent, so we should set
the new object's prototype to be the `this` object instead.
*/

/*
Create a function neww, so that it works like the new operator. For this practice problem, you may use Object.create.
*/

function neww(constructor, args) {
  let newObj = Object.create(constructor.prototype);
  let returned = constructor.apply(newObj, args);
  if (typeof returned === 'object') {
    return returned;
  }
  return newObj;
}

function Person(firstName, lastName) {
  this.firstName = firstName;
  this.lastName = lastName;
}

Person.prototype.greeting = function() {
  console.log('Hello, ' + this.firstName + ' ' + this.lastName);
};

let john = neww(Person, ['John', 'Doe']);
john.greeting();          // => Hello, John Doe
console.log(john.constructor);         // Person(firstName, lastName) {...}

/*
NOTE:
An earlier attempt to answer the question only returned newObj.
However, that's not how `new` works- the last step of `new` is that it returns the created object
only if the constructor function doesn't explicitly return an object.
Therefore, we need to record the return value of calling the constructor function and then
check if it is an object.
*/