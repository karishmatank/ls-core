/*
Create a function that constructs a new object with a log method that is read-only.
The log method will use console.log to output the name property on itself.
*/

function newPerson(name) {
  let newObj = { name };
  Object.defineProperties(newObj, {
    log: {
      value: function() {
        console.log(name);
      },
      writable: false,
    },
  });
  return newObj;
}

let me = newPerson('Shane Riley');
me.log();     // => Shane Riley
me.log = function() { console.log('Amanda Rose'); }; // Errors in strict mode
me.log();     // => Shane Riley