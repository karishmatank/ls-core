/*
What will each line of the following code return? Don't run the code until after you have tried to answer.
*/

console.log((false && undefined));
console.log((false || undefined));
console.log(((false && undefined) || (false || undefined)));
console.log(((false || undefined) || (false && undefined)));
console.log(((false && undefined) && (false || undefined)));
console.log(((false || undefined) && (false && undefined)));
console.log(('a' || (false && undefined) || ''));
console.log(((false && undefined) || 'a' || ''));
console.log(('a' && (false || undefined) && ''));
console.log(((false || undefined) && 'a' && ''));

/*
(false && undefined);                              false
(false || undefined);                              undefined
((false && undefined) || (false || undefined));    undefined
((false || undefined) || (false && undefined));    false
((false && undefined) && (false || undefined));    false
((false || undefined) && (false && undefined));    undefined
('a' || (false && undefined) || '');               'a'
((false && undefined) || 'a' || '');               'a'
('a' && (false || undefined) && '');               undefined
((false || undefined) && 'a' && '');               undefined
*/