/*
The code below is buggy.
The person who created the code expects that nothing will happen when the user clicks on the image.
This, however, isn't the case; clicking the image still brings the user to another web page.

Study the code and explain the bug.


JS:
document.querySelector('img').addEventListener('click', event => {
  event.stopPropagation();
}, false);

HTML:
<a href="https://www.launchschool.com">
  Home
  <img src="https://d1nrfq3cstnmkv.cloudfront.net/exercises/events_event_handlers/ls_logo.png" />
</a>

*/

/*
The bug is because we should have event.preventDefault() at the top of the event handler. Stopping propagation
doesn't really do much here- it stops the propagation from bubbling up further, but that doesn't mean that the browser
won't try to follow the link after the image has been clicked, given the image is inside an <a> element.
*/
