#Find the Runner-up Score
#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    l=float('-inf')
    s_l=float('-inf')
    for i in range(n):
        if arr[i]>l:
            s_l=l
            l=arr[i]
        elif arr[i]<l and arr[i]>s_l:
            s_l=arr[i]
    print(s_l)

