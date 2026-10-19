#Introduction to sets
#https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    # your code goes here
    res=set(array)
    sum=0
    for i in res:
        sum+=i
    return sum/len(res)
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
