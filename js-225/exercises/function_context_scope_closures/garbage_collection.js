/*
Read the following code carefully.
Will the JavaScript garbage collection mechanism garbage collect the array assigned to the variable array
after the function pushIt is called on line 11?
*/

function makeArrays() {
  let array = [];

  return () => {
    array.push('');
    return array;
  };
}

const pushIt = makeArrays();
pushIt();
// more code

/*
No, it won't. `pushIt` references a closure that closes over `array`. We may need to invoke `pushIt` again
in the future.
*/
