function totalArea(arr) {
  return arr.reduce((accumulator, [ height, width ]) => {
    return accumulator + (height * width);
  }, 0);
}

let rectangles = [[3, 4], [6, 6], [1, 8], [9, 9], [2, 2]];

console.log(totalArea(rectangles));    // 141


function totalSquareArea(arr) {
  let squares = arr.filter(([ height, width ]) => height === width);
  return totalArea(squares);
}

console.log(totalSquareArea(rectangles));    // 121