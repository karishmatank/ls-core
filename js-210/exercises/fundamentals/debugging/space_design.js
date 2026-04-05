/*
We're putting together some information about our new company Space Design.
Not all roles have been filled yet.
But although we have a CEO and Scrum Master, displaying them shows undefined. Why is that?
*/

// Roles (salary still to be determined)

const ceo = {
  tasks: ['company strategy', 'resource allocation', 'performance monitoring'],
  salary: 0,
};

const developer = {
  tasks: ['turn product vision into code'],
  salary: 0,
};

const scrumMaster = {
  tasks: ['organize scrum process', 'manage scrum teams'],
  salary: 0,
};

// Team -- we're hiring!

const team = {};

team[ceo] = 'Kim';
team[scrumMaster] = 'Alice';
team[developer] = undefined;
console.log(team);

const company = {
  name: 'Space Design',
  team,
  projectedRevenue: 500000,
};

console.log(`----{ ${company.name} }----`);
console.log(`CEO: ${company.team[ceo]}`);
console.log(`Scrum master: ${company.team[scrumMaster]}`);
console.log(`Projected revenue: $${company.projectedRevenue}`);

// ----{ Space Design }----
// CEO: undefined
// Scrum master: undefined
// Projected revenue: $500000

/*
The issue is that `ceo`, `scrumMaster`, and `developer` reference objects that gets coerced into
strings before being made keys of the `team` object.
When we then try to get the ceo and scrumMaster, we try to match up objects with strings, which means
we'll return undefined as the objects are not the keys.

EDIT: Not only that, but each of them gets coerced to '[object Object]'. The last time we assign
the value of that key is `team[developer] = undefined;`. In other words, team has one property,
which is key '[object Object]' and value `undefined` at the end of line 31.

This means that no matter what object we pass in as a key within the bracket notation, we'll get undefined.
*/
