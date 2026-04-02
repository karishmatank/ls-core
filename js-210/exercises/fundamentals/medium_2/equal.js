/*
Read through the following code. Currently, it does not log the expected result.
Explain why this happens, then refactor the code so that it works as expected.
*/

const person = { name: 'Victor' };
const otherPerson = { name: 'Victor' };

console.log(person === otherPerson);    // false -- expected: true

/*
This doesn't log true because in JavaScript, we use identity-based equality when comparing two objects.
Because `person` and `otherPerson` aren't referencing the same exact object in memory, the equality will result
in false.

Below is an attempt to refactor the code so that we check that both objects have the same properties and
associated values:
*/

function areObjectsEqual(obj1, obj2) {
  if (Object.keys(obj1).length !== Object.keys(obj2).length) return false;

  for (let key in obj1) {
    if (!Object.keys(obj2).includes(key)) return false;
    if (obj1[key] !== obj2[key]) return false;
  }

  return true;
}

console.log(areObjectsEqual(person, otherPerson));
