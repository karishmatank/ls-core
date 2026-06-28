/*
Starting with the template below,
write some JavaScript code to move the red X to the last position in the document that the user clicked.

(We were given a CodePen that had the following HTML and CSS loaded)

HTML:
<div class="x">
  <div class="horizontal"></div>
  <div class="vertical"></div>
</div>

CSS:
.x {
  position: absolute;
  transform: rotate(45deg);
  top: 20px;
  left: 20px;
}

.x .horizontal {
  width: 45px;
  height: 5px;
  position: absolute;
  left: -20px;
  background: red;
}

.x .vertical {
  height: 45px;
  width: 5px;
  background: red;
  position: absolute;
  left: 0px;
  top: -20px;
}
*/

document.addEventListener('DOMContentLoaded', () => {
  document.addEventListener('click', (event) => {
    let x = document.querySelector('.x');
    x.style.top = `${event.clientY}px`;
    x.style.left = `${event.clientX}px`;
  });
});


/*
Update your solution to the previous problem to make the red X move as you move the mouse around the document
instead of depending on clicks.
*/

document.addEventListener('DOMContentLoaded', () => {
  document.addEventListener('mousemove', (event) => {
    let x = document.querySelector('.x');
    x.style.top = `${event.clientY}px`;
    x.style.left = `${event.clientX}px`;
  });
});

/*
Update your solution to the previous problem to change the color of the red X to blue when the user presses the b key,
green in response to the g key, and red in response to r. The X should continue to follow the mouse around.
*/

document.addEventListener('DOMContentLoaded', () => {
  document.addEventListener('mousemove', (event) => {
    let x = document.querySelector('.x');
    x.style.top = `${event.clientY}px`;
    x.style.left = `${event.clientX}px`;
  });

  document.addEventListener('keydown', (event) => {
    let divHorizontal = document.querySelector('.horizontal');
    let divVertical = document.querySelector('.vertical');
    let key = event.key;
    if (key === 'r') {
      divHorizontal.style.background = 'red';
      divVertical.style.background = 'red';
    } else if (key === 'g') {
      divHorizontal.style.background = 'green';
      divVertical.style.background = 'green';
    } else if (key === 'b') {
      divHorizontal.style.background = 'blue';
      divVertical.style.background = 'blue';
    }
  });
});

/*
EDIT: The official solution does it a bit more elegantly, where it records the color in a separate variable
and then it iterates through all the children of `x` to change their background color. Here's my re-attempt below:
*/

document.addEventListener('DOMContentLoaded', () => {

  let x = document.querySelector('.x');

  document.addEventListener('mousemove', (event) => {
    x.style.top = `${event.clientY}px`;
    x.style.left = `${event.clientX}px`;
  });

  document.addEventListener('keydown', (event) => {
    let key = event.key;
    let color;
    if (key === 'r') {
      color = 'red';
    } else if (key === 'g') {
      color = 'green';
    } else if (key === 'b') {
      color = 'blue';
    }

    if (color) {
      Array.from(x.children).forEach(child => {
        child.style.background = color;
      });
    }
  });
});


/*
Using the following code, write some JavaScript to add a character counter that updates as the user types.


HTML:
<div class="composer">
  <textarea placeholder="Enter your message"></textarea>
  <p class="counter"></p>
  <button type="submit">Post Message</button>
</div>

CSS:
.composer {
  background: #f5f5f5;
  padding:  1em;
  width:  30em;
}

.composer textarea {
  width: 100%;
  height: 4em;
}

.composer textarea.invalid {
  color: red;
}
*/

document.addEventListener('DOMContentLoaded', () => {
  const STARTING_CHARS = 140;

  let counterP = document.querySelector('.counter');
  counterP.textContent = `${STARTING_CHARS} characters remaining`;

  let text = document.querySelector('textarea');
  text.addEventListener('keyup', (event) => {
    // Get length of text
    let textLength = text.value.length;

    // Update charsRemaining and display
    charsRemaining = STARTING_CHARS - textLength;
    counterP.textContent = `${charsRemaining} characters remaining`;

    // Style if we went over
    if (charsRemaining < 0) {
      text.classList.add('invalid');
    } else {
      text.classList.remove('invalid');
    }
  });
});

