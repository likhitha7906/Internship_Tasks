#Company Logo
#https://www.hackerrank.com/challenges/most-commons/problem
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    d={}
    for i in s:
        d[i]=d.get(i,0)+1
    res=sorted(d.items(),key=lambda x:(-x[1],x[0]))
    for i  in res[:3]:
        print(i[0],i[1])
        
        
        
