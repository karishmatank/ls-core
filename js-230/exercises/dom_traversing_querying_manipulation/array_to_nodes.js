/*
Implement a function that converts a nested array of nodeNames (see Nodes to Array exercise for examples) to nodes.
Go over the sample code and the corresponding return values below as a guide for what you will implement.

Example 1:

// Nested array of nodes
const nodes = ["BODY",[["HEADER",[]],["MAIN",[]],["FOOTER",[]]]];

// OR
//
// ["BODY", [
//   ["HEADER", []],
//   ["MAIN", []],
//   ["FOOTER", []]]]

arrayToNodes(nodes);

<body>
  <header></header>
  <main></main>
  <footer></footer>
</body>


Example 2:

// Nested array of nodes
const nodes = ["BODY",[["DIV",[["DIV",[]],["DIV",[["DIV",[]]]]]],["DIV",[]],["DIV",[["DIV",[]],["DIV",[]],["DIV",[]]]]]];

// OR
//
// [
//   "BODY", [
//     [
//       "DIV", [
//         ["DIV", []],
//         [
//           "DIV", [
//             ["DIV", []]
//           ]
//         ]
//       ]
//     ],
//     ["DIV", []],
//     [
//       "DIV", [
//         ["DIV", []],
//         ["DIV", []],
//         ["DIV", []]
//       ]
//     ]
//   ]
// ]

arrayToNodes(nodes);

<body>
  <div>
    <div></div>
    <div>
      <div></div>
    </div>
  </div>
  <div></div>
  <div>
    <div></div>
    <div></div>
    <div></div>
  </div>
</body>
*/

function createChildrenElements(parentNode, nodesArray) {
  nodesArray.forEach(([tag, children]) => {
    let newElement = document.createElement(tag);
    parentNode.appendChild(newElement);
    if (children.length > 0) {
      createChildrenElements(newElement, children);
    }
  });
}

function arrayToNodes(nodesArray) {
  // First will always be the body
  document.body = document.createElement('BODY');
  let childrenNodes = nodesArray[1];
  createChildrenElements(document.body, childrenNodes);
}

/*
EDIT: LS Bot yelled at me because I didn't return the newly created nodes. Apparently we don't want to actually
insert it into the HTML but just return the HTML. Wasn't clear to me...

Also, the official solution seems to be more general- instead of assumping the first node will always be body,
they don't assume that. I'll rewrite my answer below:
*/

function arrayToNodes([tag, children]) {
  let parent = document.createElement(tag);
  children.forEach(child => parent.appendChild(arrayToNodes(child)));
  return parent;
}

/* Ended up being easier than the solution I came up with... */