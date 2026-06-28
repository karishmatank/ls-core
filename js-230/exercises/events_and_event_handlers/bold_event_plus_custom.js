/*
Implement a function that makes an element bold and allows the user of the function to optionally do something else with it.

HTML:
<!doctype html>
<html lang="en-US">
  <head>
    <meta charset="utf-8">
    <title>Bold Element + Custom</title>
  </head>
  <body>
    <section>Hello World</section>
    <p>Greetings!</p>
  </body>
</html>

Example usage:
> let sectionElement = document.querySelector('section');
> makeBold(sectionElement, function(elem) {
    elem.classList.add('highlight');
  });

> sectionElement.classList.contains('highlight');
= true
> sectionElement.style.fontWeight;
= "bold"
*/

function makeBold(element, callback) {
  element.style.fontWeight = "bold";
  if (callback) {
    callback(element);
  }
}

/*
EDIT: Should also check to make sure the callback is a function, otherwise we'll get an error if we try to call
an uncallable object:

function makeBold(element, callback) {
  element.style.fontWeight = "bold";
  if (callback && typeof(callback) === 'function') {
    callback(element);
  }
}

*/

/*
You can get the same behavior as the above solution by creating your own custom event.
For this further exploration exercise, create your own CustomEvent called bolded that allows the user to
add it as the type of event to listen to.

CustomEvent: https://developer.mozilla.org/en-US/docs/Web/API/CustomEvent
*/

let bolded = new CustomEvent('bolded');

function makeBold(element) {
  element.style.fontWeight = "bold";
  element.dispatchEvent('bolded');
}

// If we had a callback, we would then listen for the bolded event and do:
// document.addEventListener('bolded', callback)

// We would have to invoke makeBold to then trigger the event listener