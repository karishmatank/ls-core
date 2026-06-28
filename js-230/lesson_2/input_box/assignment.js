/*
In this assignment, we'll use HTML, CSS, and JavaScript to build an approximation of an input element.
You'll never do this in an actual project, but doing so here gives us an opportunity to create an interface
that must handle more than one event type.

We'll build the functionality in increments.
When we refer to the text-field element, we mean the element that with a text-field class.
Likewise, the content element has a class of content.

Steps:

1)
Write JavaScript to add the focused class to the text-field element when the user clicks the element.

2)
Write JavaScript that removes the focused class from the text-field element when the user clicks the document.

3)
Write JavaScript to create an interval that adds or removes the class cursor from the text-field element
every 500 milliseconds after the user clicks the text-field element.
The code should toggle the cursor class every 500ms: on with one cycle, off with the next.

We can use a function called setInterval to invoke a callback function over and over again after a
certain amount of time has elapsed. It takes two arguments: the callback to be invoked and the delay in milliseconds
that should elapse between invocations.

Try running this code in the DevTools console to test it out: setInterval(() => console.log('Hello!'), 1000);.
You'll learn more about how setInterval works in the next course.

4)
When the user clicks anywhere in the document, clear the interval that adds and removes the cursor class.

To stop setInterval, we need to pass an interval ID to clearInterval.
The ID is returned when we invoke setInterval, which explains why you likely saw an integer output
when you ran setInterval(() => console.log('Hello!'), 1000); in the console.
Try running this again, but capture this return value and then use it to clear the interval using clearInterval.

5)
When the user presses a keyboard key while the text-field element has the focused class,
append the String value of the key to the content element.
Ignore keyboard entries when the text-field element does not have the focused class.

6)
You might have noticed that when you press keys like "shift" or the backspace button,
the strings "Shift" and "Backspace" are added to our input.
Let's update our solution to ignore keys like shift and delete/backspace.
Additionally, when the user presses the backspace/delete key while the text-field element has the focused class,
delete the last character from the text within the content element.

7)
The current solution has a subtle bug.
If you click consecutively on the text-field element, the cursor will blink chaotically.
It also won't clear when we click outside of the text-field.
This happens because there are as many "intervals" added as there are clicks.
Write JavaScript that only sets the interval if it hasn't been set yet.
*/

document.addEventListener('DOMContentLoaded', () => {
  let textField = document.querySelector('div.text-field');
  let content = document.querySelector('div.content');
  let intervalId;

  textField.addEventListener('click', event => {
    event.stopPropagation();
    textField.classList.add('focused');
    if (!intervalId) {
      intervalId = setInterval(() => {
      textField.classList.toggle('cursor');
    }, 500);
    }
  });

  document.addEventListener('click', event => {
    textField.classList.remove('focused');
    clearInterval(intervalId);
    intervalId = null;
    textField.classList.remove('cursor');
  });

  document.addEventListener('keydown', event => {
    if (textField.classList.contains('focused')) {
      if (event.key === 'Backspace') {
        content.textContent = content.textContent.slice(0, -1);
      } else if (event.key.length === 1) {
        content.textContent += String(event.key);
      }
    }
  })
});