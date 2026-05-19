function makeAccount(number) {
  let balance = 0;
  let transactions = [];

  return {
    deposit(amount) {
      balance += amount;
      this.addTransactionLog('deposit', amount);
      return amount;
    },
    withdraw(amount) {
      if (amount > balance) {
        amount = balance;
      }
      balance -= amount;
      this.addTransactionLog('withdraw', amount);
      return amount;
    },
    addTransactionLog(type, amount) {
      transactions.push({ type, amount });
    },
    balance() {
      return balance;
    },
    number() {
      return number;
    },
    transactions() {
      return [...transactions];
    },
  };
}

function makeBank() {
  let nextAccountNum = 101;
  let accounts = [];

  return {
    openAccount() {
      let account = makeAccount(nextAccountNum);
      accounts.push(account);
      nextAccountNum += 1;
      return account;
    },
    transfer(sourceAcct, destinationAcct, amount) {
      let withdrawalAmount = sourceAcct.withdraw(amount);
      destinationAcct.deposit(withdrawalAmount);
      return withdrawalAmount;
    },
  };
}


// let account = makeAccount();

// console.log(account.balance);
// // 0
// console.log(account.deposit(12));
// // 12
// console.log(account.balance);
// // 12
// console.log(account.deposit(10));
// // 10
// console.log(account.balance);
// // 22

// account.balance = 100;
// console.log(account.balance);
// // 100
// console.log(account.withdraw(19));
// // 19
// console.log(account.balance);
// // 81

// console.log(account.withdraw(91));
// // 81
// console.log(account.balance);
// // 0

// console.log(account.deposit(23));
// // 23
// console.log(account.transactions);
// // [{...}]
// console.log(account.transactions.slice(-1)[0]);
// // {type: "deposit", amount: 23}

// let otherAccount = makeAccount();
// console.log(otherAccount.balance);
// // 0


// let bank = makeBank();
// console.log(bank.accounts);
// // []


// account = bank.openAccount();
// console.log(account.number);
// // 101
// console.log(bank.accounts);
// // [{...}]
// console.log(bank.accounts[0]);
// // {
// //  number: 101,
// //  balance: 0,
// //  transactions: [],
// //  deposit: [Function: deposit],
// //  withdraw: [Function: withdraw]
// // }
// let secondAccount = bank.openAccount();
// console.log(secondAccount.number);
// // 102


// // let bank = makeBank();
// let source = bank.openAccount();
// console.log(source.deposit(10));
// // 10
// let destination = bank.openAccount();
// console.log(bank.transfer(source, destination, 7));
// // 7
// console.log(source.balance);
// // 3
// console.log(destination.balance);
// // 7

// let bank = makeBank();
// let account = bank.openAccount();
// console.log(account.balance());
// // 0
// console.log(account.deposit(17));
// // 17
// let secondAccount = bank.openAccount();
// console.log(secondAccount.number());
// // 102
// console.log(account.transactions());
// // [{...}]


let bank = makeBank();
console.log(bank.accounts);
// undefined