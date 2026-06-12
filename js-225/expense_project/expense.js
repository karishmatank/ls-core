"use strict";

/*
Create a system to track expenses.

Rules:
- Our system will have 3 components- expenses, an expense manager, and a budget expense manager
- Expenses
  Input: amount, date, category
  Output: Object with 4 properties: unique id, amount, date, and category

  Rules:
  - Each expense represents a single record
  - The date can't be a future date
  - The amount must be positive
  - The category must be a non-empty string
  - Each expense is immutable once created
  - Assume the id can't be provided directly by the user- our program will handle creating unique ids

  Data structures: Objects for each record

  Algorithm:
  - We'll use class syntax to set up an Expense class
  - Private variables- #id, #amount, #date, #category
  - Private static method to get the next id, implemented as an IIFE -> `getNextId`
    - Initialize a variable `lastID` to 0
    - Return a function that closes over the nonlocal `lastID`, increments it by 1, and returns the new value
  - Constructor method:
    - Use `getNextId` to set the private #id value
    - Use "one-time setters" for amount, date, category (see below)
  - Getters only for amount, date, category - each will return the value of #amount, #date, #category, respectively
  - Private methods to serve as "one-time setters":
    - #setAmount
      - Check if new value is > 0. If so, set the value of #amount. Otherwise, raise Error
    - #setDate
      - Check if new value is on or before current date. If so, set the value of #date. If not, raise Error
    - #setCategory
      - Check if category is a non-empty string. If not, raise Error

- Expense managers
  - A single expense manager has a collection of expenses
  - We must be able to:
    - Add a new expense
    - Remove an expense by id
    - Summarize expenses (total spent, average amount, count)
    - Filter expenses by a date range
    - Filter expenses by category
    - Add a new allowed category
    - Retrieve the current list of allowed categories
  - Default allowed categories are: Food, Housing, Transportation, Entertainment, and Health
  - All expenses must belong to an allowed category
  - Assume we should not allow a user to access the collection of expenses directly
- Budget expense manager
  - Provides similar behavior to an expense manager but includes a budget limit
  - The manager must prevent adding expenses that would cause the total to exceed the budget
  - Must show a summary of how much of the budget has been used and how much of the budget remains

*/

class Expense {
  #id
  #amount
  #date
  #category

  constructor(amount, date, category) {
    this.#id = Expense.#getNextId();
    this.#setAmount(amount);
    this.#setDate(date);
    this.#setCategory(category);
    Object.freeze(this); // Ensures we can't add any new properties to the object
  }

  static #getNextId = (function() {
    let lastID = 0;
    return function() {
      lastID += 1;
      return lastID;
    };
  })();

  get id() {
    return this.#id;
  }

  get date() {
    // NOTE: Dates are objects, so they can be mutated if we just return this.#date!
    return new Date(this.#date);
  }

  get amount() {
    return this.#amount;
  }

  get category() {
    return this.#category;
  }

  #setAmount(newAmount) {
    if (newAmount <= 0) {
      throw new Error('Amount must be positive.');
    }

    this.#amount = newAmount;
  }

  #setDate(newDate) {
    let today = new Date();

    // Check if date passed in is a string or a Date object
    // If date is a string, convert to Date object
    if (typeof(newDate) === 'string') {
      newDate = new Date(newDate);
    }

    if (newDate > today) {
      throw new Error("Date can't be in the future.");
    }

    this.#date = newDate;
  }

  #setCategory(newCategory) {
    if (newCategory.trim() === '') {
      throw new Error("Category can't be an empty string.");
    }

    this.#category = newCategory.trim().toLowerCase();
  }
}


class ExpenseManager {
  #expenses
  #allowedCategories;

  constructor() {
    this.#expenses = [];
    this.#allowedCategories = ['food', 'housing', 'transportation', 'entertainment', 'health'];
    Object.freeze(this);
  }

  get expenses() {
    return [...this.#expenses];
  }

  add(amount, date, category) {
    let normalizedCategory = category.trim().toLowerCase();
    if (!this.#allowedCategories.includes(normalizedCategory)) {
      throw new Error('Category must be one of: ' + this.#allowedCategories.join(', '));
    }
    try {
      this.#expenses.push(new Expense(amount, date, normalizedCategory));
    } catch (error) {
      throw new Error(`Failed to add expense: ${error}`);
    }
  }

  remove(expenseId) {
    let expense = this.#expenses.find(expense => expense.id === expenseId);
    let idx = this.#expenses.indexOf(expense);
    this.#expenses.splice(idx, 1);
  }

  summary() {
    // Total spent, average amount, count
    let totalSpent = this.#expenses.reduce((acc, expense) => acc + expense.amount, 0);
    let count = this.#expenses.length;
    let averageAmount = count === 0 ? 0 : totalSpent / count;
    return { totalSpent, count, averageAmount };
  }

  filterByDates(dateStart, dateEnd) {
    return this.#expenses.filter(expense => expense.date >= new Date(dateStart) && expense.date <= new Date(dateEnd));
  }

  filterByCategory(category) {
    category = category.trim().toLowerCase();
    return this.#expenses.filter(expense => expense.category === category);
  }

  addNewAllowedCategory(newCategory) {
    if (newCategory.trim().toLowerCase() === '') {
      throw new Error('Category name should not be empty');
    }
    this.#allowedCategories.push(newCategory.toLowerCase());
  }

  getAllowedCategories() {
    return [...this.#allowedCategories];
  }
}


class BudgetExpenseManager extends ExpenseManager {
  #budget;

  constructor(budget) {
    super();

    if (budget < 0) {
      throw new Error('Budget must be positive.');
    }
    this.#budget = budget;
  }

  add(amount, date, category) {
    let { total } = this.summary();
    if ((total + amount) > this.#budget) {
      throw new Error('Expense not added, expense total would go over budget.');
    }
    super.add(amount, date, category);
  }

  summary() {
    let summaryObj = super.summary();
    summaryObj['budgetLimit'] = this.#budget;
    summaryObj['budgetRemaining'] = this.#budget - summaryObj['totalSpent'];
    return summaryObj;
  }
}






// Testing

console.log(' ====== Part 1: Expenses ====== ');

// Happy path
console.log('Test 1: Happy path');
let expense = new Expense(50, '2025-01-01', 'Health');
console.log(expense.id); // prints 1
console.log(expense.amount); // prints 50
console.log(expense.date); // prints Date object representing 1/1/25
console.log(expense.category); // prints Health
console.log('*****');

// Confirm we can't manually set the id
console.log('Test 2: Manual reset does not work');
try {
  expense.id = 55;
} catch(error) {
  console.log("Error caught!");
}

console.log(expense.id); // prints 1

// Confirm we can't manually change the amount
try {
  expense.amount = 100;
} catch(error) {
  console.log("Error caught!");
}
console.log(expense.amount); // prints 50
console.log('*****');

// Confirm that a new expense automatically gets the next ID in line (id of 2)
console.log('Test 3: Test that ID of new Expense object gets the next ID value in line');
let expense2 = new Expense(3, '2025-01-01', 'Food');
console.log(expense2.id); // prints 2
console.log('*****');

// Confirm guard rails
console.log('Test 4: Test that amount can not be 0 or negative');
try {
  new Expense(-5, '2025-01-01', 'Health');
} catch (error) {
  console.log(error.message) // should print this error. "Amount must be positive."
}
console.log('*****');

console.log('Test 5: Test that date can not be in the future');
try {
  new Expense(50, '2027-01-01', 'Health');
} catch (error) {
  console.log(error.message) // should print this error. "Date can't be in the future."
}
console.log('*****');

console.log('Test 6: Test that category does not allow empty string');
try {
  new Expense(50, '2025-01-01', '   ');
} catch (error) {
  console.log(error.message) // should print this error. "Category can't be an empty string."
}
console.log('*****');



