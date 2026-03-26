/*
Write a program to determine a student’s grade based on the average of three scores you get from the user.
Use these rules to compute the grade:

If the average score is greater than or equal to 90 then the grade is 'A'
If the average score is greater than or equal to 70 and less than 90 then the grade is 'B'
If the average score is greater than or equal to 50 and less than 70 then the grade is 'C'
If the average score is less than 50 then the grade is 'F'
You may assume that all input values are valid positive integers.


// prompts to get the 3 scores
Enter score 1: 90
Enter score 2: 50
Enter score 3: 78

// log to the console
Based on the average of your 3 scores your letter grade is "B".
*/

const rlSync = require('readline-sync');
let scoreTotal = 0;

// Get 3 scores
for (let scoreNum = 1; scoreNum <= 3; scoreNum += 1) {
  scoreTotal += parseInt(rlSync.question(`Enter score ${scoreNum}: `), 10);
}

let scoreAvg = scoreTotal / 3;
let message = 'Based on the average of your 3 scores, your letter grade is ';

if (scoreAvg >= 90) {
  message += '"A"';
} else if (scoreAvg >= 70) {
  message += '"B"';
} else if (scoreAvg >= 50) {
  message += '"C"';
} else {
  message += '"F"';
}

console.log(message + ".");