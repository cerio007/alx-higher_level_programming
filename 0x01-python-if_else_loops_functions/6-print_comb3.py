#!/usr/bin/python3
for numone in range(0, 10):
    for numtwo in range(numone + 1, 10):
        if numone == 8 and numtwo == 9:
            print("{}{}".format(numone, numtwo))
        else:
            print("{}{}".format(numone, numtwo), end=", ")
