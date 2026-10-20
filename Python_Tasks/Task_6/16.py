#Check Subset
#https://www.hackerrank.com/challenges/py-check-subset/problem
# Enter your code here. Read input from STDIN. Print output to STDOUTt=
t=int(input())
for i in range(t):
    n=int(input())
    A=set(map(int,input().split()))
    m=int(input())
    B=set(map(int,input().split()))
    print(A.issubset(B))
    