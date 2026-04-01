/*
Identify the bug in the following code. Don't run the code until after you've tried to answer.
*/

const myObject = {
  a: 'name',
  'b': 'test',
  123: 'c',
  1: 'd',
};

myObject[1];
myObject[a];
myObject.a;

/*
The bug is on the line `myObject`, as we're trying to find a key of `1`, but we'll only find keys of
`'a'`, `'b'`, `'123'`, and `'1'`. The key is in string form, whereas we are trying to find an integer key.

EDIT: Nope! The issue is that we have `myObject[a]` on line 2, which will try to find a variable `a`
which doesn't exist.

myObject[1] actually works. With bracket notation, JavaScript evaluates the expression inside the
brackets first. Here, 1 is a number, so JS converts it to a string '1' before using it as a property key.
Since the object has a key '1', this returns 'd'.
*/