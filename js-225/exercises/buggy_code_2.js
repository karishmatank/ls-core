/*
A grocery store uses a JavaScript function to calculate discounts on various items.
They are testing out various percentage discounts but are getting unexpected results.
Go over the code, and identify the reason why they aren't getting the expected discounted prices from the function.
Then, modify the code so that it produces the correct results.
*/

const item = {
  name: 'Foo',
  description: 'Fusce consequat dui est, semper.',
  price: 50,
  quantity: 100,
  discount(percent) {
    const discount = this.price * percent / 100;
    this.price -= discount;

    return this.price;
  },
};

console.log(item.discount(20));   // should return 40
// = 40
console.log(item.discount(50));   // should return 25
// = 20
console.log(item.discount(25));   // should return 37.5
// = 15

/*
The issue is that we're reassigning the `price` property of the `item` object to the discounted value each time
we are calling `discount`. That means that on subsequent calls, we are not discounting the original price of 50,
we are discounting the price after the prior discount call.

We should not reassign `this.price`:
*/

const item2 = {
  name: 'Foo',
  description: 'Fusce consequat dui est, semper.',
  price: 50,
  quantity: 100,
  discount(percent) {
    const discount = this.price * percent / 100;
    return this.price - discount;
  },
};

console.log(item2.discount(20));  // should return 40
// = 40
console.log(item2.discount(50));  // should return 25
// = 20
console.log(item2.discount(25));  // should return 37.5
// = 15

