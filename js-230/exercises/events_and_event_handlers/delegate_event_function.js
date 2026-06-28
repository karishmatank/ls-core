/*
Implement a function delegateEvent(parentElement, selector, eventType, callback) that uses event delegation
to handle events on descendant elements.

Your function should:

Attach a single event listener of type eventType to parentElement.
When an event bubbles up from a descendant that matches selector, invoke callback(event).
Return true if parentElement is a valid DOM element and the event listener was added.
Return undefined if parentElement is not a valid element.
Assume all event listeners use the bubbling phase.

Use this markup and the following scenarios to test your implementation:

HTML:
<!doctype html>
<html lang="en-US">
  <head>
    <meta charset="utf-8">
    <title>Event Delegation Function</title>
  </head>
  <body>
    <main>
      <section>
        <h1>Header</h1>
        <p>Content</p>
      </section>
      <aside>
        <h2>Sub Side Notes</h2>
        <p>Note 1</p>
        <p>Note 2</p>
      </aside>
    </main>
    <nav>
      <p>Side Note</p>
    </nav>
  </body>
</html>


Notes on the scenarios:

Each scenario is independent of the others.
Assume that delegateEvent runs before the described scenario occurs.


Scenarios:

// Possible elements for use with the scenarios
const element1 = document.querySelector('table');
const element2 = document.querySelector('main h1');
const element3 = document.querySelector('main');

// Possible callback for use with the scenarios
const callback = ({target, currentTarget}) => {
  alert(`Target: ${target.tagName}\nCurrent Target: ${currentTarget.tagName}`);
};

Scenario 1: delegateEvent(element1, 'p', 'click', callback);

Returns undefined.
It doesn't add an event listener to any elements.


Scenario 2: delegateEvent(element2, 'p', 'click', callback);

Returns true.
It adds a click event listener to element2.
element2 has no descendant matching 'p', so the callback never triggers.


Scenario 3: delegateEvent(element2, 'h1', 'click', callback);

Returns true.
It adds a click event listener to element2.
element2 has no descendant matching 'h1', so the callback never triggers.


Scenario 4: delegateEvent(element3, 'h1', 'click', callback);

Returns true.
It adds a click event listener to element3.
If you click the h1 element that contains the text "Header," the callback function should trigger and display an alert message,
e.g., 'Target: H1\nCurrent Target: MAIN'.
If you click anywhere else, the callback function does not trigger.


Scenario 5: delegateEvent(element3, 'aside p', 'click', callback);

Returns true.
It adds a click event listener to element3.
If you click a p element that is a descendant of aside element inside main, the callback function should trigger and
display an alert message, e.g., 'Target: P\nCurrent Target: MAIN'.
If you click anywhere else, the callback function does not trigger.


Scenario 6: delegateEvent(element2, 'p', 'click', callback);

Returns true.
It adds a click event listener to element2.
If you click anywhere on the page, the callback function does not trigger.
Run this code:
const newP = document.createElement('P');
const newContent = document.createTextNode('New Paragraph');
newP.appendChild(newContent);
element2.appendChild(newP);

If you click the p element that contains the text "New Paragraph", the callback function should trigger and
display an alert message, e.g., 'Target: P\nCurrent Target: H1'.
If you click anywhere else, the callback function does not trigger.

*/


function delegateEvent(parentElement, selector, eventType, callback) {
  if (document.contains(parentElement)) {
    let newSelector = parentElement.tagName + " " + selector;
    parentElement.addEventListener(eventType, event => {
      if (event.target.matches(newSelector)) {
        callback(event);
      }
    });
    return true;
  }

  return undefined;
}

/*
EDIT: Apparently because the question was asking to check that it is a valid DOM element, my check
instead should be:

if (document instanceof Element)

Also, apparently instead of changing the selector, which is considered "not clean" (I disagree), I should do:
const validTargets = Array.prototype.slice.call(
  parentElement.querySelectorAll(selector)
);

if (validTargets.includes(event.target)) {
  callback(event);
}

This solution instead gets all of the descendents of the parentElement that match the selector. It then
invokes the callback if the current event.target is in that list of descendents.

*/