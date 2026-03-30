let myArray = [1, 2, 3, 4];
const myOtherArray = myArray;

myArray.pop();
console.log(myArray);
console.log(myOtherArray);

myArray = [1, 2];
console.log(myArray);
console.log(myOtherArray);

/*
Read through the code shown above. What does it log to the console at lines 5, 6, 9, and 10?

This will print:
[1, 2, 3]
[1, 2, 3]
[1, 2]
[1, 2, 3]

On line 2, we assign myOtherArray a reference to the array that myArray is pointing to.
Thus, when we then mutate that array on line 4 using `pop`, it will be reflected when we reference
either `myArray` or `myOtherArray`.

We then reassign `myArray` to reference another array. When we subsequently log `myArray` to the console, we'll
see that second array instead, whereas `myOtherArray` still references the original array.
*/