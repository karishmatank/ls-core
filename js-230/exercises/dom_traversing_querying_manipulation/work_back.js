/*
Given the JavaScript code below, create the corresponding HTML that results to the same logs to the console when executed in
sequence.

There are several possible solutions for this exercise. You'll likely need to experiment to find one that works.
*/

console.log(document.head.childNodes.length); // 3
console.log(document.head.children[0].tagName); // 'TITLE'
console.log(document.head.textContent);
// "
//    Title
//  "
console.log(document.body.children.length); // 3
console.log(document.body.childNodes.length); // 5
console.log(document.querySelector('div').parentNode.parentNode.tagName); // 'BODY'
console.log(document.querySelector('div section').children[2].nextElementSibling); // null
console.log(document.querySelectorAll('div').length); // 1

let nodeA = document.body.firstElementChild;
console.log(document.querySelector('footer').children.length); // 1
console.log(document.querySelector('body').replaceChild(
  document.querySelector('footer'), document.body.firstElementChild).tagName); // 'HEADER'
console.log(document.body.appendChild(nodeA)); // <header>Header</header>

console.log(document.querySelector('section').textContent.split("\n").map(function(text) {
  return text.trim();
}).filter(function(text) {
  return text.length > 0;
})); // ["H1", "Hello", "World"]

console.log(document.querySelector('section').children); // HTMLCollection(3) [h1, p, p]
console.log(document.querySelector('section').textContent);
// "
//           H1
//           Hello
//           World
//         "

console.log(document.querySelector('span.emphasis').parentNode.tagName); // 'FOOTER'

/*
One example of a possible HTML:

<!DOCTYPE html>
<html>
  <head>
    <title>Title</title>
  </head>
  <body>
    <header>Header</header><?>
      <div>
        <section>
          <h1>H1</h1>
          <p>Hello</p>
          <p>World</p>
        </section>
      </div>
    </?><footer>
      <span class='emphasis'></span>
    </footer>
  </body>
</html>

I left a ? for the secodn body element child since the JS didn't reveal what that was, but the official solution
says it's a <main> tag, which makes sense.
The official solution also includes the entire <footer> on one line instead of splitting it over several lines.

*/