function buyFruit(groceryList) {
  return groceryList.reduce((acc, [ fruit, quantity ]) => {
    for (let i = 0; i < quantity; i += 1) {
      acc.push(fruit);
    }
    return acc;
  }, []);
}

console.log(buyFruit([['apple', 3], ['orange', 1], ['banana', 2]]));
// returns ["apple", "apple", "apple", "orange", "banana", "banana"]