/*
Let's build another program using madlibs. We made a similar program in the Easy exercises,
but this time the requirements are a bit different.

Build a madlibs program that takes a text template as input, plugs in a selection of randomized nouns,
verbs, adjectives, and adverbs into that text, and then returns it.
You can build your lists of nouns, verbs, adjectives, and adverbs directly into your program.
Your program should read this text and, for each line, place random words of the appropriate types
into the text and return the result.

The challenge of this program isn't just about writing your solution—it's about choosing the structure
of the text template. Choose the right way to structure your template and this problem becomes much easier.
Consequently, this exercise is a bit more open-ended since the input is also something that you'll be defining.

Note: The quotes in the example strings returned by the madlibs function are only shown for emphasis.
These quotes are not present in the actual output strings.
The words in quotes come from the list of texts and it is the madlibs function that puts them in.


My questions:
- Confirm the adjectives, nouns, verbs, and adverbs can be repeated more than once per invocation
-


Input: String (template)
Output: String (filled out template)
Rules:
- We need to plug in random nouns, verbs, adjectives, and adverbs into the template
- A given adjective, noun, verb, or adverb can be repeated more than once per invocation
- We should format the template such that we can identify where to plug in a specific type of word


*/

template1 = 'The "ADJECTIVE" brown "NOUN" "ADVERB"\n' +
            '"VERB" the "ADJECTIVE" yellow\n' +
            '"NOUN", who "ADVERB" "VERB" his\n' +
            '"NOUN" and looks around.\n';

template2 = 'The "NOUN" "VERB" the "NOUN"\'s "NOUN".';

function madlibs(template) {
  const ADJECTIVES = ['quick', 'lazy', 'sleepy', 'noisy', 'hungry'];
  const NOUNS = ['fox', 'dog', 'head', 'leg', 'tail', 'cat'];
  const VERBS = ['jumps', 'lifts', 'bites', 'licks', 'pats'];
  const ADVERBS = ['easily', 'lazily', 'noisily', 'excitedly'];

  return template.replace(/\"([A-Z]+)\"/g, (_, word) => {
    let choices;
    if (word === 'ADJECTIVE') {
      choices = ADJECTIVES;
    } else if (word === 'NOUN') {
      choices = NOUNS;
    } else if (word === 'VERB') {
      choices = VERBS;
    } else {
      choices = ADVERBS;
    }

    let idx = Math.round(Math.random() * (choices.length - 1));
    return choices[idx];
  });

}

// These examples use the following list of replacement texts:
// adjectives: quick lazy sleepy noisy hungry
// nouns: fox dog head leg tail cat
// verbs: jumps lifts bites licks pats
// adverbs: easily lazily noisily excitedly
// ------

console.log(madlibs(template1));
// The "sleepy" brown "cat" "noisily"
// "licks" the "sleepy" yellow
// "dog", who "lazily" "licks" his
// "tail" and looks around.

console.log(madlibs(template1));
// The "hungry" brown "cat" "lazily"
// "licks" the "noisy" yellow
// "dog", who "lazily" "licks" his
// "leg" and looks around.

console.log(madlibs(template2));      // The "fox" "bites" the "dog"'s "tail".

console.log(madlibs(template2));      // The "cat" "pats" the "cat"'s "head".