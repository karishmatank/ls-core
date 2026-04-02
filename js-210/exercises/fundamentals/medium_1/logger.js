/*
Read through the following code. Why will it log 'debugging'?
*/

function debugIt() {
  const status = 'debugging';
  function logger() {
    console.log(status);
  }

  logger();
}

debugIt();

/*
This logs 'debugging' as there is no `status` variable declared within the `logger` function scope to shadow the
`status` variable defined within `debugIt`'s scope. Therefore, JS will reference the `status` defined within
`debugIt` and log its value to the console.

EDIT- Add the following: "Because of JavaScript's lexical scoping rules, the inner `logger` function has access to
variables defined in its outer function `debugIt`."
*/