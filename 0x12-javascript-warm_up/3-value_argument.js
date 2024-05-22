#!/usr/bin/node
/*
Write a script that prints the first argument passed to it:

If no arguments are passed to the script, print “No argument
*/
const array = process.argv;
if (array[2]) {
  console.log(array[2]);
} else {
  console.log('No argument');
}
