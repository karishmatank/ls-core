/*
In this exercise, you'll build a simple inventory management system composed of three components:

Item Creator – validates and constructs item objects.
Item Manager – manages the collection of items (create, update, delete, query).
Report Manager – generates reports for individual items or for all items.

Component Specifications

Item Creator:

The item creator is responsible for validating data and constructing new items.

Each item must have the following properties:

SKU Code — A unique identifier generated from the item name and category.
It consists of the first 3 letters of the item name and the first 2 letters of the category.
If the item name has two words and the first word has only two letters, the next letter is taken from the second word.
All letters in the SKU code are uppercase.
Item Name — Must contain at least 5 non-space characters.
Category — Must be a single word with at least 5 characters.
Quantity — Must be provided (you may assume a valid number is supplied).
If any of these validations fail, the item creator returns an object with a single property: { notValid: true }

If all validations pass, it returns a plain object with the four properties listed above (skuCode, itemName, category,
quantity). Item objects should not include any additional properties or methods.

Item Manager:

The item manager is responsible for maintaining and manipulating the collection of items. It exposes the following:

items — A property containing a list (array) of all item objects.
create(itemName, category, quantity) — Uses the item creator to validate and create a new item.
If creation succeeds, the new item is added to the collection.
If creation fails, this method returns false.
update(skuCode, itemInfo) — Updates any information on an existing item (assume valid values).
delete(skuCode) — Removes the item with the given SKU code from the list (assume valid SKU).
inStock() — Returns a list of all items with a quantity greater than 0.
itemsInCategory(category) — Returns a list of all items belonging to the given category.
Report Manager:

The report manager is responsible for generating reports about items. It exposes the following methods:

init(itemManager) — Accepts the ItemManager object and stores it for later use.
createReporter(skuCode) — Returns a reporter object for the given SKU code.
The returned object has one method, itemInfo(), which logs each property of the item as "key: value" (one per line).
The reporter object should not have any other properties or methods (other than those from Object.prototype).
reportInStock() — Logs a comma-separated list of item names that are currently in stock.
Notes:

You don’t need to enforce unique SKU codes; duplicates are allowed under this spec.
Each required piece of information for an item corresponds to one property.
If invalid information is provided, the item creator returns { notValid: true }, and the item manager’s create method
returns false.
You may add helper methods to ItemManager as needed.
*/

function itemCreator(itemName, category, quantity) {
  let isItemNameValid = (name) => {
    name = name.replace(/\s/g, '');
    return name.length >= 5;
  };

  let isCategoryValid = (name) => {
    if (name.split(/\s+/g).length > 1) return false;
    return name.length >= 5;
  };

  let isQuantityValid = (number) => {
    return number !== undefined;
  };

  if (!isItemNameValid(itemName) || !isCategoryValid(category) || !isQuantityValid(quantity)) {
    return { notValid: true };
  }

  return {
    skuCode: (itemName.replace(/\s/g, '').slice(0, 3) + category.slice(0, 2)).toUpperCase(),
    itemName,
    category,
    quantity,
  };
}

let ItemManager = {
  items: [],
  create(itemName, category, quantity) {
    let newItem = itemCreator(itemName, category, quantity);
    if (newItem.notValid) {
      return false;
    }
    this.items.push(newItem);
  },
  update(skuCode, itemInfo) {
    let item = this.items.find(item => item.skuCode === skuCode);
    if (item === undefined) {
      return;
    }
    for (let field in itemInfo) {
      item[field] = itemInfo[field];
    }
  },
  delete(skuCode) {
    this.items = this.items.filter(item => item.skuCode !== skuCode);
  },
  inStock() {
    return this.items.filter(item => item.quantity > 0);
  },
  itemsInCategory(category) {
    return this.items.filter(item => item.category === category);
  },
};

let ReportManager = function() {
  let itemManager = null;

  return {
    init(manager) {
      itemManager = manager;
    },
    createReporter(skuCode) {
      return {
        itemInfo() {
          let item = itemManager.items.find(item => item.skuCode === skuCode);
          for (let prop in item) {
            console.log(`${prop}: ${item[prop]}`);
          }
        },
      };
    },
    reportInStock() {
      console.log(itemManager.inStock().map(item => item.itemName).join(', '));
    },
  };
}();


ItemManager.create('basket ball', 'sports', 0);       // valid
ItemManager.create('asd', 'sports', 0);               // invalid (too short)
ItemManager.create('soccer ball', 'sports', 5);       // valid
ItemManager.create('football', 'sports');             // invalid (no quantity)
ItemManager.create('football', 'sports', 3);          // valid
ItemManager.create('kitchen pot', 'cooking items', 0);// invalid (category has space)
ItemManager.create('kitchen pot', 'cooking', 3);      // valid

console.log(ItemManager.items);
// => list with 4 valid items

ReportManager.init(ItemManager);
ReportManager.reportInStock();
// logs: soccer ball,football,kitchen pot

ItemManager.update('SOCSP', { quantity: 0 });
console.log(ItemManager.inStock());
// => football, kitchen pot

ReportManager.reportInStock();
// logs: football,kitchen pot

console.log(ItemManager.itemsInCategory('sports'));
// => basket ball, soccer ball, football

ItemManager.delete('SOCSP');
console.log(ItemManager.items);
// => remaining 3 valid items (soccer ball removed)

const kitchenPotReporter = ReportManager.createReporter('KITCO');
kitchenPotReporter.itemInfo();
// logs:
// skuCode: KITCO
// itemName: kitchen pot
// category: cooking
// quantity: 3

ItemManager.update('KITCO', { quantity: 10 });
kitchenPotReporter.itemInfo();
// logs:
// skuCode: KITCO
// itemName: kitchen pot
// category: cooking
// quantity: 10