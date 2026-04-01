/*
Write a function named objectHasProperty that takes two arguments: an Object and a String.
The function should return true if the Object contains a property with the name given by the String,
false otherwise.
*/

function objectHasProperty(obj, str) {
  return Object.keys(obj).includes(str);
}

// It's better to do the above rather than something like `return obj[str] === undefined`.
// The issue with that is- what happens if there is an actual undefined value in the object?

let pets = {
  cat: 'Simon',
  dog: 'Dwarf',
  mice: null,
};

console.log(objectHasProperty(pets, 'dog'));       // true
console.log(objectHasProperty(pets, 'lizard'));    // false
console.log(objectHasProperty(pets, 'mice'));      // true

/*
Write a function named incrementProperty that takes two arguments: an Object and a String.
If the Object contains a property with the specified name, the function should increment the value of that property.
If the property does not exist, the function should add a new property with a value of 1.
The function should return the new value of the property.
*/

function incrementProperty(obj, str) {
  // Could have also used the objectHasProperty function from above
  if (Object.keys(obj).includes(str)) {
    obj[str] += 1;
  } else {
    obj[str] = 1;
  }
  return obj[str];
}

let wins = {
  steve: 3,
  susie: 4,
};

console.log(incrementProperty(wins, 'susie'));   // 5
console.log(wins);                               // { steve: 3, susie: 5 }
console.log(incrementProperty(wins, 'lucy'));    // 1
console.log(wins);                               // { steve: 3, susie: 5, lucy: 1 }

/*
Write a function named copyProperties that takes two Objects as arguments.
The function should copy all properties from the first object to the second.
The function should return the number of properties copied.
*/

function copyProperties(obj1, obj2) {
  for (let key in obj1) {
    obj2[key] = obj1[key];
  }
  return Object.keys(obj1).length;
}

let hal = {
  model: 9000,
  enabled: true,
};

let sal = {};
console.log(copyProperties(hal, sal));  // 2
console.log(sal);                       // { model: 9000, enabled: true }


/*
Write a function named wordCount that takes a single String as an argument.
The function should return an Object that contains the counts of each word that appears in the provided String.
In the returned Object, you should use the words as keys, and the counts as values.
*/

function wordCount(str) {
  let words = str.split(' ');
  let counts = {};

  for (let word of words) {
    incrementProperty(counts, word);
  }

  return counts;
}

console.log(wordCount('box car cat bag box'));  // { box: 2, car: 1, cat: 1, bag: 1 }
