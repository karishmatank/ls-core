/*
While version numbers often appear to be decimal numbers, they are, in fact,
a convenient notation for a more complicated number system. The following are all legal version numbers:

1
1.0
1.2
3.2.3
3.0.0
4.2.3.0

Write a function that takes any two version numbers in this format and compares them,
with the result of this comparison showing whether the first is less than, equal to, or greater than the second version:

If version1 > version2, we should return 1.
If version1 < version2, we should return -1.
If version1 === version2, we should return 0.
If either version number contains characters other than digits and the . character, we should return null.

Here is an example of version number ordering:

0.1 < 1 = 1.0 < 1.1 < 1.2 = 1.2.0.0 < 1.18.2 < 13.37

*/

/*
Input: Two strings, each representing a version number
Output: A number 1, -1, 0, or null

Rules:
- If either version string has characters other than digits or ., return null
- Groups can have one or more digits
- [MISSED] A version number can't start with or end with a . (Makes sense to ask about this though,
  as realistically we could just interpret the missing number as a 0)
- [MISSED] We can't have more than one '.' back-to-back
- Compare each version's group to determine which version is < or > than the other
  - Groups are defined as sections of the version string delimited by '.'
  - If the number in version1 < number in version2, version1 < version2 => return -1
  - If the number in version1 > number in version2, version1 > version2 => return 1
  - If they are the same, move on to the next section.
- The versions may not have the same number of "groups"
  - Missing groups can be interpreted as a number of 0
  - If each group between the two versions matches, but one has additional groups with 0s, the versions are the same => return 0
  - Otherwise, if the additional groups are not all 0s, the version with additional groups is > the version with fewer groups
- [LSBot answered] We will always get two strings as inputs
- [LSBot answered] Groups should be compared as numbers, not lexicographically
- [LSBot answered] version1 is the first argument provided. version2 is the second argument provided
- [LSBot answered] Don't worry about other data types besides strings
- [LSBot answered] It is possible we get strings that don't have any '.' characters. We should just compare that number to the first "group" of the other version


Questions:
- Will we always receive two versions? When provided, will they always be strings?
- What does it mean to compare versions? Do we compare them based on leftmost digits (before first .), followed by
  second set of digits (after first ., before second .) if first set of digits matches, etc?
  - Does greater than mean that the number of a given set of digits is > that of the other input?
- Do we compare digits as numbers, or lexicographically?
- What is version1, is it the first argument? Is version2 the second argument?
- Will both inputs actually be strings? What happens if one is another data type?


Data structures:
- Input: string
- Output: Number or null
- Groups = [ (num), (num), ... ] => each of the numbers between '.' chars

Algorithm:

High-level
- Parameters are `version1` and `version2`, in that order
1. Check that each version string is valid
2. If at least one string is not valid, return null
3. Get standardized array of groups per version => `groups1`, `groups2`
4. For each index `idx` in `groups1`:
  a. If the group at `idx` in `groups1` is < group at `idx` in `groups2`, return -1
  b. If the group at `idx` in `groups1` is > group at `idx` in `groups2`, return 1
5. If we get to this point, return 0

HELPER: isValidVersion
- Input: string (version)
- Output: true/false
1. Use regex to see if we match this pattern: ^([1 or more digits]. => zero or more times)(1 or more digits)$
2. If so, return true. Otherwise, return false

HELPER: getGroups
- Input: two strings (versions)
- Output: nested array (2xn), each subarray is groups of each version
1. For each of the versions:
  - Split each version into constituent `groups` based on '.' char
  - Convert each element of resulting array into numbers
2. Find absolute value of difference in length => `diff`
3. If group array lengths are uneven (`diff` is not 0):
  - Append on `diff` number of elements of value 0 to the shorter array
4. Return nested array of both groups arrays

Main:
1. Check that each version string is valid
  - Use isValidVersion to check, passing in each input string in successive calls
2. If at least one string is not valid, return null
3. Get standardized array of groups per version => `groups1`, `groups2`
  - Use getGroups, unpack nested array into `groups1` and `groups2`
4. For each index `idx` in `groups1`:
  a. If the group at `idx` in `groups1` is < group at `idx` in `groups2`, return -1
  b. If the group at `idx` in `groups1` is > group at `idx` in `groups2`, return 1
5. If we get to this point, return 0
*/

function isValidVersion(version) {
  return version.match(/^(\d+\.)*\d+$/) !== null;
}

function getGroups(version1, version2) {
  let groups1 = version1.split('.').map(str => Number(str));
  let groups2 = version2.split('.').map(str => Number(str));

  let diff = Math.abs(groups1.length - groups2.length);
  if (diff !== 0) {
    for (let iteration = 0; iteration < diff; iteration += 1) {
      if (groups1.length < groups2.length) {
        groups1.push(0);
      } else {
        groups2.push(0);
      }
    }
  }

  return [groups1, groups2];
}


function compareVersions(version1, version2) {
  if (!isValidVersion(version1) || !isValidVersion(version2)) {
    return null;
  }

  let [ groups1, groups2 ] = getGroups(version1, version2);

  for (let idx = 0; idx < groups1.length; idx += 1) {
    let g1 = groups1[idx];
    let g2 = groups2[idx];

    if (g1 < g2) return -1;
    else if (g1 > g2) return 1;
  }

  return 0;
}


// Test cases

// Happy path
console.log(compareVersions('0.1', '1') === -1);
console.log(compareVersions('0.1', '1.0') === -1);
console.log(compareVersions('1', '0.1') === 1);
console.log(compareVersions('1.0.0', '0.1') === 1);

console.log(compareVersions('1.9', '1.8') === 1);
console.log(compareVersions('1.9', '1.85') === -1);
console.log(compareVersions('1.9.2', '1.9.1') === 1);

console.log(compareVersions('1.0', '1.0') === 0);
console.log(compareVersions('1.0.0', '1.0') === 0);

console.log(compareVersions('1.18.2', '13.37') === -1);
console.log(compareVersions('10.18.2', '2.37') === 1);

console.log(compareVersions('20', '13.37') === 1);
console.log(compareVersions('20', '26') === -1);

console.log(compareVersions('1.0', '1.0.5') === -1); // MISSED
console.log(compareVersions('1.0.0', '1.1') === -1); // MISSED

// Edge cases
console.log(compareVersions('0.a', '1') === null);
console.log(compareVersions('0.1', 'abc ') === null);
console.log(compareVersions('0.ab', 'abc ') === null);
console.log(compareVersions('0.1a', '1.0') === null);

console.log(compareVersions('0.1.', '1') === null);
console.log(compareVersions('.1', '1') === null);
console.log(compareVersions('0..1', '1') === null);




// console.log(isValidVersion('0.1'));
// console.log(isValidVersion('1'));
// console.log(isValidVersion('1.0'));
// console.log(isValidVersion('1.9.0'));

// console.log(isValidVersion('.0.0'));
// console.log(isValidVersion('0.0.'));
// console.log(isValidVersion('0..2'));
// console.log(isValidVersion('12a.123'));


// console.log(getGroups('0.1', '1') === -1);
// console.log(getGroups('0.1', '1.0') === -1);
// console.log(getGroups('1', '0.1') === 1);
// console.log(getGroups('1.0.0', '0.1') === 1);

// console.log(getGroups('1.9', '1.8') === 1);
// console.log(getGroups('1.9', '1.85') === -1);
// console.log(getGroups('1.9.2', '1.9.1') === 1);