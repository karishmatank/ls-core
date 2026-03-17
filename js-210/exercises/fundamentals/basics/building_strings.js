/*
The intention of the program below is to output a paragraph.
Copy and paste the program into a JavaScript console (e.g., from the Chrome Developer Tools), then run it.
Is the output what you expected? Are there any bugs/errors?
*/

const paragraph = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sed \
                ligula at risus vulputate faucibus. Aliquam venenatis nibh ut justo dignissim \
                dignissim. Proin dictum purus mollis diam auctor sollicitudin. Ut in bibendum \
                ligula. Suspendisse quam ante, dictum aliquam tristique id, porttitor pulvinar \
                diam. Maecenas blandit aliquet ipsum. Integer vitae sapien sed nulla rutrum \
                hendrerit ac a urna. Interdum et malesuada fames ac ante ipsum primis in faucibus.';

console.log(paragraph);

/*
It prints, but there are a lot of added spaces in between the lines above. That's because when we use \ to
merge together multi-line strings, JavaScript adds in any indentation included in subsequent lines.

I have my editor set up to strip trailing whitespace. However, the original problem actually had whitespace
after the \. If we did have trailing whitespace, this would have raised a SyntaxError.
From the solution:
The purpose of the backslash is to escape the newline character at the end of the line.
However, the extra whitespace prevents this from happening, causing a SyntaxError to be raised.
*/