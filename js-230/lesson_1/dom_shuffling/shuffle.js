// Move header up
let header = document.querySelector('body > header');
document.body.insertBefore(header, document.body.firstElementChild);

// Move h1 into header
let h1 = document.querySelector('h1');
header.insertBefore(h1, header.firstElementChild);

// Switch images
let [firstFigure, lastFigure] = document.querySelectorAll('figure');
let firstImage = firstFigure.firstElementChild;
let lastImage = lastFigure.firstElementChild;

firstFigure.insertBefore(lastImage, firstFigure.firstElementChild);
lastFigure.insertBefore(firstImage, lastFigure.firstElementChild);

// Move figures inside the article
let article = document.querySelector('#content article');
article.appendChild(firstFigure);
article.appendChild(lastFigure);