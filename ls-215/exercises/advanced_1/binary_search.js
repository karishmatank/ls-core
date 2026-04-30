/*
Implement a binarySearch function that takes an array and a search item as arguments,
and returns the index of the search item if found, or -1 otherwise.
You may assume that the array argument will always be sorted.
*/

function binarySearch(arr, searchTerm) {
  if (arr.length === 0) {
    return -1;
  }
  let halfway = Math.floor(arr.length / 2);
  if (arr[halfway] === searchTerm) {
    return halfway;
  }
  else if (arr[halfway] < searchTerm) {
    let result = binarySearch(arr.slice(halfway + 1), searchTerm);
    return result === -1 ? result : (halfway + 1 + result);
  } else {
    return binarySearch(arr.slice(0, halfway), searchTerm);
  }

}

const yellowPages = ['Apple Store', 'Bags Galore', 'Bike Store', 'Donuts R Us', 'Eat a Lot', 'Good Food',
  'Pasta Place', 'Pizzeria', 'Tiki Lounge', 'Zooper'];

console.log(binarySearch(yellowPages, 'Pizzeria'));                   // 7


/*
1st run- halfway = 5 => line 16 binarySearch(['Pasta Place', 'Pizzeria', 'Tiki Lounge', 'Zooper']) => return 5 + 1 + 1
2nd run- halfway = 2 => line 19 binarySearch(['Pasta Place', 'Pizzeria']) => return 1
3rd run- halfway = 1 => return 1
*/



console.log(binarySearch(yellowPages, 'Apple Store'));                // 0

console.log(binarySearch([1, 5, 7, 11, 23, 45, 65, 89, 102], 77));    // -1
console.log(binarySearch([1, 5, 7, 11, 23, 45, 65, 89, 102], 89));    // 7
console.log(binarySearch([1, 5, 7, 11, 23, 45, 65, 89, 102], 5));     // 1

console.log(binarySearch(['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue', 'Tyler'], 'Peter'));  // -1
console.log(binarySearch(['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue', 'Tyler'], 'Tyler'));  // 6