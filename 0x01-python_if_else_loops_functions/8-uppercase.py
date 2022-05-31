#!/usr/bin/python3
def uppercase(str):
    st = ""
    for i in str:
        if 97 <= ord(i) <= 123:
            st += chr((ord(i) - 32))
        else:
            st += i
    print("{}".format(st))
