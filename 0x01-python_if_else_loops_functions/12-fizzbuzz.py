#!/usr/bin/python3
def fizzbuzz();
for i int range(1, 101):
    if i % 5 == 0 and i % 3 ==0:
        print("{}".format("FizzBuzz"), end="")
    elif i % 3 == 0:
        print("{}".format("Fizz"), end="")
    elif i % 5 == 0:
        print("{}".format("Buzz"), end="")
    else:
        print("{}".format(i), end="")
