/*
The processOrder function shown below accepts the following arguments: price, quantity, discount, serviceCharge and tax.
Any arguments other than price may be omitted when calling the function, in which case, default values will be assigned.
*/

function processOrder(price, quantity, discount, serviceCharge, tax) {
  if (!quantity) {
    quantity = 1;
  }

  if (!discount) {
    discount = 0;
  }

  if (!serviceCharge) {
    serviceCharge = 0.1;
  }

  if (!tax) {
    tax = 0.15;
  }

  return (price * quantity) * (1 - discount) * (1 + serviceCharge) * (1 + tax);
}

processOrder(100);      // 126.5

/*
This function uses conditional statements to test whether arguments have been omitted.
When an argument is omitted, JavaScript automatically initializes it to a value of undefined.
The function takes advantage of this behavior by setting undefined arguments to a default value.

The following variation of the processOrder function has the same behavior as the first:
*/

function processOrder(price, quantity, discount, serviceCharge, tax) {
  quantity = quantity || 1;
  discount = discount || 0;
  serviceCharge = serviceCharge || 0.1;
  tax = tax || 0.15;

  return (price * quantity) * (1 - discount) * (1 + serviceCharge) * (1 + tax);
}

/*
However, both of these solutions have a limitation that can lead to an incorrect result for certain inputs.
What is this limitation and how does it affect the result?
*/


/*
I believe the limitation is based on what values are truthy vs falsy. For example, a user could pass in
a numeric string, which would not be falsy. A user can also pass in an empty object or array, which would also
not be falsy. Thus, the numeric operations may return an unexpected result.


EDIT: Not quite, the issue is that if a user passes in a value of 0 for any of these arguments, we will
interpret it as falsy and reassign the parameter to the default value. However, 0 may be the intended value.
*/
