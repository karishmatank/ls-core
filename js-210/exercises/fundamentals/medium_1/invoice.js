/*
The invoiceTotal function in the code below computes the total amount for an invoice containing four "line items".
How can you refactor the function so that it will work with invoices containing any number of line items?
*/

function invoiceTotal(amount1, amount2, amount3, amount4) {
  return amount1 + amount2 + amount3 + amount4;
}

console.log(invoiceTotal(20, 30, 40, 50));          // works as expected
console.log(invoiceTotal(20, 30, 40, 50, 40, 40));  // does not work; how can you make it work?

/*
We can use the rest parameter:
*/

function invoiceV2(...amounts) {
  return amounts.reduce((accumulator, number) => accumulator + number, 0);
}

console.log(invoiceV2(20, 30, 40, 50));
console.log(invoiceV2(20, 30, 40, 50, 40, 40));