/*
Write a function that will take a short line of text, and write it to the console log within a box.

logInBox('To boldly go where no one has gone before.');
will log on the console:

+--------------------------------------------+
|                                            |
| To boldly go where no one has gone before. |
|                                            |
+--------------------------------------------+

logInBox('');
+--+
|  |
|  |
|  |
+--+

You may assume that the output will always fit in your browser window.

*/

function logInBox(text) {
  let outerLines = '+-' + '-'.repeat(text.length) + '-+';
  let middleLines = '| ' + ' '.repeat(text.length) + ' |';

  console.log(outerLines);
  console.log(middleLines);
  console.log('| ' + text + ' |');
  console.log(middleLines);
  console.log(outerLines);
}

logInBox('To boldly go where no one has gone before.');
logInBox('');

/*
Modify this function so that it truncates the message if it doesn't fit inside a maximum width provided
as a second argument (the width is the width of the box itself).
You may assume no maximum if the second argument is omitted.
For a real challenge, try word wrapping messages that are too long to fit, so that they appear on multiple lines
but are still contained within the box.
*/

// Wrap messages option
function getLines(text, maxWidth) {
  let lines = [];
  let startIdx = 0;

  while (startIdx < text.length) {
    let endIdx = Math.min(text.length, startIdx + maxWidth);
    lines.push(text.slice(startIdx, endIdx));
    startIdx += maxWidth;
  }

  return lines;
}

function logInBox(text, maxWidth) {
  if (maxWidth === undefined) {
    maxWidth = text.length;
  }
  let outerLines = '+-' + '-'.repeat(maxWidth) + '-+';
  let middleLines = '| ' + ' '.repeat(maxWidth) + ' |';

  console.log(outerLines);
  console.log(middleLines);
  for (let line of getLines(text, maxWidth)) {
    let numExtraSpaces = maxWidth - line.length;
    console.log('| ' + line + ' '.repeat(numExtraSpaces) + ' |');
  }
  console.log(middleLines);
  console.log(outerLines);
}


logInBox('To boldly go where no one has gone before.', 40);
logInBox('To boldly go where no one has gone before.', 30);
logInBox('To boldly go where no one has gone before.', 15);