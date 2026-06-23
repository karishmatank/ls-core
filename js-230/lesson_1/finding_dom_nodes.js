// ---------- Finding more than one element ----------

/*
Write a JavaScript function that returns the p elements in the DOM represented by this HTML:

<!doctype html>
<html lang="en-US">
  <head>
    <title>On the River</title>
  </head>
  <body>
    <h1>On The River</h1>
    <p>The sun is low</p>
    <p>The waters flow</p>
  </body>
</html>
*/

function findParagraphs() {
  let p = [];

  let body = document.lastChild.lastChild;

  for (let idx = 0; idx < body.childNodes.length; idx += 1) {
    let child = body.childNodes[idx];
    if (child.nodeName === 'P') {
      p.push(child);
    }
  }

  return p;
}

/*
Write a JavaScript function that adds the class article-text to every <p> tag in this HTML:

<!doctype html>
<html lang="en-US">
  <head>
    <title>On the River</title>
  </head>
  <body>
    <div id="page1">
      <div class="intro">
        <p>The sun is low,</p>
      </div>
      <p>The waters flow,</p>
    </div>
    <div id="page2">
      <div class="intro">
        <p>My boat is dancing to and fro.</p>
      </div>
      <p>The eve is still,</p>
    </div>
    <div id="page3">
      <div class="intro">
        <p>Yet from the hill</p>
      </div>
      <p>The killdeer echoes loud and shrill.</p>
    </div>
  </body>
</html>
*/

function walk(node, callback) {
  callback(node);
  for (let idx = 0; idx < node.childNodes.length; idx += 1) {
    walk(node.childNodes[idx], callback);
  }
}

function addParagraphClass(newClassName) {
  walk(document.body, node => {
    if (node instanceof HTMLParagraphElement) {
      node.classList.add(newClassName);
    }
  });
}

addParagraphClass('article-text');

/*
The solution to the previous problem does everything in one function.
It works, but if we need to perform a similar operation later, we must write most of the same code again.
 We can do better by rethinking the problem.

You can think of the problem as having two primary operations: find all the p elements and then add a class to each of them.
We can structure our code similarly; this makes the code's intent clearer to other developers and increases the
reusability of the components.

Using this task breakdown, rewrite the solution to the second problem. The core of your solution should be a
function named getElementsByTagName that returns an array of all elements with a given tag name.
You should then add the CSS class article-text to each paragraph in the array.
*/

function walk(node, callback) {
  callback(node);
  for (let idx = 0; idx < node.childNodes.length; idx += 1) {
    walk(node.childNodes[idx], callback);
  }
}

function getElementsByTagName(tagName) {
  let tagElements = [];
  walk(document.body, node => {
    if (node.nodeName === tagName) {
      tagElements.push(node);
    }
  });
  return tagElements;
}

function addParagraphClass(className) {
  let elements = getElementsByTagName('P');
  elements.forEach(element => element.classList.add(className));
}

addParagraphClass('article-text');

// ---------- Built in functions ----------

/*
Update the answer to question 3 of problem group 1 to use the document.getElementsByTagName method:
*/

function addParagraphClass(className) {
  let elements = Array.from(document.getElementsByTagName('P'));
  elements.forEach(element => element.classList.add(className));
}

addParagraphClass('article-text');

/*
Let's make the previous problem more realistic.
Instead of adding the article-text class to every paragraph on the page, let's restrict it to only the paragraphs
inside a <div class="intro"> tag. How can we do this?
Keep in mind that you can call getElementsByClassName and getElementsByTagName on any element;
document is handiest when you need all matching elements from the page, but you can use any other element
if you don't need everything on the page.

Update the code from Problem 1 to add the article-text class to paragraphs inside <div class="intro">, and nowhere else.
*/

function addParagraphClass(className) {
  let divs = Array.from(document.getElementsByClassName('intro'));
  let elements = divs.reduce((acc, div) => {
    acc = acc.concat(Array.from(div.getElementsByTagName('P')));
    return acc;
  }, []);
  elements.forEach(element => element.classList.add(className));
}

addParagraphClass('article-text');
