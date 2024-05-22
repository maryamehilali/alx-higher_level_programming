#!/usr/bin/node
/*
Write a script that prints x times “C is fun”

Where x is the first argument of the script
If the first argument can’t be converted to an integer, print “Missing number of occurrences”
*/
const array = process.argv;
if (!isNaN(array[2])) {
  for (let i = 0; i < parseInt(array[2]); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
