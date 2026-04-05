/*
Run the following code. Why is every warning displayed twice?
Change the code so that each warning is displayed only once, as intended.
*/

const species = ['wolf', 'human', 'wasp', 'squirrel', 'weasel', 'dinosaur'];
const isMidnight = true;
const isFullmoon = true;

function isTransformable(species) {
  return species[0] === 'w';
}

function transform(species) {
  return `were${species}`;
}

for (let index = 0; index < species.length; index++) {
  const thisSpecies = species[index];
  var newSpecies;

  if (isMidnight && isFullmoon && isTransformable(thisSpecies)) {
    newSpecies = transform(thisSpecies);
  }

  if (newSpecies) {
    console.log(`Beware of the ${newSpecies}!`);
  }
}

/*

The issue is that we've used var to declare `newSpecies`.
`var` is function scoped, which means this code is as good as "hoisting" the
declaration for `newSpecies` up to the top of the program, where newSpecies
is initialized to `undefined`.
For the first loop, we'll reassign `newSpecies` to `werewolf`, which will
log `Beware of the werewolf`.
However, during the second loop, since `isTransformable('human')` returns false,
we don't reassign `newSpecies`.
`newSpecies` is still `werewolf` by the time we get to line 26, which re-logs
the same error we just logged during the prior loop.

The fix here is not to use `var` to declare `newSpecies` but `let`. That way,
`newSpecies` would be block scoped and essentially "refreshed" for each loop.
*/
