/*
Implement a function, sliceTree, that is "similar" to the Array.prototype.slice method, but this time for a DOM tree.
The sliceTree function takes two arguments: the start index which is the parent node's id attribute and,
the end index which is the innermost child node's id attribute. The function returns an array of tagNames.
Take note of the following when implementing the sliceTree function:

- It's similar to slice but different in the sense that slice isn't inclusive on the right hand side.
- The end index doesn't have to be the id of the "innermost" child node as some of the examples suggest.
- Only consider element nodes.
- Only elements that have body as an ancestor (parent, grandparent, etc.) are sliceable.
- If the id attribute of the start or end index is not in the DOM, return undefined.
- If the slice is not feasible — there's no path connecting the element at the starting index to the ending index — return
  undefined.


<!doctype html>
<html>
  <head>
    <title>Tree Slicing</title>
  </head>
  <body>
    <article id="1">1
      <header id="2">2
        <span id="3">3
          <a href="#" id="4">4</a>
        </span>
      </header>
      <main id="5">5
        <section id="6">6
          <p id="7">7
            <span id="8">8
              <strong id="9">9
                <a href="#" id="10">10</a>
              </strong>
            </span>
          </p>
        </section>
        <section id="11">11
          <p id="12">12
            <span id="13">13
              <strong id="14">14
                <a href="#" id="15">15</a>
              </strong>
            </span>
          </p>
          <p id="16">16
            <span id="17">17
              <strong id="18">18
                <a href="#" id="19">19</a>
              </strong>
            </span>
            <span id="20">20
              <strong id="21">21
                <a href="#" id="22">22</a>
              </strong>
            </span>
          </p>
        </section>
      </main>
      <footer id="23">23
        <p id="24">24</p>
      </footer>
    </article>
  </body>
</html>


> sliceTree(1, 4);
= ["ARTICLE", "HEADER", "SPAN", "A"]
> sliceTree(1, 76);
= undefined
> sliceTree(2, 5);
= undefined
> sliceTree(5, 4);
= undefined
> sliceTree(1, 23);
= ["ARTICLE", "FOOTER"]
> sliceTree(1, 22);
= ["ARTICLE", "MAIN", "SECTION", "P", "SPAN", "STRONG", "A"]
> sliceTree(11, 19);
= ["SECTION", "P", "SPAN", "STRONG", "A"]
*/

function walkTree(currentNode, endNode) {
  let tree = [];
  let children = Array.from(currentNode.children);

  for (let child of children) {
    if (child === endNode) {
      tree.push(currentNode.tagName);
      tree.push(child.tagName);
      break;
    }

    tree = walkTree(child, endNode);
    if (tree.length > 0) {
      tree.unshift(currentNode.tagName);
      break;
    }
  }

  return tree;

}

function sliceTree(startId, endId) {
  let startElement = document.getElementById(startId);
  let endElement = document.getElementById(endId);
  if (startElement === null || endElement === null) {
    return undefined;
  }

  let tree = walkTree(startElement, endElement);
  if (tree.length > 0) {
    return tree;
  }
  return undefined;
}

/*
EDIT: The above works, but the official solution notes a few things:
1) It is actually easier to traverse from the end to the start. As we did it above, we have to check multiple
   branches to find where the end node is. If we start with the end, we just keep checking the parent to see whether
   it is the start node, as there is only one path from the start to the end if we are traversing from the end
2) We technically didn't account for the elements being in the body. We didn't have to with this HTML as it isn't
   an issue, but we should have put in a check
*/