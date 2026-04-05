/*
You have written basic functions to display a random greeting to any number
of friends upon each invocation of greet.
Upon invoking the greet function, however, the output is not as expected.
Figure out why not and fix the code.
*/

function randomGreeting() {
  const words = ['Hello', 'Howdy', 'Hi', 'Hey there', 'What\'s up',
                 'Greetings', 'Salutations', 'Good to see you'];

  const idx = Math.floor(Math.random() * words.length);

  words[idx];
}

function greet(...args) {
  const names = Array.prototype.slice.call(args);

  for (let i = 0; i < names.length; i++) {
    const name = names[i];
    const greeting = randomGreeting;

    console.log(`${greeting}, ${name}!`);
  }
}

greet('Hannah', 'Jose', 'Beatrix', 'Julie', 'Ian');

/*
I believe the issue here is that we are not invoking randomGreeting within the body of greet.
`greeting` simply references the function.
Therefore, when we later print `greeting` to the console as part of line 24, we'll print
the function that greeting references.

Even if we did fix that, we would still have an issue within `randomGreeting`, as we don't
explicitly return the element from `words` that will represent the greeting.
Therefore, even if we fixed line 22 to be `const greeting = randomGreeting();`, `greeting`
would always be assigned `undefined`, and we would then always get `undefined, [name]!`.

Therefore, there are two fixes:
- Line 22- `const greeting = randomGreeting();`
- Line 14- `return words[idx];`
*/