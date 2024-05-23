#!/usr/bin/node
/*
Write a script that computes and prints a factorial

The first argument is integer (argument can be cast as integer) used for computing the factorial
Factorial of NaN is 1
You must do it recursively
You must use a function
*/
function fact (n) {
  if (n === 1) {
    return 1;
  } else {
    return fact(n - 1) * n;
  }
}
const array = process.argv;
if (!isNaN(array[2])) {
  console.log(fact(array[2]));
} else {
  console.log(1);
}
