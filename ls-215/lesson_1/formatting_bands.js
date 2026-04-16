let bands = [
  { name: 'sunset rubdown', country: 'UK', active: false },
  { name: 'women', country: 'Germany', active: false },
  { name: 'a silver mt. zion', country: 'Spain', active: true },
];

function processBands(data) {
  return data.map(({ name, country, active}) => {
    name = name.replaceAll('.', '').split(' ').map(word => word[0].toUpperCase() + word.slice(1)).join(' ');
    country = 'Canada';
    return {
      name,
      country,
      active,
    }
  });
}

console.log(processBands(bands));

// should return:
[
  { name: 'Sunset Rubdown', country: 'Canada', active: false },
  { name: 'Women', country: 'Canada', active: false },
  { name: 'A Silver Mt Zion', country: 'Canada', active: true },
]

console.log(bands);