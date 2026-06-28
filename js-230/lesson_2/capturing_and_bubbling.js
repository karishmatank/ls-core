/*
All of the problems below use the following HTML and CSS:

CodePen: https://codepen.io/launchschool/pen/raNzLPg

HTML:
<div id="elem1">1
  <section id="elem2">2
    <article id="elem3">3
      <main id="elem4">4
      </main>
    </article>
  </section>
</div>

CSS:
#elem1 {
  background-color: green;
  position: relative;
  width: 200px;
  height: 200px;
  text-align: center;
  cursor: pointer;
}

#elem2 {
  background-color: blue;
  position: absolute;
  top: 25px;
  left: 25px;
  width: 150px;
  height: 150px;
}

#elem3 {
  background-color: red;
  position: absolute;
  top: 25px;
  left: 25px;
  width: 100px;
  height: 100px;
  line-height: 25px;
}

#elem4 {
  background-color: yellow;
  position: absolute;
  top: 25px;
  left: 25px;
  width: 50px;
  height: 50px;
  line-height: 50px;
}
*/

/*
JS:
let elem1 = document.querySelector('#elem1');

elem1.addEventListener('click', event => alert(event.target.tagName));
elem1.addEventListener('click', event => alert(event.currentTarget.tagName));

Q:
Click on the yellow box labeled "4".
Based on what you see, what event handlers are triggered, and in what order? How can we tell?
*/


/*
We'll see "MAIN" in an alert first, followed by "DIV" after.

I think the first event listener that alerts the event.target.tagName will fire first because we've attached
it first in the JS code. event.target references the element that we clicked on, which is the element with label "4", or
the <main> element. I think the event listener that alerts the event.currentTarget.tagName will fire last.
event.currentTarget references the element we attached the event listener to, which is elem1, or the <div> element.
*/


/*
JS:
let elem1 = document.querySelector('#elem1');

elem1.addEventListener('click', event => alert("bubbling"));
elem1.addEventListener('click', event => alert("capturing"), true);

Q:
Again, click on the yellow "4" box. What happens when we do this, and why? How can we explain the order of the alert boxes?
*/

/*
In this case, it will alert "capturing" first, followed by "bubbling".
This is because the second event listener is instructed to fire during the capturing phase as the event cascades
from the window all the way down to the element with id "elem4".
Then, the first event listener will fire during the bubbling phase, which comes afterwards.
*/


/*
JS:
let elem1 = document.querySelector('#elem1');
let elem4 = document.querySelector('#elem4');

elem1.addEventListener('click', event => alert('Elem1 Listener triggered!'));
elem4.addEventListener('click', event => alert('Elem4 Listener triggered!'));


Q:
Click on the red box labeled "3".
What event listeners are triggered?
Would this behavior change if we set "on capture" to true for either or both event listeners?
*/

/*
We would only see an alert for "Elem1 Listener triggered!". We only click on the element with id "elem3", which is the parent
to the element with id "elem4". We don't cascade all the way down to #elem4, so its event listener never triggers.
The event propagates from "window" down to #elem3 during the capture phase,
then turns around and propagates back up to window through the bubbling phase.

This doesn't change even if we set "on capture" to true.
*/
