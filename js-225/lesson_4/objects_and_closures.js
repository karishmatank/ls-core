function makeList() {
  let items = [];

  return {
    add(newItem) {
      items.push(newItem);
      console.log(newItem + ' added!');
    },
    remove(item) {
      let idx = items.indexOf(item);
      items.splice(idx, 1);
      console.log(item + ' removed!');
    },
    list() {
      if (items.length === 0) {
        console.log('The list is empty.');
      } else {
        items.forEach(item => console.log(item));
      }
    }
  };
}

let list = makeList();
list.add('peas');
// peas added!
list.list();
// peas
list.add('corn');
// corn added!
list.list();
// peas
// corn
list.remove('peas');
// peas removed!
list.list();
// corn