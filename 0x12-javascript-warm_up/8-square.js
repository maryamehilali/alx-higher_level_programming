#!/usr/bin/node
/*
Write a script that prints a square

The first argument is the size of the square
If the first argument can’t be converted to an integer, print “Missing size”
You must use the character X to print the square
*/
const array = process.argv;
if (!isNaN(array[2])) {
  for (let i = 0; i < parseInt(array[2]); i++) {
    let square = '';
    for (let j = 0; j < parseInt(array[2]); j++) {
      square += 'X';
    }
    console.log(square);
  }
} else {
  console.log('Missing size');
}
