/*
Q1:
Given the following code, how can you access the name of the person?
*/

let person = {
  name:       'Bob',
  occupation: 'web developer',
  hobbies:    'painting',
};

console.log(person['name']);
console.log(person.name);

/*
Q2:
Which of the following values are valid keys for an object?

1               => No
'1'             => Yes
undefined       => No
'hello world'   => Yes
true            => No
'true'          => Yes


EDIT: All of the above are actually valid!
From the solution: "Note, though, that JavaScript coerces the non-string key values to strings.
Given the listed values, 1 and '1' represent the same key, as do true and 'true'. "

So these are all valid keys when defining object literals, but I got tripped up in thinking about
what gets printed out when we call Object.keys().
*/

/*
Q3:
Use object literal syntax (e.g., { key: value, ... } notation) to create an object
that behaves as an array in a for statement. The object should contain at least 3 elements.
You should place your code between the braces in the let statement:
*/

let myArray = {
  0: 1,
  1: 2,
  2: 3,
  length: 3,
};

for (let i = 0; i < myArray.length; i += 1) {
  console.log(myArray[i]);
}

/*
Q4:
Create an array from the keys of the object obj below, with all of the keys converted to uppercase.
Your implementation must not mutate obj.

The order of the array does not matter.
*/

let obj = {
  b: 2,
  a: 1,
  c: 3,
};

let upperKeys = Object.keys(obj).map((element) => element.toUpperCase());
console.log(upperKeys);
console.log(obj);

/*
Q5:
Create a new object named myObj that uses myProtoObj as its prototype.
*/

let myProtoObj = {
  foo: 1,
  bar: 2,
};

let myObj = Object.create(myProtoObj);

/*
Q6:
Which of the following values are primitive values? Which are objects? Which are neither?

"foo"                             => primitive
3.1415                            => primitive
[ 'a', 'b', 'c' ]                 => object
false                             => primitive
foo                               => neither
function bar() { return "bar"; }  => object
undefined                         => primitive
{ a: 1, b: 2 }                    => object

*/

/*
Q7:
Add a qux property with value 3 to the myObj object we created in the previous exercise.
*/

myObj['qux'] = 3;

/*
Now, examine the following code snippets:
*/

let objKeys = Object.keys(myObj);
objKeys.forEach(function(key) {
  console.log(key);
});

for (let key in myObj) {
  console.log(key);
}

/*
Without running this code, can you determine whether these two snippets produce the same output? Why?

I would guess that both of these produce the same output.
Snippet #1 goes through each key of myObj, which includes the keys that it inherited.
Snippet #2 does the same. If we wanted to limit it to only myObj's specific keys, we would have to use
the `hasOwnProperty` method.

EDIT: I am wrong. Snippet #1 only prints myObj's specific keys rather than the keys it inherited.
*/


/*
Q8:

Create a function that creates and returns a copy of an object.
The function should take two arguments: the object to copy and an array of the keys that you want to copy.
Do not mutate the original object.

The function should let you omit the array of keys argument when calling the function.
If you do omit the argument, the function should copy all of the existing keys from the object.

Here are some examples for your reference:
*/

function copyObj(obj, keys=undefined) {
  if (keys === undefined) {
    keys = Object.keys(obj);
  }

  let newObj = {};
  keys.forEach((key) => {
    newObj[key] = obj[key];
  });

  return newObj;
}

let objToCopy = {
  foo: 1,
  bar: 2,
  qux: 3,
};

let newObj = copyObj(objToCopy);
console.log(newObj);        // => { foo: 1, bar: 2, qux: 3 }

let newObj2 = copyObj(objToCopy, [ 'foo', 'qux' ]);
console.log(newObj2);       // => { foo: 1, qux: 3 }

let newObj3 = copyObj(objToCopy, [ 'bar' ]);
console.log(newObj3);       // => { bar: 2 }


/*
Q9:
What does the following program log to the console? Why?
*/

let foo = {
  a: 'hello',
  b: 'world',
};

let qux = 'hello';

function bar(argument1, argument2) {
  argument1.a = 'hi';
  argument2 = 'hi';
}

bar(foo, qux);

console.log(foo.a);
console.log(qux);

/*
The first log statement will print 'hi'. We've mutated `foo` from within the `bar` function body.

The second log statement will print 'hello'. We've only reassigned a local variable `argument2` within the
`bar` function body. `argument2` starts by taking on the value `hello` since we passed `qux` as the second argument,
but we then reassign it to the value `hi`. We don't end up doing anything with that reassigned local variable, however.
*/

/*
Q10:
How many primitive values are there in the following expression?
Identify them. How many objects are there in the expression? Identify those objects.

[1, 2, ["a", ["b", false]], null, {}]


Primitives:
- 1
- 2
- "a"
- "b"
- false
- null

Objects:
- ["a", ["b", false]], ["b", false], {}, [1, 2, ["a", ["b", false]], null, {}] (the entire thing)

*/

/*
Q11:
Write some code to replace the value 6 in the following object with 606:

You don't have to search the object. Just write an assignment that replaces the 6.
*/

obj = {
  foo: { a: "hello", b: "world" },
  bar: ["example", "mem", null, { xyz: 6 }, 88],
  qux: [4, 8, 12]
};

obj['bar'][3]['xyz'] = 66;
console.log(obj);

/*
Q12:
Consider the following code:

function foo(bar) {
  console.log(bar, bar, bar);
}

foo("hello"); // should print "hello hello hello"
bar("hi");    // should print "hi hi hi"

As written, this code will raise an error on line 6.
Without creating a new function or changing lines 5 or 6, update this code to work as intended.
*/

function foo(bar) {
  console.log(bar, bar, bar);
}

let bar = foo;

foo("hello"); // should print "hello hello hello"
bar("hi");    // should print "hi hi hi"

/*
Q13:
Consider the following code:

function foo(bar) {
  console.log(bar());
}

foo();    // Should print 'Welcome'
foo();    // Should print 3.1415
foo();    // Should print [1, 2, 3]

As written, this code will raise an error on line 5.
Without modifying the function definition of foo, update this code to print the desired text.
*/

function foo(bar) {
  console.log(bar());
}

function returnWelcome() {
  return 'Welcome';
}

function returnPi() {
  return 3.1415;
}

function returnArray() {
  return [1, 2, 3];
}

foo(returnWelcome);    // Should print 'Welcome'
foo(returnPi);    // Should print 3.1415
foo(returnArray);    // Should print [1, 2, 3]

/*
Q14:
Identify all of the variables, object property names, primitive values, and objects shown in the following code
(assume the code has not been executed).
Don't panic if you miss a few items - this exercise is more challenging than it looks.

function hello(greeting, name) {
  return greeting + ' ' + name;
}

function xyzzy() {
  return { a: 1, b: 2, c: [3, 4, 5], d: {} };
}

const howdy = hello('Hi', 'Grace');
let foo = xyzzy();



Variables:
- hello
- greeting
- name
- xyzzy
- howdy
- foo

Object property names:
- a
- b
- c
- d
- MISSED: 0, 1, 2 for array indices!

Primitive values:
- 1
- 2
- 'Hi'
- ' '
- 'Grace'
- MISSED: 3, 4, and 5 themselves!
- MISSED: 'a', 'b', 'c', 'd', 0, 1, 2 since object property names are primitives here

Objects:
- [3, 4, 5]
- {}
- MISSED: { a: 1, b: 2, c: [3, 4, 5], d: {} }

*/

/*
Q15:
Identify all of the variables, object property names, primitive values, and objects in the following code.
This problem is even more challenging than the previous one.

function bar(arg1, arg2) {
  let foo = 'Hello';
  const qux = {
    abc: [1, 2, 3, [4, 5, 6]],
    def: null,
    ghi: NaN,
    jkl: foo,
    mno: arg1,
    pqr: arg2,
  };

  return qux;
}

let result = bar('Victor', 'Antonina');


Variables:
- bar
- arg1
- arg2
- foo
- qux
- result

Object property names:
- abc
- Array indices:
  - 0, 1, 2, 3 for the outer list for value of `abc`
  - 0, 1, 2 for the nested list in the value for `abc`
- def
- ghi
- jkl
- mno
- pqr

Primitive values:
- 'Hello'
- Inside abc's value: 1, 2, 3, 4, 5, 6
- null
- NaN
- 'Victor'
- 'Antonina'
- Object property names: abc, def, ghi, jkl, mno, pqr, 0, 1, 2, 3, 0, 1, 2

Objects:
- {
    abc: [1, 2, 3, [4, 5, 6]],
    def: null,
    ghi: NaN,
    jkl: foo,
    mno: arg1,
    pqr: arg2,
  }
- [1, 2, 3, [4, 5, 6]]
- [4, 5, 6]
- MISSED: The `bar` function itself!

*/
