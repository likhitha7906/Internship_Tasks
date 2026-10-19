#sYMMETRIC DIFFERENCE
#https://www.hackerrank.com/challenges/symmetric-difference/problem


# Enter your code here. Read input from STDIN. Print output to STDOUT
n1=int(input())
s1=set(map(int,input().split()))
n2=int(input())
s2=set(map(int,input().split()))

res=s1.symmetric_difference(s2)
for i in sorted(res):
    print(i)