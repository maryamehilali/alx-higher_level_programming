#!/usr/bin/node
/*
Write a script that searches the second biggest integer in the list of arguments.

You can assume all arguments can be converted to integer
If no argument passed, print 0
If the number of arguments is 1, print 0
*/
const array = process.argv;
if (array[3]) {
  let i = 3;
  let first = parseInt(array[2]);
  let second = parseInt(array[3]);
  while (array[i]) {
    if (parseInt(array[i]) >= first) {
      second = first;
      first = array[i];
    } else if (parseInt(array[i]) > second) {
      second = array[i];
    }
    i++;
  }
  console.log(second);
} else {
  console.log(0);
}
