#!/bin/env python3
import sys

def check_symmetry(a,b):
    try:
        #print(f"Trying numbers: {(a,b)}")
        sum1 = a ** b
        sum2 = a + b
    except:
        raise TypeError(f"Wrong type passed to function check_symmetry")
    if (b ** a) == sum1:
        d = sum1 % 10
        c = (sum1 - d)//10
        if (c + d - 1) == sum2:
            print(f"\n===========\nHEUREKA!!!! Found numbers: \n{(a,b)}\n")
            return (a,b)
        else:
            if a != b:
                print(f"{(a,b)} symmetry 'a**b == b**a' OK")
            return None

if __name__ == "__main__":
    if sys.argv[1] == "find":
        a = 0
        b = 0
        list_a=[]
        while True:
            try:
                res = check_symmetry(a,b)
            except:
                raise OverflowError(f"Last checked numbers {(a,b)}")
            if res:
                list_a.append((a,b))
                with open('../results','w',encoding='UTF-8') as f:
                    f.write(str(list_a))
            if a == b:
                if a % 10 == 0:
                    print(f"No {a} checked")
                a += 1
                b = 0
            else:
                b += 1

    a = check_symmetry(int(sys.argv[1]),int(sys.argv[2]))
