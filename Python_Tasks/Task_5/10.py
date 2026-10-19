#Swap Case
#https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    res=""
    for i in s:
        if i.islower():
            res+=i.upper()
        elif i.isupper():
            res+=i.lower()
        else:
            res+=i
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)