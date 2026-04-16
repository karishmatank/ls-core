function multiplyAllPairs(numArr1, numArr2) {
  let products = [];
  numArr1.forEach(num => {
    numArr2.forEach(num2 => {
      products.push(num * num2);
    });
  });

  return products.sort((a, b) => a - b);
}

console.log(multiplyAllPairs([2, 4], [4, 3, 1, 2]));    // [2, 4, 4, 6, 8, 8, 12, 16]