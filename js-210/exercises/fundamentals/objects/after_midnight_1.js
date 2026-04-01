/*
We can use the number of minutes before or after midnight to represent the time of day.
If the number of minutes is positive, the time is after midnight.
If the number of minutes is negative, the time is before midnight.

The timeOfDay function shown below takes a time argument using this minute-based format,
and returns the time of day in 24-hour format ("hh:mm"). Reimplement the function using JavaScript's Date object.

function timeOfDay(deltaMinutes) {
  deltaMinutes = deltaMinutes % MINUTES_PER_DAY;
  if (deltaMinutes < 0) {
    deltaMinutes = MINUTES_PER_DAY + deltaMinutes;
  }

  let hours = Math.floor(deltaMinutes / MINUTES_PER_HOUR);
  let minutes = deltaMinutes % MINUTES_PER_HOUR;

  return `${padWithZeroes(hours, 2)}:${padWithZeroes(minutes, 2)}`;
}

*/

const MINUTES_PER_HOUR = 60;
const HOURS_PER_DAY = 24;
const MINUTES_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR;

function timeOfDay(deltaMinutes) {
  let date = new Date(0);

  // Documentation says we have to provide 0 to 59, but I don't necessarily do that for some inputs
  // Somehow this works even if deltaMinutes is negative or > 59
  date.setMinutes(deltaMinutes % MINUTES_PER_DAY);

  return `${padWithZeroes(date.getUTCHours(), 2)}:${padWithZeroes(date.getUTCMinutes(), 2)}`;
}

function padWithZeroes(number, length) {
  let numberString = String(number);

  while (numberString.length < length) {
    numberString = `0${numberString}`;
  }

  return numberString;
}



console.log(timeOfDay(0));          // "00:00"
console.log(timeOfDay(-3));         // "23:57"
console.log(timeOfDay(35));         // "00:35"
console.log(timeOfDay(-1437));      // "00:03"
console.log(timeOfDay(3000));       // "02:00"
console.log(timeOfDay(800));        // "13:20"
console.log(timeOfDay(-4231));      // "01:29"