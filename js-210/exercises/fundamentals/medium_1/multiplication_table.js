/*
The following program is expected to log a multiplication table for the numbers from 1 to 10, inclusive, to the console.
Read through the code shown below. Will it produce the expected result? Why or why not?
*/

function padLeft(number) {
  const stringNumber = String(number);
  switch (stringNumber.length) {
    case 1:  return `  ${stringNumber}`;
    case 2:  return ` ${stringNumber}`;
    default: return stringNumber;
  }
}

for (let i = 1; i < 10; i += 1) {
  let row = '';
  for (let j = 1; j <= 10; j += 1) {
    row += `${padLeft(i * j)} `;
  }

  console.log(row);
}

/*
The format will match as shown below:
  1   2   3   4   5   6   7   8   9  10 (end)
  2   4   6   8  10  12  14  16  18  20 (end)
  ...
  9  18  27  36  45  54  63  72  81  90 (end)

I assume the format is fine for this question, but this only goes to row 9, not row 10.
Therefore, I don't think this will produce the intended result.
*/