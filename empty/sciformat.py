#!/bin/env python3

import sys

def sci(a):
    string_no = f"{a}"[0]+f"."+f"{a}"[1:4]+f"e+{len(str(a))-1}"
    print(string_no)
    return string_no

if __name__ == "__main__":
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    except:
        print("The script requires two integer numbers:\nThe result is: a**b and b**a in scientific format")
    c = a ** b
    d = b ** a
    print(f"a**b: {a}**{b}={sci(c)}")
    print(f"b**a: {b}**{a}={sci(d)}")
