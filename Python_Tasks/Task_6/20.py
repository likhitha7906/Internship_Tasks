#Validating the Phone Number
#https://www.hackerrank.com/challenges/validating-the-phone-number/problem?utm_source=chatgpt.com
# Enter your code here. Read input from STDIN. Print output to STDOUTp
#patters="r'^[789]\d{9}$"
import re
n=int(input())
for i in range(n):
    num=input()
    pattern=r'^[789]\d{9}$'
    if re.match(pattern,num):
        print("YES")
    else:
        print("NO")
    
