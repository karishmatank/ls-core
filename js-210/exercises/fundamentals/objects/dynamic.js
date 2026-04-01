/*
What will the following code log to the console and why? Don't run the code until after you have tried to answer.
*/

const myObject = {
  prop1: '123',
  prop2: '234',
  'prop 3': '345',
};

const prop2 = '456';
myObject['prop2'] = '456';
myObject[prop2] = '678';

console.log(myObject[prop2]);
console.log(myObject.prop2);

/*
This will print:
678
456

`myObject` at the end of line 13 looks like:

const myObject = {
  prop1: '123',
  prop2: '456',
  'prop 3': '345',
  '456': '678',
};

The constant `prop2` declared in the local scope is independent of the key `prop2` within `myObject`.
`myObject['prop2']` references the key 'prop2' in `myObject`.
`myObject[prop2]` resolves essentially to `myObject['456']` as JS will look for the prop2 variable
That key doesn't exist in `myObject`, so we add a new key-value pair with key `'456'` and value `'678'`
*/


/*
Here is another example. What do you think will be logged to the console this time, and why?
*/

const myObj = {};
myObj[myFunc()] = 'hello, ';

function myFunc() {
  return 'funcProp';
}

console.log(myObj);
myObj[myFunc()] = 'world!';
console.log(myObj);

/*
This will print:
{ 'funcProp': 'hello, ' }
{ 'funcProp': 'world!' }

The function definition is hoisted, so it is available when we call myFunc() on the second line.
myFunc() returns 'funcProp' always, so JS will look for a key 'funcProp' within `myObj`, which it won't find,
thus it will create a new key-value pair with value 'hello, '
Later on, we reassign the value of that same key to 'world!', which is why the object will look different
when we log it the second time around.
*/