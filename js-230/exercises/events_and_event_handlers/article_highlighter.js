/*
Given the HTML and CSS in article_highlighter.html, implement JS that does the following:

- When the user clicks on a navigation link (Articles 1-4), the browser scrolls to that article in the <main> element
  and adds the highlight class to it. If another element already has the highlight class,
  the browser removes the class from that element.
- When the user clicks on an article element or any of its child elements, the browser adds the highlight class to it.
  If another element already has the highlight class, the browser removes the class from that element.
- When the user clicks anywhere else on the page, the browser adds the highlight class to the main element.
  If another element already has the highlight class, the browser removes the class from that element.
*/

document.addEventListener('DOMContentLoaded', () => {
  let navLinkUl = document.querySelector('header ul');
  let mainElement = document.querySelector('main');
  let currentlyHighlighted;

  function removeHighlight() {
    // Remove highlights of currently highlighted element
    if (currentlyHighlighted) {
      currentlyHighlighted.classList.remove('highlight');
    }
  }

  navLinkUl.addEventListener('click', event => {
    // event.preventDefault(); -- We want the default behavior because we want to scroll
    if (event.target.tagName === 'A') {
      event.stopPropagation();
      removeHighlight();
      let articleId = event.target.href.split('#').slice(-1)[0];
      let article = document.getElementById(articleId);
      article.classList.add('highlight');
      currentlyHighlighted = article;
    }

  });

  document.addEventListener('click', event => {
    let articleElements = document.querySelectorAll('article');
    let toHighlight;
    articleElements.forEach(article => {
      if (article.contains(event.target)) {
        toHighlight = article;
      }
    });

    if (!toHighlight) {
      toHighlight = mainElement;
    }

    removeHighlight();
    toHighlight.classList.add('highlight');
    currentlyHighlighted = toHighlight;
  });

});