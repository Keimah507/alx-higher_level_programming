#!/usr/bin/node
function factorialize(num) {
    if (num < 0) {
        return (-1);
    }else if (num === undefined) {
        return (1);
    } else {
        return (num * factorialize(num-1))
    }
}

console.log(factorialize(Number(process.argv[2])));
