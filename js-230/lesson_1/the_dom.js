// Link: https://d1nrfq3cstnmkv.cloudfront.net/course_content/pages/dom_assignment.html

/*
Use JavaScript to set a class of 'heading' to the heading (the h1 element).
*/

let h1 = document.querySelector('h1');
h1.classList.add('heading');

/*
Use JavaScript to set the class of the ul element to 'bulleted'.
*/

let list = document.querySelector('#list');
list.classList.add('bulleted');

/*
In this problem and the next, we'll use the onclick element property, which corresponds to a similarly named attribute on
HTML tags. You don't need to know much about onclick right now.
Normally, you won't (and shouldn't) use it in modern code.
The onclick attribute can be set for a DOM element by setting the onclick property of the element to a function
that will be invoked when the user clicks on the corresponding element.

Our page has an element that you can't see initially; it's hidden. When the user clicks the link,
the browser should display the hidden item; the next click on that link should hide the revealed item.
Each click should toggle the hidden element between the visible and hidden states.

Use the Inspector to find the hidden element and determine its ID. Following this, set the onclick property
on the link with an ID of toggle to a function that makes the element visible when it's hidden and hides it when it's visible.
The class names of interest are 'visible' and 'hidden'.

Your function should take a single argument, e. The first line of your function should invoke e.preventDefault().
 We'll discuss this later when we talk more about events, but, for now, just be aware that preventDefault tells
your browser that it shouldn't try to follow the link.
*/

document.querySelector('#toggle').onclick = e => {
  e.preventDefault();

  let hiddenElement = document.querySelector('#notice');

  if (hiddenElement.className === 'hidden') {
    hiddenElement.className = 'visible';
  } else {
    hiddenElement.className = 'hidden';
  }
}

/*
Add an onclick event to the element we show and hide above.
This time, the function should set the class of the element to 'hidden'.
This event will let you hide the visible element by clicking on it.
Since this element is just a div, we don't need to invoke preventDefault, as there's no default behavior
associated with clicking on div elements. Again, don't worry about that for now.
*/

document.querySelector('#notice').onclick = e => {
  e.currentTarget.className = 'hidden';
}

/*
Locate the multiplication paragraph and change the text to the result of the arithmetic problem.
*/

let multiplication = document.querySelector('#multiplication');
multiplication.textContent = '13 x 9 = 117';

/*
Set the ID of the body element to 'styled' to apply the rest of the styles from the original file.
The body tag in this file doesn't have an ID, so you must locate it by some other means.
*/

document.body.id = 'styled';
