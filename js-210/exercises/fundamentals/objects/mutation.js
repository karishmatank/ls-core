/*
What will the following code log to the console and why? Don't run the code until after you have tried to answer.
*/

const array1 = ['Moe', 'Larry', 'Curly', 'Shemp', 'Harpo', 'Chico', 'Groucho', 'Zeppo'];
const array2 = [];

for (let i = 0; i < array1.length; i += 1) {
  array2.push(array1[i]);
}

for (let i = 0; i < array1.length; i += 1) {
  if (array1[i].startsWith('C')) {
    array1[i] = array1[i].toUpperCase();
  }
}

console.log(array2);

/*
I believe this will log:
['Moe', 'Larry', 'Curly', 'Shemp', 'Harpo', 'Chico', 'Groucho', 'Zeppo']

In the first for loop, we take each element of array1 and add it to array2.
Even though we then reassign elements of array1, those have no bearing on array2 as strings are immutable.
*/