/*
Write a function that takes a year as input and returns the century.
The return value should be a string that begins with the century number, and ends with 'st', 'nd', 'rd', or 'th'
as appropriate for that number.

New centuries begin in years that end with 01. So, the years 1901 - 2000 comprise the 20th century.

Examples:
century(2000);        // "20th"
century(2001);        // "21st"
century(1965);        // "20th"
century(256);         // "3rd"
century(5);           // "1st"
century(10103);       // "102nd"
century(1052);        // "11th"
century(1127);        // "12th"
century(11201);       // "113th"
*/

function century(year) {
  let centuryNumber = getCenturyNumber(year);
  let suffix = getSuffix(centuryNumber);
  return `${centuryNumber}${suffix}`;
}

function getCenturyNumber(year) {
  let yearEnding = year % 100;
  let candidateCentury = (year - yearEnding) / 100;
  return yearEnding > 0 ? candidateCentury + 1 : candidateCentury;
}

function getSuffix(centuryNumber) {
  if (centuryNumber % 100 >= 11 && centuryNumber % 100 <= 19) return 'th';

  switch (centuryNumber % 10) {
    case 1:
      return 'st';
    case 2:
      return 'nd';
    case 3:
      return 'rd';
    default:
      return 'th';
  }
}

console.log(century(2000));        // "20th"
console.log(century(2001));        // "21st"
console.log(century(1965));        // "20th"
console.log(century(256));         // "3rd"
console.log(century(5));           // "1st"
console.log(century(10103));       // "102nd"
console.log(century(1052));        // "11th"
console.log(century(1127));        // "12th"
console.log(century(11201));       // "113th"