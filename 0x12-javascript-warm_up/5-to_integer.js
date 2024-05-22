#!/usr/bin/node
/*
Write a script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer:

If the argument can’t be converted to an integer, print “Not a number”
*/
const array = process.argv;
if (!isNaN(array[2])) {
  console.log(`My number: ${parseInt(array[2])}`);
} else {
  console.log('Not a number');
}
