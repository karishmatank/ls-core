/*
Given the HTML below, write some JavaScript code that updates the options on one dropdown when the selection
in the other dropdown changes. For instance, when the user chooses an option under Classifications,
the items in the Animals dropdown should change accordingly.
Use the lookup tables below to see which animals and classifications go together.

HTML:
<form id="selection-filters" method="post" action="#">
  <select id="animal-classifications">
    <option value="Classifications" selected>Classifications</option>
    <option value="Vertebrate">Vertebrate</option>
    <option value="Warm-blooded">Warm-blooded</option>
    <option value="Cold-blooded">Cold-blooded</option>
    <option value="Mammal">Mammal</option>
    <option value="Bird">Bird</option>
  </select>
  <select id="animals">
    <option value="Animals" selected>Animals</option>
    <option value="Bear">Bear</option>
    <option value="Turtle">Turtle</option>
    <option value="Whale">Whale</option>
    <option value="Salmon">Salmon</option>
    <option value="Ostrich">Ostrich</option>
  </select>
  <button id="clear" type="button">Clear</button>
</form>

Selection Change with Filter1: Animal Classifications

Selection |	Animals Options
Vertebrate |	Bear, Turtle, Whale, Salmon, Ostrich
Warm-blooded |	Bear, Whale, Ostrich
Cold-blooded |	Salmon, Turtle
Mammal |	Bear, Whale
Bird |	Ostrich

Selection Change with Filter2: Animals

Selection |	Animal Classifications Options
Bear |	Vertebrate, Warm-blooded, Mammal
Turtle |	Vertebrate, Cold-blooded
Whale |	Vertebrate, Warm-blooded, Mammal
Salmon |	Vertebrate, Cold-blooded
Ostrich |	Vertebrate, Warm-blooded, Bird
When the user clicks the "Clear" button, the program should reset both dropdowns to their default values.
*/

const ANIMALS_PER_CLASSIFICATION = {
  'Classifications': ['Animals', 'Bear', 'Turtle', 'Whale', 'Salmon', 'Ostrich'],
  'Vertebrate': ['Bear', 'Turtle', 'Whale', 'Salmon', 'Ostrich'],
  'Warm-blooded': ['Bear', 'Whale', 'Ostrich'],
  'Cold-blooded': ['Salmon', 'Turtle'],
  'Mammal': ['Bear', 'Whale'],
  'Bird': ['Ostrich'],
};

const CLASSIFICATIONS_PER_ANIMAL = {
  'Animals': ['Classifications', 'Vertebrate', 'Warm-blooded', 'Cold-blooded', 'Mammal', 'Bird'],
  'Bear': ['Vertebrate', 'Warm-blooded', 'Mammal'],
  'Turtle': ['Vertebrate', 'Cold-blooded'],
  'Whale': ['Vertebrate', 'Warm-blooded', 'Mammal'],
  'Salmon': ['Vertebrate', 'Cold-blooded'],
  'Ostrich': ['Vertebrate', 'Warm-blooded', 'Bird'],
};

function rebuildSelect(element, options) {
  element.options.length = 0;
  options.forEach(value => {
    let newOption = document.createElement('option');
    newOption.textContent = value;
    newOption.value = value;
    element.appendChild(newOption);
  });
}

document.addEventListener('DOMContentLoaded', () => {
  let classificationsElement = document.querySelector('#animal-classifications');
  let animalsElement = document.querySelector('#animals');
  let clearBtn = document.querySelector('#clear');

  classificationsElement.addEventListener('change', event => {
    let selectedValue = event.target.value;
    rebuildSelect(animalsElement, ANIMALS_PER_CLASSIFICATION[selectedValue]);
  });

  animalsElement.addEventListener('change', event => {
    let selectedValue = event.target.value;
    rebuildSelect(classificationsElement, CLASSIFICATIONS_PER_ANIMAL[selectedValue]);
  });

  clearBtn.addEventListener('click', () => {
    rebuildSelect(animalsElement, ANIMALS_PER_CLASSIFICATION['Classifications']);
    rebuildSelect(classificationsElement, CLASSIFICATIONS_PER_ANIMAL['Animals']);
  });

});