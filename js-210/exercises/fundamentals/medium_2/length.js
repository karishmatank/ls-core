/*
Read through the code below. What values will be logged to the console? Can you explain these results?
*/

const languages = ['JavaScript', 'Ruby', 'Python'];
console.log(languages);
console.log(languages.length);

languages.length = 4;
console.log(languages);
console.log(languages.length);

languages.length = 1;
console.log(languages);
console.log(languages.length);

languages.length = 3;
console.log(languages);
console.log(languages.length);

languages.length = 1;
languages[2] = 'Python';
console.log(languages);
console.log(languages[1]);
console.log(languages.length);

/*
This will print:

[ 'JavaScript', 'Ruby', 'Python' ]
3
[ 'JavaScript', 'Ruby', 'Python', (1 empty space) ] -- Note- how this appears depends on where we run it
4
[ 'JavaScript' ]
1
[ 'JavaScript', (2 empty spaces) ]
3
[ 'JavaScript', (1 empty space), 'Python' ]
undefined
3

EDIT- (1 empty space) => <1 empty item> in Node. (2 empty spaces) => <2 empty items>

*/