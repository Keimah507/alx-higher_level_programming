#!/usr/bin/python3
back = 122
while back > 96:
    if back % 2 != 0:
        upperC = chr(back - 32)
        print("{}".format(upperC), end="")
    else:
        print("{}".format(upperC, end="")
    back -= 1
