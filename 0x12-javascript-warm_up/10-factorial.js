#!/usr/bin/node
function factorialize (num) {
  if (num < 0) {
    return (-1);
  }
  if (num === 0 || isNaN(num)) {
    return (1);
  }
  return (num * factorialize(num - 1));
}

console.log(factorialize(Number(process.argv[2])));
