#!/usr/bin/python3
from sys import argv
div = 0
file = open(argv[1], 'r')
lines = file.readlines()
for number in lines:
    c = int(number)
    for i in range(2, c + 1):
        if(c % i == 0):
            div = int(c / i)
            print("{:d} = {:d} * {:d}".format(c, div, i))
            break
