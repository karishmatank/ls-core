/*
Go over the two HTML snippets. How many nodes will the resulting DOM tree have?

<div>
  <p>Then press the <em>Draw</em> button</p>
</div>

<div><p>Then press the <em>Draw</em> button.</p></div>
*/

/*
The first one has:
div node
  empty node (between div and p)
  p node
    text node 1
    em node
      text node inside em node
    text node 2
  empty node
That is, 8 nodes.

EDIT: Forgot that the DOM inserts in the html, head, and body nodes automatically too.
That means we add on an additional 3 nodes to get to ** 11 nodes **.

The second one has:
HTML node
  HEAD node
  BODY node
  div node
    p node
      text node 1
      em node
        text node
      text node 2
That is, 9 nodes.
*/