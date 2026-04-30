/*
A 3x3 matrix can be represented by an array of arrays: an outer array containing three subarrays
that each contain three elements. For example, the 3x3 matrix shown below:

1  5  8
4  7  2
3  9  6

is represented by the following array of arrays:

const matrix = [
  [1, 5, 8],
  [4, 7, 2],
  [3, 9, 6],
];

The transpose of a 3x3 matrix is the matrix that results from exchanging the rows and columns of the original matrix.
For example, the transposition of the matrix shown above is:

1  4  3
5  7  9
8  2  6

Write a function that takes an array of arrays that represents a 3x3 matrix and returns the transpose of the matrix.
You should implement the function on your own, without using any external libraries.

Take care not to modify the original matrix — your function must produce a new matrix and leave the input matrix
array unchanged.


My questions:
- Will the elements within the nested arrays always be integers? Does it matter if they aren't?
- Will the array always be square? If it is mxn, will the transpose just be nxm?
- Will all inner arrays have the same length? What happens if they don't?
- Will each inner array always have at least one element?
- What happens if we receive an empty array, or empty nested arrays? What do we return?
- Will any of the arrays / nested arrays be sparse? Will there be any custom properties?
- Will we always receive an array, or might it be another data type?
- Might we receive more than 1 input too or even 0 inputs?
- Does "transpose" mean that the rows essentially become the new columns?


Input: Nested array (matrix)
Output: Nested array (transposed matrix)
Rules:
-

*/

function transpose(matrix) {
  return matrix.reduce((acc, row) => {
    row.forEach((col, colIdx) => {
      acc[colIdx] = acc[colIdx] ?? [];
      acc[colIdx].push(col);
    });
    return acc;
  }, []);
}


const matrix = [
  [1, 5, 8],
  [4, 7, 2],
  [3, 9, 6]
];

const newMatrix = transpose(matrix);

console.log(newMatrix);      // [[1, 4, 3], [5, 7, 9], [8, 2, 6]]
console.log(matrix);         // [[1, 5, 8], [4, 7, 2], [3, 9, 6]]
