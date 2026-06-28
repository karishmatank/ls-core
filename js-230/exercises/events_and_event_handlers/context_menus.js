/*
Given the following markup, implement distinct context menus for the main and the sub areas of the web page.
You can represent a context menu as an alert box that displays the name of the respective area (i.e., alert("sub")).
Only one context menu should appear when the event occurs.

Context menus: https://developer.mozilla.org/en-US/docs/Web/API/Element/contextmenu_event

HTML:
<main>
  Main Area
  <section id="sub">
    Sub Area
  </section>
</main>

CSS:
main, #sub {
  padding: 15px;
}
main {
  width: 100%;
  height: 200px;
  background: blue;
  color: white;
}

#sub {
  position: relative;
  top: 100px;
  left: 15px;
  background: red;
  height: 50px;
  width: 50%;
}
*/

document.querySelector('main').addEventListener("contextmenu", event => {
  alert("main");
});

document.querySelector('#sub').addEventListener("contextmenu", event => {
  event.stopPropagation();
  alert("sub");
});

/*
EDIT: Also have to prevent the default behavior of having the right-click menu open, so it's actually:

document.querySelector('main').addEventListener("contextmenu", event => {
  event.preventDefault();
  alert("main");
});

document.querySelector('#sub').addEventListener("contextmenu", event => {
  event.stopPropagation();
  event.preventDefault();
  alert("sub");
});
*/
