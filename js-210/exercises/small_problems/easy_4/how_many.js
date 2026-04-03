/*
Write a function that counts the number of occurrences of each element in a given array.
Once counted, log each element alongside the number of occurrences.
*/

function countOccurrences(arr) {
  let counts = {};
  for (let element of arr) {
    counts[element] = counts[element] || 0;
    counts[element] += 1;
  }

  Object.keys(counts).forEach((word) => console.log(`${word} => ${counts[word]}`));
}

const vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
                'motorcycle', 'suv', 'motorcycle', 'car', 'truck'];

countOccurrences(vehicles);

// console output
// car => 4
// truck => 3
// SUV => 1
// motorcycle => 2
// suv => 1
