/*
Todd wrote some simple code in an attempt to log his shop's financial transactions.
Each time he makes a sale or spends money on inventory, he logs that deposit or withdrawal
via the logTransaction function. His code also intends to ensure that each transaction logged
is a valid numerical amount.
At the end of each day, he displays his total gain or loss for the day with transactionTotal.

Test out the code yourself. Can you spot the problem and fix it?
*/

const transactionLog = [];

function processInput(input) {
  const numericalData = parseFloat(input);

  if (Number.isNaN(numericalData)) {
    throw (new Error('Data could not be converted to numerical amount.'));
  }

  return numericalData;
}

function logTransaction() {
  let data = prompt('Please enter the transaction amount: ');

  try {
    data = processInput(data);
    transactionLog.push(data);

    alert('Thank you. Data accepted.');
  } catch {
    alert(error.message);
  }
}

function transactionTotal() {
  let total = 0;

  for (let i = 0; i < transactionLog.length; i++) {
    total += transactionLog[i];
  }

  return total;
}

logTransaction();
logTransaction();
logTransaction();

console.log(transactionTotal());

/*
I believe the issue is in the try/except block. We need to specify the `error` by writing `catch (error)` rather
than just `catch`.
*/