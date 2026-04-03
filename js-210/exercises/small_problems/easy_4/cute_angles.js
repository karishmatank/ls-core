/*
Write a function that takes a floating point number representing an angle between 0 and 360 degrees and returns
a string representing that angle in degrees, minutes, and seconds.
You should use a degree symbol (°) to represent degrees, a single quote (') to represent minutes, and a
double quote (") to represent seconds. There are 60 minutes in a degree, and 60 seconds in a minute.

Note: You can use the following constant to represent the degree symbol:
const DEGREE = '\u00B0';

Note: your results may differ slightly depending on how you round values,
but should generally be within a second or two of the results shown.
*/

const DEGREE = '\u00B0';
const MAX_DEGREES = 360;
const MINUTES_PER_DEGREE = 60;
const SECONDS_PER_MINUTE = 60;

function dms(angle) {
  let degrees = Math.floor(angle);
  let remainder = angle - degrees;

  let minutes = Math.floor(remainder * MINUTES_PER_DEGREE);
  remainder = (remainder * MINUTES_PER_DEGREE) - minutes;

  let seconds = Math.floor(remainder * SECONDS_PER_MINUTE);

  let degreesFormat = degrees % MAX_DEGREES;
  let minutesFormat = String(minutes).padStart(2, '0');
  let secondsFormat = String(seconds).padStart(2, '0');

  return degreesFormat + DEGREE + minutesFormat + "'" + secondsFormat + '"';
}


// All test cases should return true
console.log(dms(30) === "30°00'00\"");
console.log(dms(76.73) === "76°43'48\"");
console.log(dms(254.6) === "254°35'59\"");
console.log(dms(93.034773) === "93°02'05\"");
console.log(dms(0) === "0°00'00\"");
console.log(dms(360) === "360°00'00\"" || dms(360) === "0°00'00\"");

/*
The current solution implementation only works with positive numbers in the range of 0 to 360 (inclusive).
Can you refactor it so that it works with any positive or negative number?
*/

function getNormalizedAngle(angle) {
  // If angle is >= 360, compute the mod to get number between 0 and 359
  if (angle >= MAX_DEGREES) {
    angle %= MAX_DEGREES;
  }

  // If angle is negative, keep adding 360 until we get to a positive number
  do {
    angle += MAX_DEGREES;
  } while (angle < 0)

  return angle;
}

function dmsV2(angle) {
  return dms(getNormalizedAngle(angle));
}

console.log(dmsV2(-1));   // 359°00'00"
console.log(dmsV2(400));  // 40°00'00"
console.log(dmsV2(-40));  // 320°00'00"
console.log(dmsV2(-420)); // 300°00'00"
