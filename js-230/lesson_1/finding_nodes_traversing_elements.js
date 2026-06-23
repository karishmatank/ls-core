/* Link: https://d1nrfq3cstnmkv.cloudfront.net/course_content/pages/polar_bear_wiki.html */

/*
Write some JavaScript code to retrieve a word count for each h2 heading on the page.
*/

let h2Elements = Array.from(document.getElementsByTagName('H2'));
let wordCounts = h2Elements.reduce((acc, element) => {
  acc[element.textContent] = element.textContent.split(' ').length;
  return acc;
}, {});

for (let header in wordCounts) {
  console.log(`${header}: ${wordCounts[header]}`);
}

/*
The page has a table of contents with the title "Contents" and links to the different content sections
on "Naming and etymology," "Taxonomy and evolution," etc.

Use three different DOM methods to retrieve a reference to the div element that contains the table of contents.
*/

let tableOfContents;

// Method 1
tableOfContents = document.getElementById('toc');

// Method 2
tableOfContents = document.querySelector('#toc');

// Method 3
tableOfContents = document.getElementsByClassName('toc')[0];

/* NOTE: You can also use querySelectorAll */

/*
Write some JavaScript code to change the color for every odd indexed link in the table of contents to green.
*/

let links = Array.from(document.querySelectorAll('#toc a'));
links.forEach((link, idx) => {
  if (idx % 2 === 1) {
    link.style.color = 'green';
  }
});

/*
Write some JavaScript code to retrieve the text of every thumbnail caption on the page.
*/

let thumbCaptions = Array.from(document.querySelectorAll('.thumbcaption')).map(caption => caption.textContent.trim());

/*
You can think of the scientific classification of an animal as a series of key-value pairs.
Here, the keys are taxonomic ranks (Kingdom, Phylum, Class, etc.).
The values are the specific groups to which the animal belongs.

Write JavaScript code that extracts the classification of animals from the web page and logs an Object that
uses the ranks as keys and the groups as values.
You may assume the taxonomic ranks to use as keys are provided for you as an array.
*/

let info = Array.from(document.querySelectorAll('.biota td')).slice(2, 16).map(element => element.textContent);
let ranks = info.filter((_, idx) => idx % 2 === 0).map(element => element.replace(':', ''));
let groups = info.filter((_, idx) => idx % 2 === 1);

let classification = {};
for (let idx = 0; idx < ranks.length; idx += 1) {
  classification[ranks[idx]] = groups[idx];
}

/*
Note: There's an interesting way of doing this using nextElementChild:

let keys = ['Kingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genus', 'Species'];
let classification = {};
let tds = document.querySelectorAll('.infobox td');
let cell;
let link;

for (let index = 0; index < tds.length; index += 1) {
  cell = tds[index];

  keys.forEach(key => {
    if (cell.textContent.indexOf(key) !== -1) {
      link = cell.nextElementSibling.firstElementChild;
      classification[key] = link.textContent;
    }
  });
}

console.log(classification);
*/