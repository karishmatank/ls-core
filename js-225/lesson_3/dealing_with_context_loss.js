/*
Our desired output for the code below is: Christopher Turk is a Surgeon.
What will the code output, and what explains the difference, if any, between the actual and desired outputs?
*/

let turk = {
  firstName: 'Christopher',
  lastName: 'Turk',
  occupation: 'Surgeon',
  getDescription() {
    return this.firstName + ' ' + this.lastName + ' is a ' + this.occupation + '.';
  }
};

function logReturnVal(func) {
  let returnVal = func();
  console.log(returnVal);
}

logReturnVal(turk.getDescription);

/*
This will print (in sloppy mode):
undefined undefined is a undefined.

In strict mode, it will error out.

The reason is because we lose context when we invoke the function within `logReturnVal`. When we invoke it, `this`
references the `window` or `global` object instead.
*/

/*
Alter logReturnVal such that it takes an additional context argument,
and use one of the methods we've learned in this lesson to invoke func inside of logReturnVal
with context as its function execution context.
Alter the invocation of logReturnVal and supply turk as the context argument.
*/

let turk = {
  firstName: 'Christopher',
  lastName: 'Turk',
  occupation: 'Surgeon',
  getDescription() {
    return this.firstName + ' ' + this.lastName + ' is a ' + this.occupation + '.';
  }
};

function logReturnVal(func, context) {
  let returnVal = func.call(context);
  console.log(returnVal);
}

logReturnVal(turk.getDescription, turk);


/*
Suppose that we want to extract getDescription from turk, but always have it execute with turk as context.
Use one of the methods we've learned in the last lesson to assign such a permanently bound function to a new variable,
getTurkDescription.
*/

let getTurkDescription = turk.getDescription.bind(turk);

/*
Consider the code below, and our desired output:
*/

let TESgames = {
  titles: ['Arena', 'Daggerfall', 'Morrowind', 'Oblivion', 'Skyrim'],
  seriesTitle: 'The Elder Scrolls',
  listGames() {
    this.titles.forEach(function(title) {
      console.log(this.seriesTitle + ' ' + title);
    });
  }
};

TESgames.listGames();

/*
Desired output:
The Elder Scrolls Arena
The Elder Scrolls Daggerfall
The Elder Scrolls Morrowind
The Elder Scrolls Oblivion
The Elder Scrolls Skyrim
*/

/*
Will this code log our desired output? Why or why not?


No, because `this` inside of the callback function invoked within `forEach` references the `window` or
`global` object, which won't have a `seriesTitle` property.

*/

/*
Use an arrow function so that the code logs our desired output.
*/

let TESgames = {
  titles: ['Arena', 'Daggerfall', 'Morrowind', 'Oblivion', 'Skyrim'],
  seriesTitle: 'The Elder Scrolls',
  listGames() {
    this.titles.forEach(title => {
      console.log(this.seriesTitle + ' ' + title);
    });
  }
};

TESgames.listGames();

/*
Use the let self = this fix to alter TESgames.listGames such that it logs our desired output to the console.
*/

let TESgames = {
  titles: ['Arena', 'Daggerfall', 'Morrowind', 'Oblivion', 'Skyrim'],
  seriesTitle: 'The Elder Scrolls',
  listGames() {
    let self = this;
    this.titles.forEach(function(title) {
      console.log(self.seriesTitle + ' ' + title);
    });
  }
};

TESgames.listGames();

/*
If we don't want to rely on let self = this,
forEach provides us with an alternative means of supplying execution context to the inner function.
Use this means to achieve our desired output.
*/

let TESgames = {
  titles: ['Arena', 'Daggerfall', 'Morrowind', 'Oblivion', 'Skyrim'],
  seriesTitle: 'The Elder Scrolls',
  listGames() {
    this.titles.forEach(function(title) {
      console.log(this.seriesTitle + ' ' + title);
    }, this);
  }
};

TESgames.listGames();

/*
Consider the code below:
*/

let foo = {
  a: 0,
  incrementA() {
    function increment() {
      this.a += 1;
    }

    increment();
  }
};

foo.incrementA();
foo.incrementA();
foo.incrementA();

/*
What will the value of foo.a be after this code has executed?
*/

/*
It's value will be 0. In sloppy mode, we end up creating a property `a` in the `global` or `window` object
whose value will be NaN after each invocation of `incrementA`. It doesn't affect `foo.a` at all.
*/

/*
Use one of the methods we learned in this lesson to invoke increment with explicit context such that
foo.a is incremented with each invocation of incrementA.
*/

let foo = {
  a: 0,
  incrementA() {
    function increment() {
      this.a += 1;
    }

    increment.call(this);
  }
};

foo.incrementA();
foo.incrementA();
foo.incrementA();

console.log(foo.a);

/*
We decide that we want each invocation of foo.incrementA to increment foo.a by 3, rather than 1,
and alter our code accordingly:
*/

let foo = {
  a: 0,
  incrementA() {
    function increment() {
      this.a += 1;
    }

    increment.apply(this);
    increment.apply(this);
    increment.apply(this);
  }
};

/*
Calling apply three times seems repetitive, though. Use bind to permanently set foo as increment's execution context.
*/
let foo = {
  a: 0,
  incrementA() {
    function increment() {
      this.a += 1;
    }

    increment = increment.bind(this);
    for (let i = 0; i < 3; i += 1) {
      increment();
    }
  }
};

foo.incrementA();
console.log(foo.a);

