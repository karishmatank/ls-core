/*
One of the ways to manage the flow of a program is through the use of conditionals.
Go over the code below and specify how many unique execution paths are possible.
*/

if (condition1) {
  // ...
  if (condition2) {
    // ...
  } else {
    // ...
  }
} else {
  // ...
  if (condition4) {
    // ...
    if (condition5) {
    // ...
    }
  }
}

/*
If condition1 is truthy, then there are 2 paths to start based on whether condition2 is truthy or not
If condition1 is falsy, then there are 2 paths again based on whether condition4 is truthy or not
If condition4 is truthy, then either we'll execute the if block or not based on whether condition5 is truthy or not

1. condition1 is truthy => condition2 is truthy
2. condition1 is truthy => condition2 is falsy
3. condition1 is falsy => condition4 is truthy => condition5 is truthy
4. condition1 is falsy => condition4 is truthy => condition5 is falsy
5. condition1 is falsy => condition4 is falsy

5 paths
*/
