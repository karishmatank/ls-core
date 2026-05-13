/*
The code below is expected to output the following when run:

> const helloVictor = createGreeter('Victor');
> helloVictor.greet('morning');
= Good Morning Victor

However, it instead results in an error. What is the problem with the code? Why isn't it producing the expected results?

*/

function createGreeter(name) {
  return {
    name,
    morning: 'Good Morning',
    afternoon: 'Good Afternoon',
    evening: 'Good Evening',
    greet(timeOfDay) {
      let msg = '';
      switch (timeOfDay) {
        case 'morning':
          msg += `${morning} ${name}`;
          break;
        case 'afternoon':
          msg += `${afternoon} ${name}`;
          break;
        case 'evening':
          msg += `${evening} ${name}`;
          break;
      }

      console.log(msg);
    },
  };
}

/*
The issue is that we're trying to reference a `morning`, `afternoon`, or `evening` variable that doesn't exist.
We need to use `this` to get the respective properties from the object that we're calling the method on.
*/

function createGreeter(name) {
  return {
    name,
    morning: 'Good Morning',
    afternoon: 'Good Afternoon',
    evening: 'Good Evening',
    greet(timeOfDay) {
      let msg = '';
      switch (timeOfDay) {
        case 'morning':
          msg += `${this.morning} ${this.name}`;
          break;
        case 'afternoon':
          msg += `${this.afternoon} ${this.name}`;
          break;
        case 'evening':
          msg += `${this.evening} ${this.name}`;
          break;
      }

      console.log(msg);
    },
  };
}

/*
Further exploration:
An alternative solution to this exercise is the following code:
*/
// rest of code omitted for brevity

      switch (timeOfDay) {
        case 'morning':
          msg += this.morning + ' ' + name;
          break;
        case 'afternoon':
          msg += this.afternoon + ' ' + name;
          break;
        case 'evening':
          msg += this.evening + ' ' + name;
          break;
      }

// rest of code omitted for brevity

// Why does it work? What concept does this demonstrate?

/*
This works because JavaScript will find the name variable defined within the `createGreeter` function,
as `name` is a parameter to the function. The concept here is of closures, as the method remembers the
reference to the non-local `name` variable.
*/