/*
Without changing the behavior of the following code, remove the call to event.stopPropagation and refactor the result.

Code:

document.querySelector('html').addEventListener('click', () => {
  document.querySelector('#container').style = 'display: none';
});

document.querySelector('#container').addEventListener('click', event => {
  event.stopPropagation();
});
*/


/*
EDIT: I couldn't figure out how to solve, so I eventually looked at the solution:

document.querySelector('html').addEventListener('click', (event) => {
  const container = document.querySelector('#container');
  if (!container.contains(event.target)) {
    container.style = 'display: none';
  }
});

The reason we do `!container.contains(event.target)` and not just `event.target !== container` is because
if we click on an element that is not the container itself but is a child of the container, we still want to collapse
the container. The `contains` method checks if the target is either the container or a child of the container.
*/
