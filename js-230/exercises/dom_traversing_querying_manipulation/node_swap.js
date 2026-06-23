/*
Write a function that takes two element ids as arguments and swaps the positions of the elements represented by the ids.
The function returns true for valid swaps and undefined for invalid.
To put the focus on the node swapping functionality, you can assume that nodes will have a value for the id attribute
and two arguments will always be provided. Use the following HTML and sample codes to test your output:

<!doctype html>
<html>
  <head>
    <title>Node Swap</title>
  </head>
  <body>
    <div id="1">
      <div id="4"></div>
      <div id="5">
        <div id="6"></div>
      </div>
    </div>
    <div id="2"></div>
    <div id="3">
      <div id="7"></div>
      <div id="8"></div>
      <div id="9"></div>
    </div>
  </body>
</html>


Invalid swaps
// at least one of the id attributes doesn't exist
> nodeSwap(1, 20);
= undefined

// at least one of the nodes is a "child" of the other
> nodeSwap(1, 4);
= undefined
> nodeSwap(9, 3);
= undefined

Valid swaps
// one swap
> nodeSwap(1, 2);

<!doctype html>
<html>
  <head>
    <title>Node Swap</title>
  </head>
  <body>
    <div id="2"></div>
    <div id="1">
      <div id="4"></div>
      <div id="5">
        <div id="6"></div>
      </div>
    </div>
    <div id="3">
      <div id="7"></div>
      <div id="8"></div>
      <div id="9"></div>
    </div>
  </body>
</html>

// multiple swaps
> nodeSwap(3, 1);
> nodeSwap(7, 9);

<!doctype html>
<html>
  <head>
    <title>Node Swap</title>
  </head>
  <body>
    <div id="3">
      <div id="9"></div>
      <div id="8"></div>
      <div id="7"></div>
    </div>
    <div id="2"></div>
    <div id="1">
      <div id="4"></div>
      <div id="5">
        <div id="6"></div>
      </div>
    </div>
  </body>
</html>

*/

function isRelatedElement(parent, child) {
  // Check if child is an actual child of parent
  let currentElement = child;
  do {
    let parentElement = currentElement.parentNode;
    if (parentElement === parent) {
      return true;
    }
    currentElement = parentElement;
  } while (currentElement !== null);

  return false;
}

function nodeSwap(id1, id2) {
  // If neither element exists, return undefined
  let element1 = document.getElementById(id1);
  let element2 = document.getElementById(id2);
  if (element1 === null || element2 === null) {
    return undefined;
  }

  // If one of the nodes is a child of the other, return undefined
  if (isRelatedElement(element1, element2) || isRelatedElement(element2, element1)) {
    return undefined;
  }

  // Make the swap
  let clone1 = element1.cloneNode(true);
  let clone2 = element2.cloneNode(true);
  element1.parentNode.replaceChild(clone2, element1);
  element2.parentNode.replaceChild(clone1, element2);

  return true;
}

/*
The current solution clones the nodes and uses the .replaceChild method to handle the swapping.
The limitation of this approach, however, is that the nodes will lose all event listeners attached to it via JavaScript.
For further exploration, refactor/implement a solution wherein the swapped nodes don't lose event listeners — if any —
added via JavaScript.
*/

function nodeSwap(id1, id2) {
  // If neither element exists, return undefined
  let element1 = document.getElementById(id1);
  let element2 = document.getElementById(id2);
  if (element1 === null || element2 === null) {
    return undefined;
  }

  // If one of the nodes is a child of the other, return undefined
  if (isRelatedElement(element1, element2) || isRelatedElement(element2, element1)) {
    return undefined;
  }

  // Make the swap

  // First, we'll put in some placeholder so we don't lose our place when swapping
  let placeholder1 = document.createElement('div');
  element1.parentNode.insertBefore(placeholder1, element1);
  let placeholder2 = document.createElement('div');
  element2.parentNode.insertBefore(placeholder2, element2);

  placeholder1.insertAdjacentElement('afterend', element2);
  placeholder2.insertAdjacentElement('afterend', element1);

  placeholder1.remove();
  placeholder2.remove();

  return true;
}